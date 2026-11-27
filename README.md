# Tattva Digital Labs website

Live at https://tattvadigitallabs.github.io (GitHub Pages, `main` branch).

| Page | Path |
|---|---|
| Company home (all apps) | `/` |
| Tattva Image Compressor | `/image-compressor/` |
| Tattva Finance Calculator | `/finance-calculator/` |
| Privacy (company + one section per app) | `/privacy/` (`#image-compressor`, `#finance-calculator`) |
| Support (app chooser + FAQ per app) | `/support/` |

## Editing
Pages are generated from `scripts/build_site.py` (shared header, footer and sections):

```bash
python3 scripts/build_site.py .
```

To add a new app: add its icon to `assets/brand/`, a card in the home "Our apps" section, a product page, a section in the privacy page and a chooser card + FAQ block in support.

## Brand
- Company mark: `assets/brand/tattva-mark.svg` (the "T." monogram). Use this for Tattva Digital Labs only.
- App icons are separate per product: `assets/brand/image-compressor-icon.svg`, `assets/brand/finance-calculator-icon.svg`.
- Font: Manrope by Mikhail Sharanda, SIL Open Font License 1.1 (self-hosted, no third-party requests).
