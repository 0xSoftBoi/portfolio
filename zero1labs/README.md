# Zero-1 Labs — website

A self-contained landing page for **Zero-1 Labs**, the research-and-build holding
company taking ideas 0→1 across crypto, security, AI, robotics, materials, and gaming.

- **Single file, zero dependencies.** Everything is in `index.html` — all visuals
  are CSS + `<canvas>` (a generative "0→1" particle field and per-venture motifs),
  so there are no images or build step to carry around. Fonts load from Google Fonts.
- Honest, verifiable framing matching the founder's other work: every vertical links
  to a real public repo or live product, and anything unproven is tagged `exploring`.

## Preview locally

```bash
# from this folder
python3 -m http.server 8000
# open http://localhost:8000
```

Or just open `index.html` in a browser.

## Publish it to its own repo + GitHub Pages

This folder is built to lift cleanly into a dedicated `zero1labs` repo (the current
session couldn't create it — repo creation was outside its permissions). Once you've
created an empty `zero1labs` repo on GitHub:

```bash
# copy this folder out to a fresh checkout, then:
cd zero1labs
git init -b main
git add index.html README.md
git commit -m "Zero-1 Labs site"
git remote add origin git@github.com:0xSoftBoi/zero1labs.git
git push -u origin main
```

Then enable Pages: **Settings → Pages → Source: `main` / root**. The site goes live at
`https://0xsoftboi.github.io/zero1labs/` (or your custom domain, e.g. `zero1labs.com`,
by adding a `CNAME` file with the domain and pointing DNS at GitHub Pages).

## Edit the content

All site content lives in the `<script>` data blocks near the top of `index.html`:

- `VERTS` — the six verticals and the representative repos listed under each.
- `FLAGS` — the flagship venture cards (Suwappu, Onchain Rover).
- Hero copy, About, and contact links are plain HTML in the body.

Add a venture by appending a row `["repo-name","one-line description","https://…","live|explore|"]`
to the relevant vertical's `rows` array.
