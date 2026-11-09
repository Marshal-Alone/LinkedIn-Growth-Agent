const fs = require('fs');

const path = 'REACT_BuildInPublic/day-01/post.md';
const content = fs.readFileSync(path, 'utf8');

console.log('=== VERIFICATION OF post.md ===');

// 1. Backtick count across the whole file
const totalBackticks = (content.match(/`/g) || []).length;
console.log('1. Total Backticks in entire post.md:', totalBackticks);

// 2. Extract post body
const parts = content.split('## LinkedIn Post Text (Ready to Copy and Paste)');
if (parts.length < 2) {
  console.error('Error: Could not find LinkedIn post section!');
  process.exit(1);
}
const postBody = parts[1].split('---')[0].trim();

const postBackticks = (postBody.match(/`/g) || []).length;
console.log('2. Backticks in post body:', postBackticks);

// 3. Length metrics
console.log('3. Post body character count:', postBody.length);
const sentences = postBody.split(/(?<=[.?!])\s+/).filter(s => s.trim().length > 0);
console.log('4. Post body sentence count:', sentences.length);

// 4. Hook analysis
const lines = postBody.split(/\r?\n/).filter(l => l.trim().length > 0);
console.log('5. First line (hook):', lines[0]);
console.log('6. Hook character count:', lines[0].length);
console.log('7. Hook ends with question mark:', lines[0].trim().endsWith('?'));

// 5. Line breaks check: Check if paragraphs have empty line separation
const rawLines = postBody.split(/\r?\n/);
let singleBreakDetected = false;
for (let i = 0; i < rawLines.length - 1; i++) {
  if (rawLines[i].trim().length > 0 && rawLines[i + 1].trim().length > 0) {
    console.warn('Warning: Adjacent non-empty lines found without blank line at:', rawLines[i], '->', rawLines[i+1]);
    singleBreakDetected = true;
  }
}
console.log('8. All thoughts separated by double line breaks (no single break collapse):', !singleBreakDetected);

// 6. Core concepts check
const requiredConcepts = [
  { name: 'Node.js runtime prerequisite', pattern: /node\.js/i },
  { name: 'npm create vite@latest vs CRA', pattern: /npm create vite@latest/i },
  { name: 'CRA comparison / startup speed', pattern: /280ms|create-react-app/i },
  { name: 'index.html root div', pattern: /<div id="root">/i },
  { name: 'createRoot and top-level App component', pattern: /createRoot.*App|App.*createRoot/is },
  { name: 'Components as functions', pattern: /component is simply a javascript function/i },
  { name: 'PascalCase naming vs lowercase HTML tags', pattern: /PascalCase/i },
  { name: 'JSX fragments (<> and </>) eliminating div soup', pattern: /div soup.*fragments|fragments.*div soup/is }
];

console.log('9. Core Concepts Verification:');
requiredConcepts.forEach(c => {
  const match = c.pattern.test(postBody);
  console.log(`   - ${c.name}: ${match ? 'PASS' : 'FAIL'}`);
});

// 7. Humanizer / AI Vocab Check
const bannedWords = [
  'significant', 'crucial', 'notably', 'particularly', 'comprehensive',
  'insights', 'robust', 'leverage', 'foster', 'landscape',
  'nuanced', 'multifaceted', 'holistic', 'streamline', 'elevate',
  'empower', 'fundamentally', 'essentially', 'ultimately', 'seamless'
];
const foundBanned = bannedWords.filter(w => new RegExp(`\\b${w}\\b`, 'i').test(postBody));
console.log('10. Banned AI Vocabulary matches:', foundBanned.length === 0 ? 'CLEAN (0 found)' : foundBanned);

// 8. Banned structural patterns
const revealBridges = ['the result?', 'plot twist:', 'here\'s what', 'here\'s how'];
const foundReveal = revealBridges.filter(b => postBody.toLowerCase().includes(b));
console.log('11. Reveal bridges:', foundReveal.length === 0 ? 'CLEAN (0 found)' : foundReveal);

const negativeParallelism = ['it\'s not', 'it is not'];
const foundNeg = negativeParallelism.filter(np => postBody.toLowerCase().includes(np));
console.log('12. Negative parallelism:', foundNeg.length === 0 ? 'CLEAN (0 found)' : foundNeg);

// 9. Hashtags
const hashtags = postBody.match(/#\w+/g) || [];
console.log('13. Hashtags count:', hashtags.length, 'Tags:', hashtags);

// 10. Archify reference in P.S.
const hasArchifyPs = /P\.S\..*Archify/i.test(postBody);
console.log('14. P.S. note references Archify:', hasArchifyPs ? 'PASS' : 'FAIL');

// 11. Closing question for seniors
const hasClosingQ = /senior.*frontend|hardest mental shift/i.test(postBody) && postBody.includes('?');
console.log('15. Closing question for seniors:', hasClosingQ ? 'PASS' : 'FAIL');

// 12. Screenshots check in the file
const hasTerminal = /Screenshot 1: Terminal Setup/i.test(content) && /ready in 280 ms/i.test(content);
const hasFileTree = /Screenshot 2:.*File Tree/i.test(content) && /index\.html/i.test(content);
const hasCodeSnippet = /Screenshot 3:.*Functional Component/i.test(content) && /WelcomeBanner/i.test(content);
const hasDevTools = /Screenshot 4:.*DevTools/i.test(content) && /<div id="root">/i.test(content);
console.log('16. Screenshot 1 (Terminal) present:', hasTerminal ? 'PASS' : 'FAIL');
console.log('17. Screenshot 2 (File Tree) present:', hasFileTree ? 'PASS' : 'FAIL');
console.log('18. Screenshot 3 (Code Snippet) present:', hasCodeSnippet ? 'PASS' : 'FAIL');
console.log('19. Screenshot 4 (Browser DevTools) present:', hasDevTools ? 'PASS' : 'FAIL');

console.log('=== VERIFICATION COMPLETE ===');
