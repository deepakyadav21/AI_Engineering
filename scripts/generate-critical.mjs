import * as critical from 'critical';

try {
  await critical.generate({
    base: '.',
    src: 'index.html',
    css: ['files/style.purged.css'],
    dimensions: [
      { width: 375, height: 812 },
      { width: 1366, height: 768 }
    ],
    target: {
      css: 'files/critical.css'
    },
    inline: false
  });
  console.log('Wrote files/critical.css');
} catch (e) {
  console.error(e);
  process.exit(1);
}
