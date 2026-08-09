const { PurgeCSS } = require('purgecss');
const fs = require('fs');

(async () => {
  try {
    const critical = await import('critical');

    console.log('Running PurgeCSS...');
    const purgeResult = await new PurgeCSS().purge({
      content: ['index.html', 'about.html', 'projects.html', 'contact.html'],
      css: ['files/style.css']
    });
    const purged = purgeResult[0].css;
    fs.writeFileSync('files/style.purged.css', purged);
    console.log('Wrote files/style.purged.css');

    console.log('Generating critical CSS...');
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
      inline: false,
      penthouse: { blockJSRequests: false }
    });

    console.log('Wrote files/critical.css');
  } catch (err) {
    console.error(err);
    process.exit(1);
  }
})();
