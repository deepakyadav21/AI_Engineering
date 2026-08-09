const fs = require('fs');
const path = require('path');
const file = path.resolve(__dirname, '..', 'lighthouse-report.html');
const s = fs.readFileSync(file, 'utf8');
const m = s.match(/window.__LIGHTHOUSE_JSON__ = (\{[\s\S]*?\});/);
if (!m) { console.error('No Lighthouse JSON found'); process.exit(2); }
const j = JSON.parse(m[1]);
const cats = j.categories || {};
const out = {};
for (const k of Object.keys(cats)) {
  out[k] = {score: cats[k].score};
}
// collect failing/average performance audits
const audits = j.audits || {};
const problems = [];
const interesting = ['largest-contentful-paint','total-blocking-time','cumulative-layout-shift','speed-index','interactive','unused-css-rules','render-blocking-resources','uses-rel-preconnect','server-response-time'];
for (const id of interesting) {
  if (audits[id]) {
    problems.push({id, title: audits[id].title, score: audits[id].score, displayValue: audits[id].displayValue || audits[id].numericValue || null});
  }
}
console.log(JSON.stringify({categories: out, topProblems: problems}, null, 2));
