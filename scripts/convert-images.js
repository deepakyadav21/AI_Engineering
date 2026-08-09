// Convert images to WebP and AVIF using sharp
// Usage: npm install sharp && node scripts/convert-images.js
const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const srcDir = path.join(__dirname, '..', 'files');
const outDir = path.join(srcDir, 'optimized');
const exts = ['.jpg', '.jpeg', '.png'];

if (!fs.existsSync(outDir)) fs.mkdirSync(outDir);

async function convertFile(file){
  const full = path.join(srcDir, file);
  const name = path.parse(file).name;
  try{
    await sharp(full).webp({quality:80}).toFile(path.join(outDir, name + '.webp'));
    await sharp(full).avif({quality:50}).toFile(path.join(outDir, name + '.avif'));
    console.log('Converted', file);
  }catch(err){
    console.error('Error converting', file, err.message);
  }
}

(async ()=>{
  const files = fs.readdirSync(srcDir).filter(f => exts.includes(path.extname(f).toLowerCase()));
  for(const f of files){
    await convertFile(f);
  }
  console.log('Done. Optimized images are in files/optimized');
})();
