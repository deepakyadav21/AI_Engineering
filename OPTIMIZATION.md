OPTIMIZATION RECORD

Date: 2026-08-09

Summary of changes applied to improve performance:

- Reordered CSS so Bootstrap loads early and the theme stylesheet loads last.
- Replaced duplicate `style.css` reference with a `preload` + `noscript` fallback to avoid render-blocking.
- Added `defer` to all script tags so JS loads without blocking initial render and preserves execution order.
- Inserted a small `DOMContentLoaded` script that sets `loading="lazy"` on images and hides the initial spinner.

Files changed:
- index.html
- OPTIMIZATION.md (this file)

Recommended next steps (not applied):
- Compress and convert large images to WebP/AVIF and update `src` references.
- Remove unused CSS rules or generate a critical CSS subset and inline it for the hero section.
- Concatenate and minify JS and CSS, or serve via a CDN.
- Enable gzip/Brotli compression and set long cache headers on static assets via server configuration.
- Rename `.download` JS files to proper `.js` filenames and ensure correct MIME types on server.
- Run Lighthouse or PageSpeed Insights and iterate on specific suggestions.

Updates performed (2026-08-09):
- Renamed `.download` JS assets to `.js` and updated HTML references.
- Added split pages: `about.html`, `projects.html`, `contact.html` to improve navigation and session length.
- Updated site color scheme to a teal/coral palette and enhanced button styles.
- Added AOS (Animate On Scroll) for smooth scroll-triggered animations and initialized it site-wide.
- Added CTAs and improved accessibility (alt text, `visually-hidden`, meta update).

Notes on image optimization:
- I attempted to convert images to WebP but a local Python runtime was not available in the environment, so I did not convert images automatically. If you'd like, I can either convert images on my side and commit them, or provide step commands for you to run locally.

If you want, I can proceed with any of the following:
- Convert images to WebP/AVIF (requires Python or imagemagick locally) and update HTML to use them.
- Run a Lighthouse audit and apply further recommendations.
- Push branch `portfolio` to your GitHub remote (provide repo URL or add remote locally and I'll push).
I added a Node helper to convert images to WebP/AVIF:

- `scripts/convert-images.js` — Node script using `sharp` that converts JPG/PNG files in `files/` to WebP and AVIF and places them in `files/optimized/`.
- `package.json` and `README_CONVERT.md` — instructions to install dependencies and run the converter locally.

Run locally:
```bash
npm install
npm run convert-images
```
After conversion update your HTML to use `<picture>` elements to serve AVIF/WebP with JPG fallbacks (see README_CONVERT.md).
