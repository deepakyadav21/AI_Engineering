const fs = require('fs');
const files = ['index.html', 'about.html', 'projects.html', 'contact.html'];
for (const file of files) {
  let content = fs.readFileSync(file, 'utf8');
  content = content.replace(/\s+wow fadeInUp/g, '');
  content = content.replace(/data-wow-delay="0\.1s"/g, 'data-aos-delay="100"');
  content = content.replace(/data-wow-delay="0\.2s"/g, 'data-aos-delay="200"');
  content = content.replace(/data-wow-delay="0\.5s"/g, 'data-aos-delay="500"');
  content = content.replace(/data-wow-delay="0\.8s"/g, 'data-aos-delay="800"');
  content = content.replace(/style="visibility: visible; animation-delay: 0\.1s; animation-name: fadeInUp;"/g, '');
  content = content.replace(/style="visibility: visible; animation-delay: 0\.5s; animation-name: fadeInUp;"/g, '');
  content = content.replace(/<script src="\.\/files\/wow\.min\.js" defer><\/script>\s*/g, '');
  fs.writeFileSync(file, content, 'utf8');
}
const mainPath = 'files/main.js';
let main = fs.readFileSync(mainPath, 'utf8');
main = main.replace(/\s*new WOW\(\)\.init\(\);\s*/g, '\n');
fs.writeFileSync(mainPath, main, 'utf8');
console.log('Animation cleanup done.');
