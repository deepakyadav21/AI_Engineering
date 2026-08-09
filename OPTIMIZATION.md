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

If you want, I can proceed to rename `.download` files, compress images, run a local Lighthouse check, and create a git branch and push the changes to GitHub.
