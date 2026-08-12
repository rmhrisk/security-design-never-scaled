# Security Design Never Scaled

Standalone long-form post. Published at `https://rmhrisk.github.io/security-design-never-scaled/`.

`index.html` is generated, self-contained, and committed so the site works even if the
workflow is disabled. Everything needed to regenerate it lives in `src/`.

## Layout

```
index.html                     generated, single file, no external assets but web fonts
.nojekyll                      skip Jekyll processing
src/essay.md                   the source of truth; edit this
src/build.py                   markdown -> index.html, numbers figures and citations
src/figs.py                    inline SVG figures
src/style.css                  design tokens and all styling
src/lint_figs.py               geometric layout checker for the figures
src/snap.py                    renders each figure to PNG for visual review
.github/workflows/ci.yml       verifies index.html is in sync and figures are clean
```

## Editing

Edit `src/essay.md`. Never edit `index.html` directly; it is overwritten on every build.

```bash
cd src
pip install markdown
python build.py        # regenerates ../index.html
python lint_figs.py    # must report "0 issue(s)"
```

Figure numbers, citation numbers, and the table of contents are all derived at build
time from document order. Insert a figure or a citation anywhere and everything
downstream renumbers itself.

Citations use named keys rather than numbers. In the prose:

```html
<a class="ref" href="#r-saltzer">[saltzer]</a>
```

and in the Sources list:

```markdown
- <span id="r-saltzer"></span>Saltzer, J. H. and Schroeder, M. D., ...
```

The build assigns display numbers in reading order and sorts the Sources list to match.
It fails loudly on a citation with no source entry, or a source entry never cited.

## Checking the figures

`lint_figs.py` flags paths crossing text, overlapping text, and anything outside the
viewBox. It runs in CI and the deploy fails if it reports anything.

For a visual pass:

```bash
cd src
pip install cairosvg
python snap.py         # writes render/fig01.png ... render/fig14.png
```

## Styling

Every colour and font is a custom property in the `:root` block at the top of
`src/style.css`. The SVG figures reference those variables rather than literal values,
so replacing that block restyles the prose and the figures together. Dark mode is a
`prefers-color-scheme` override of the same tokens.

## Deploying

Repository Settings → Pages → Source: **Deploy from a branch**, branch `main`, folder
`/ (root)`. The committed `index.html` is what gets served, so publication does not
depend on any workflow succeeding.

The `Check` workflow does not deploy. It rebuilds `index.html` from `src/` and fails if
the committed copy is stale, then runs the figure linter. If it breaks, the site stays
up and you have a red check to fix.

## Outstanding before publication

- Sources 3, 6, 11, 14 and 15 carry identifiers but no URL. Add links or leave as-is.
- The Munich Re and Marsh citations point at bodies of work rather than specific
  reports. Either narrow the claim in section 10 or cite the exact publications.
