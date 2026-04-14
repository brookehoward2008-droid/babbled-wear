# baBBled wear — website

Static holding page. Pushed to two GitHub repos so the same site lives at both URLs.

## Files
- `index.html` — the entire site, one self-contained file
- `publish.bat` — double-click to push to GitHub (menu: personal / business / both)

## Remotes
| Remote | Repo | Published URL |
|---|---|---|
| `personal` | `brookehoward2008/babbled-wear` | https://brookehoward2008.github.io/babbled-wear/ |
| `business` | `babbledllc/babbledllc.github.io` | https://babbledllc.github.io/ |

## Before the first publish
One-time setup per account:

### Personal (brookehoward2008)
1. Log in to GitHub as `brookehoward2008@gmail.com`
2. Create a new empty repo named `babbled-wear` (Public, no README/gitignore)
3. Run `publish.bat` → choose `1`
4. On GitHub: repo **Settings** → **Pages** → Source = `main` branch, `/ (root)` → Save
5. Site goes live in ~60 sec at https://brookehoward2008.github.io/babbled-wear/

### Business (babbledllc)
1. Create a GitHub account at `babbledllc@gmail.com` (if not already)
2. Create a new empty repo named **exactly** `babbledllc.github.io` (the name = the URL)
3. Run `publish.bat` → choose `2`
4. Settings → Pages is auto-enabled for `<user>.github.io` repos
5. Site goes live at https://babbledllc.github.io/

## Day-to-day
Edit `index.html`, double-click `publish.bat`, pick `3` for both.

## Swap out the canonical URL later
When you buy `babbledwear.com`:
- Point the domain's DNS to GitHub Pages (A records: 185.199.108.153 etc)
- Settings → Pages → Custom domain: `babbledwear.com`
- Add `CNAME` file with `babbledwear.com` inside
- Redirect the personal repo to the canonical domain via a `<meta http-equiv="refresh">` tag
