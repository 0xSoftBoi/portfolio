# Zero-1 Labs — website

A cinematic landing page for **Zero-1 Labs**, the research-and-build holding
company taking ideas from zero to one across crypto, security, AI, robotics,
materials, and gaming.

## Design

Gallery-dark and editorial — the register of a cinematography / photography
portfolio rather than a dashboard:

- **Full-frame "scenes."** The portfolio is told as six chapters, each a
  full-viewport graded image (`assets/*.webp`) with a lower-third title card,
  a logline, and the ventures listed beneath — like a cinematographer's reel.
- **One serif, one mono.** [Fraunces](https://fonts.google.com/specimen/Fraunces)
  (optical display) for headlines + Inter for body + JetBrains Mono for
  captions, timecodes, and data. Numbers are set in tabular figures.
- **Cinematic framing & grade.** Letterbox bars, a consistent teal/amber color
  grade across all imagery, a very subtle film grain, and a holding-company
  "ledger" interstitial.
- **Motion with meaning, not decoration.** A slow Ken-Burns hero, transform-only
  parallax on each scene, and long-eased reveals. Everything is GPU-cheap,
  pauses via the on-screen toggle, and fully respects `prefers-reduced-motion`.
- **Discoverable & accessible.** JSON-LD `Organization` schema, OG/Twitter
  tags, an SVG favicon, a skip link, descriptive `alt` text, and visible focus
  rings.

Every vertical links to a real public repo or live product; anything unproven
is tagged `exploring`.

## Files

```
index.html          the cinematic site (current)
index-hud.html      the earlier neon/HUD version, kept for reference
assets/             8 graded .webp scene images (hero + 6 chapters + ledger)
```

## Preview locally

```bash
python3 -m http.server 8000   # from this folder, then open http://localhost:8000
```

## Publish to its own repo + GitHub Pages

This folder is self-contained and ready to lift into a dedicated `zero1labs`
repo (the build session couldn't create it — repo creation was outside its
permissions). Once you've made an empty `zero1labs` repo on GitHub:

```bash
# copy this folder into a fresh checkout, then:
cd zero1labs
git init -b main
git add .
git commit -m "Zero-1 Labs site"
git remote add origin git@github.com:0xSoftBoi/zero1labs.git
git push -u origin main
```

Then enable Pages: **Settings → Pages → Source: `main` / root**. Live at
`https://0xsoftboi.github.io/zero1labs/`, or a custom domain (e.g. `zero1labs.com`)
via a `CNAME` file + DNS.

## Edit the content

- The six chapters live in the `CH` array near the bottom of `index.html` —
  each with its image, title, logline, body, and venture rows
  `["repo","one-line description","https://…","live|explore|"]`.
- Hero, logline, ledger figures, About, and contact are plain HTML in the body.
- To re-cast an image, drop a new `assets/<key>.webp` (landscape, ~2:1, dark
  works best with the grade) and keep the filename.
