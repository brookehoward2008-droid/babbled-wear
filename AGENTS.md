# AGENTS.md — BaBBled Wear

Shared source of truth for all AI coding agents (Claude, Codex, Copilot, Cursor).

---

## What this repo is

Static website for BaBBled art studio (Brooke Chauntel). Four HTML pages. Python scripts generate training assets locally. No TypeScript. No tests. No bundler.

---

## Stack

| Layer | Tech |
|---|---|
| Pages | HTML5, CSS3, ES6 — all inline, no separate files |
| Asset generation | Python 3: Pillow, python-pptx, qrcode |
| Deployment | GitHub Actions → GitHub Pages (push to `main`) |

---

## Pages

| File | What it does |
|---|---|
| `index.html` | Galleries (art, photography, nature), shop links, about |
| `presentation.html` | 13-slide training deck, keyboard nav, CSS display toggle |
| `sandbox.html` | File upload + dynamic form for PDF practice |
| `status.html` | Fetches Gumroad reachability, shows live status cards |

---

## Design tokens (CSS variables in every page's `:root`)

```
--pink:   #ff2d87
--purple: #7b2cbf
--yellow: #ffd60a
--ink:    #0f0f14
--paper:  #fafafa
```

Always use variables. Never hardcode colors.

---

## Rules that cannot be broken

- No separate `.css` or `.js` files — inline only
- No bundlers, transpilers, or frameworks
- No hardcoded secrets, tokens, or wallet addresses in any file
- Every `<img>` needs a descriptive `alt` attribute
- Add `loading="lazy"` to all gallery images
- Keep semantic elements: `<header>`, `<main>`, `<section>`, `<footer>`, `<figure>`
- Never commit `.env`, SSH keys, or credential files
- Never push directly to `main` — use a branch and PR

---

## Commit convention

Imperative, lowercase, under 72 chars. Body explains why if needed.

```
add nature gallery section to index.html
fix slide 7 navigation on mobile
update sandbox drag-drop to accept .webp
```

---

## Writing rules (applies to all copy, alt text, comments, docs)

Full ruleset: `.github/copilot-instructions.md`

Short version:
- No AI buzzwords: delve, leverage, seamless, robust, tapestry, synergy
- No sycophancy: "Great question!", "Absolutely!", "I hope this helps!"
- No resume verbs: established, ensured, spearheaded, championed
- No forward projections: "Moving forward…", "This positions us well…"
- Be specific — numbers, names, examples. Every paragraph needs one concrete anchor.
- Repeat the right word rather than cycling synonyms

---

## Learning Filter

No generated rule becomes durable unless it has:

1. Direct evidence from actual repo files (not assumed from language patterns)
2. At least three examples, or explicit human approval
3. A confidence note (certain / likely / inferred)
4. A conflict check against this file — resolve before adding

If a rule fails any of these, mark it as provisional. Do not silently merge it into permanent guidance.

---

## Conflict Priority Ladder

When instructions disagree, apply this order (top wins):

1. **Safety and privacy** — no secrets, no force-pushes, no destructive commands without confirmation
2. **User intent** — what the person asked for in this session
3. **Repo truth** — what the actual files show (not assumed from framework conventions)
4. **Agent instructions** — CLAUDE.md, AGENTS.md, copilot-instructions.md
5. **Style and tone** — writing rules, naming conventions

If a lower priority item conflicts with a higher one, flag the conflict before acting. Do not silently pick the path of least resistance.

---

## Where to find more

- `CLAUDE.md` — full AI reference: page internals, Python scripts, deploy, storefronts
- `.github/copilot-instructions.md` — complete writing + coding ruleset
- `rb-listings.md` — Redbubble upload specs (4667×6000 px @ 333 DPI)
