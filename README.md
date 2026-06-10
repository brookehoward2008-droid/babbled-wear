# BaBBled Wear — website

Static art-studio site for BaBBled (Brooke Chauntel). Four self-contained HTML pages, no build step. Push to `main` and GitHub Actions deploys.

## Pages

| File | Purpose |
|---|---|
| `index.html` | Landing page — galleries, shop links, about |
| `presentation.html` | 13-slide training deck (saving images as PDFs) |
| `sandbox.html` | Interactive practice page for the training |
| `status.html` | Live Gumroad reachability check |

## Deploy

### Automatic (primary)

Push to `main` → `.github/workflows/main.yml` deploys to GitHub Pages at:

```
https://brookehoward2008-droid.github.io/babbled-wear/
```

### Manual — dual remote (Windows, secondary)

`publish.bat` pushes to two remotes in one step:

| Remote | Repo | URL |
|---|---|---|
| `droid` | `brookehoward2008-droid/babbled-wear` | https://brookehoward2008-droid.github.io/babbled-wear/ |
| `business` | `babbledllc/babbledllc.github.io` | https://babbledllc.github.io/ |

## Python build scripts

Run locally to regenerate training assets. Not part of CI.

```bash
pip install Pillow python-pptx qrcode

python build_mockups.py    # img/training/*.png (5 mockups)
python render_previews.py  # slide_previews/*.png (13 slides + contact sheet)
python build_pptx.py       # Save-Images-as-PDF-Using-Print.pptx
python build_qr.py         # img/training/sandbox-qr.png
```

Commit both the script changes and the regenerated output files.

## First-time remote setup

```bash
git remote add droid   https://github.com/brookehoward2008-droid/babbled-wear.git
git remote add business https://github.com/babbledllc/babbledllc.github.io.git
```

Or just use `publish.bat` on Windows — it handles both remotes.

## Key conventions

- No separate `.css` or `.js` files — all styles and scripts are inline in each HTML file
- Use CSS variables: `--pink`, `--purple`, `--yellow`, `--ink`, `--paper`
- Every `<img>` needs an `alt` attribute and `loading="lazy"` for gallery images
- Generated output files (`slide_previews/`, `img/training/`, `.pptx`) are committed

See `CLAUDE.md` for full AI-assistant reference and `AGENTS.md` for quick-start rules.
