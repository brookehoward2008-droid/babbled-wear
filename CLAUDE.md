# CLAUDE.md — BaBBled Wear

AI assistant reference for the `babbled-wear` repository.

---

## Project Overview

**BaBBled Wear** is the static website and training-materials project for BaBBled, an independent art studio run by Brooke Chauntel. The site showcases original art across multiple galleries, links to external storefronts, and hosts a self-contained training presentation on saving images as PDFs using the browser print function.

---

## Technology Stack

| Layer | Technology |
|---|---|
| Pages | HTML5 (self-contained, no build step) |
| Styles | CSS3 embedded in each HTML file |
| Interactivity | Vanilla JavaScript (ES6, inline) |
| Asset generation | Python 3 — Pillow, python-pptx, qrcode |
| Deployment | GitHub Pages via GitHub Actions |

There is **no package manager, no bundler, and no frontend framework**. Editing an HTML file and pushing to `main` is sufficient to deploy.

---

## Repository Structure

```
babbled-wear/
├── index.html              # Main landing page (galleries, shop links, about)
├── presentation.html       # 13-slide training deck (saving images as PDFs)
├── sandbox.html            # Interactive "Now You Try" practice page
├── status.html             # Live Gumroad reachability status page
│
├── img/                    # All image assets (≈303 MB total)
│   ├── gallery/            # Original art pieces (PNG + JPG)
│   ├── photography/        # Doll photography (JPG)
│   ├── nature/             # Nature/flower photography (JPG)
│   ├── training/           # Generated UI mockups + QR code (PNG)
│   └── *.png / *.svg       # Hero images (moth, mermaids, geisha, etc.)
│
├── slide_previews/         # Generated slide preview PNGs (13 slides + contact sheet)
│
├── build_mockups.py        # Generates training UI mockup PNGs via Pillow
├── build_pptx.py           # Generates .pptx PowerPoint deck via python-pptx
├── build_qr.py             # Generates QR code PNG via qrcode library
├── render_previews.py      # Renders slide previews as PNGs via Pillow
│
├── Save-Images-as-PDF-Using-Print.pptx  # Generated PowerPoint deck
├── publish.bat             # Windows batch script: pushes to dual GitHub remotes
├── rb-listings.md          # Redbubble product upload guide (titles, tags, specs)
├── README.md               # Deployment setup instructions
└── .github/workflows/main.yml  # GitHub Actions: deploy to GitHub Pages on push to main
```

---

## HTML Pages

All four HTML pages are **fully self-contained** — CSS is in `<style>` blocks, JavaScript is in `<script>` blocks, no external stylesheets or JS files.

### `index.html` — Landing Page
- Sections: hero, photography gallery, nature gallery, art gallery, shop links, about, footer
- Uses a CSS Grid with `auto-fit` and `minmax()` for responsive gallery layouts
- All images use `loading="lazy"` for performance
- External links: Redbubble, Gumroad, Zora, Cash App, Farcaster, Instagram

### `presentation.html` — Training Deck
- 13 slides presented as `<div class="slide">` elements
- Navigation via keyboard arrow keys and on-screen prev/next buttons
- Slide visibility is toggled with CSS `display: none` / `display: flex`
- Slide topics: title → hook → objectives → requirements → Windows → Mac → iPhone → shortcuts → sandbox → pitfalls → recap → final tips → contact

### `sandbox.html` — Interactive Practice
- File upload via drag-and-drop and `<input type="file">`
- Dynamic form for customizing PDF output (title, orientation, etc.)
- Step cards for easy / medium / bonus practice tasks

### `status.html` — Storefront Status
- Fetches Gumroad API reachability on page load
- Displays "online" / "offline" status cards with timestamps
- Self-refreshes via JavaScript interval

---

## Design System

All pages share the same CSS custom properties defined in `:root`:

```css
--pink:   #ff2d87
--purple: #7b2cbf
--yellow: #ffd60a
--ink:    #0f0f14   /* near-black background */
--paper:  #fafafa   /* near-white text/surface */
```

Background convention: dark radial gradient using `--ink` and `--purple` tones.  
Typography: system font stack — `-apple-system, BlinkMacSystemFont, "Segoe UI", Inter`.  
No custom web fonts are loaded.

When editing any page, keep new CSS within the same `<style>` block at the top of that file and use the existing CSS variables.

---

## Python Build Scripts

These scripts are run **locally** (not in CI) to regenerate training assets. Run them from the repo root.

| Script | Output | Dependencies |
|---|---|---|
| `build_mockups.py` | `img/training/*.png` — 5 UI mockup images | Pillow |
| `render_previews.py` | `slide_previews/*.png` — 13 slide previews + contact sheet | Pillow |
| `build_pptx.py` | `Save-Images-as-PDF-Using-Print.pptx` | python-pptx |
| `build_qr.py` | `img/training/sandbox-qr.png` | qrcode |

Install Python dependencies (no requirements.txt exists; install ad-hoc):

```bash
pip install Pillow python-pptx qrcode
```

Regenerate all training assets:

```bash
python build_mockups.py
python render_previews.py
python build_pptx.py
python build_qr.py
```

---

## Deployment

### Automatic (GitHub Actions)

Pushing to `main` triggers `.github/workflows/main.yml`, which deploys the site to GitHub Pages automatically. No manual steps needed after a push.

### Manual (Dual Remote — Windows)

`publish.bat` pushes to both the personal GitHub Pages repo and the business org repo:

```
personal  →  github.com/brookehoward2008/babbled-wear
business  →  github.com/babbledllc/babbledllc.github.io
```

Run `publish.bat` on Windows after making changes. It handles both remotes in one step.

---

## Development Workflow

### Day-to-day changes (HTML/content/images)

1. Edit the relevant `.html` file directly.
2. Add or replace images in `img/` as needed.
3. Commit and push to `main`.
4. GitHub Actions deploys automatically.

### Training material updates

1. Edit the Python build script(s) for the content that changed.
2. Run the relevant script(s) locally to regenerate assets.
3. Commit both the script changes **and** the regenerated output files.
4. Push to `main`.

### Adding new gallery images

- Place the image file in the appropriate `img/` subdirectory (`gallery/`, `photography/`, or `nature/`).
- Add an `<img>` tag in the relevant section of `index.html` with an `alt` attribute and `loading="lazy"`.
- Follow the existing `<figure>` / `<img>` markup pattern already present in that section.

---

## Key Conventions

- **No build step for HTML** — edit files directly; do not introduce bundlers or transpilers.
- **Inline styles only** — all CSS lives in `<style>` blocks inside each HTML file; do not create separate `.css` files.
- **Inline scripts only** — all JavaScript lives in `<script>` blocks; do not create separate `.js` files.
- **Use CSS variables** — always reference `--pink`, `--purple`, `--yellow`, `--ink`, `--paper` instead of hardcoding color values.
- **Alt text required** — every `<img>` must have a descriptive `alt` attribute.
- **Lazy loading** — add `loading="lazy"` to all gallery images.
- **Accessibility** — keep semantic HTML (`<header>`, `<main>`, `<section>`, `<footer>`, `<figure>`, etc.); do not replace semantic elements with bare `<div>`s.
- **Privacy** — `.gitignore` excludes `.private.txt`, `.private.md`, `.env`, `.env.*`, `wallets-private.txt`. Never commit these files.
- **Generated files belong in the repo** — `slide_previews/`, `img/training/`, and the `.pptx` file are committed output artifacts; regenerate locally and commit when the source scripts change.

---

## No Test Suite

There is no automated test framework. Quality verification is manual — open the HTML files in a browser and confirm the feature works correctly. When making changes to `presentation.html`, verify slide navigation still works. For `status.html`, verify the Gumroad check renders status cards.

---

## External Storefronts

The site links to but does not control these platforms:

| Platform | Purpose |
|---|---|
| Redbubble | Print-on-demand merchandise |
| Gumroad | Digital product sales (status checked by `status.html`) |
| Zora | NFT / digital collectibles |
| Cash App | Direct tipping / payment |
| Farcaster | Web3 social presence |
| Instagram | Photography and art portfolio |

See `rb-listings.md` for Redbubble upload specifications (dimensions: 4667×6000 px @ 333 DPI).
