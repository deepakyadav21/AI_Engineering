Image conversion helper

This repository includes a small Node.js script to convert JPG/PNG images in `files/` to WebP and AVIF formats.

Prerequisites
- Node.js (14+)
- npm

Install and run:

```bash
npm install
npm run convert-images
```

Output
- Converted images will be saved to `files/optimized/` as `.webp` and `.avif` files.

Once converted, update image references in your HTML to use `<picture>` with WebP/AVIF fallbacks for best results.

Example snippet:

<picture>
  <source type="image/avif" srcset="files/optimized/example.avif">
  <source type="image/webp" srcset="files/optimized/example.webp">
  <img src="files/example.jpg" alt="...">
</picture>
