const fs = require('fs');
const path = require('path');

const targetPath = path.resolve('c:/Users/marsh/OneDrive/Desktop/LinkedIN/REACT_BuildInPublic/day-01/post.md');
console.log('Auditing target:', targetPath);

if (!fs.existsSync(targetPath)) {
  console.error('FAIL: Target file does not exist!');
  process.exit(1);
}

const rawContent = fs.readFileSync(targetPath, 'utf8');

// 1. Backtick check across entire file
const backtickCount = (rawContent.match(/`/g) || []).length;
console.log('1. Backtick count across whole file:', backtickCount);

// 2. Line breaks analysis
// Extract post body (between ## LinkedIn Post Text and ---)
const postMatch = rawContent.match(/## LinkedIn Post Text \(Ready to Copy and Paste\)\s+([\s\S]*?)\s+---\s+## Visual Assets/);
if (!postMatch) {
  console.error('FAIL: Could not extract LinkedIn Post Text section');
}
const postBody = postMatch ? postMatch[1].trim() : '';
console.log('Post body extracted length:', postBody.length);

const postLines = postBody.split(/\r?\n/);
let consecutiveNonEmptyLines = [];
for (let i = 0; i < postLines.length - 1; i++) {
  if (postLines[i].trim() !== '' && postLines[i + 1].trim() !== '') {
    consecutiveNonEmptyLines.push({
      lineNum: i + 1,
      curr: postLines[i],
      next: postLines[i + 1]
    });
  }
}
console.log('2. Post body consecutive non-empty lines (single line breaks collapsing):', consecutiveNonEmptyLines.length);
if (consecutiveNonEmptyLines.length > 0) {
  console.log('Found consecutive lines:', consecutiveNonEmptyLines);
}

// 3. Hook analysis
const firstLine = postLines.find(l => l.trim().length > 0);
console.log('3. Hook line:', firstLine);
console.log('   Hook length:', firstLine.length);
console.log('   Hook ends with question mark:', firstLine.trim().endsWith('?'));
console.log('   Hook has number/formula:', /\d+/.test(firstLine));

// 4. Banned buzzwords
const bannedWords = [
  'leverage', 'leveraging', 'leveraged', 'leverages',
  'crucial', 'landscape', 'comprehensive', 'robust',
  'delve', 'delving', 'testament', 'game-changer',
  'seamless', 'seamlessly', 'streamline', 'streamlined', 'streamlines',
  'revolutionize', 'revolutionizing', 'tapestry', 'unleash', 'unlock',
  'pivotal', 'elevate', 'foster', 'beacon', 'vital',
  'dive deep', 'deep dive', 'fast-paced', 'in today\'s'
];

const foundBanned = [];
bannedWords.forEach(word => {
  const regex = new RegExp(`\\b${word}\\b`, 'gi');
  const matches = postBody.match(regex);
  if (matches) {
    foundBanned.push({ word, count: matches.length });
  }
});
console.log('4. Banned buzzwords in post body:', foundBanned);

// Also check banned words in entire file
const foundBannedInFile = [];
bannedWords.forEach(word => {
  const regex = new RegExp(`\\b${word}\\b`, 'gi');
  const matches = rawContent.match(regex);
  if (matches) {
    foundBannedInFile.push({ word, count: matches.length });
  }
});
console.log('   Banned buzzwords in entire file:', foundBannedInFile);

// 5. Reveal bridges & Negative parallelism & Staccato stacks
const revealBridges = [
  /the result\?/i,
  /plot twist:?/i,
  /here's the thing:?/i,
  /here's why:?/i,
  /spoiler alert:?/i,
  /guess what\?/i,
  /truth is:?/i,
  /bottom line:?/i
];
const foundBridges = [];
revealBridges.forEach(regex => {
  if (regex.test(postBody)) {
    foundBridges.push(regex.toString());
  }
});
console.log('5. Reveal bridges in post body:', foundBridges);

const negativeParallelism = [
  /it's not\s+[^,]+,\s+it's\s+/i,
  /not because\s+[^,]+,\s+but because\s+/i,
  /not\s+[^,]+,\s+but\s+/i,
  /it isn't\s+[^,]+,\s+it's\s+/i
];
const foundNegatives = [];
negativeParallelism.forEach(regex => {
  const match = postBody.match(regex);
  if (match) {
    foundNegatives.push(match[0]);
  }
});
console.log('   Negative parallelism in post body:', foundNegatives);

// 6. Senior closing question & P.S. Archify & Hashtags
console.log('6. Closing question check:');
const hasSeniorQuestion = /senior/i.test(postBody) && /\?/.test(postBody);
console.log('   Tailored question for seniors:', hasSeniorQuestion);
const hasArchifyPS = /P\.?S\.?.*Archify/i.test(postBody);
console.log('   P.S. note referencing Archify:', hasArchifyPS);
const hashtagsMatch = postBody.match(/#\w+/g) || [];
console.log('   Hashtags count:', hashtagsMatch.length, hashtagsMatch);

// 7. Content coverage
console.log('7. Technical content coverage in post body:');
console.log('   - Node.js runtime:', /Node\.?js/i.test(postBody));
console.log('   - npm create vite@latest:', /npm create vite@latest/i.test(postBody));
console.log('   - CRA vs Vite / startup speed:', /create-react-app|create react app/i.test(postBody) && /280ms|<300ms/i.test(postBody));
console.log('   - index.html root div:', /<div id="root">/i.test(postBody));
console.log('   - createRoot & App:', /createRoot/i.test(postBody) && /\bApp\b/.test(postBody));
console.log('   - Components as functions:', /component.*function|function.*component/i.test(postBody));
console.log('   - PascalCase vs lowercase HTML:', /PascalCase/i.test(postBody) && /<Button \/>/i.test(postBody) && /<button>/i.test(postBody));
console.log('   - JSX fragments / div soup:', /<>\s*(and|\.\.\.)\s*<\/>|fragment/i.test(postBody) && /div soup/i.test(postBody));

// 8. Screenshot recommendations coverage
console.log('8. Screenshot recommendations:');
const hasSc1 = /### Screenshot 1/i.test(rawContent);
const hasSc2 = /### Screenshot 2/i.test(rawContent);
const hasSc3 = /### Screenshot 3/i.test(rawContent);
const hasSc4 = /### Screenshot 4/i.test(rawContent);
console.log('   Screenshots 1-4 present:', hasSc1 && hasSc2 && hasSc3 && hasSc4);

const scRegex = /### Screenshot \d:([^\n]+)\n+([\s\S]*?)(?=(?:### Screenshot \d|---\s*##|$))/g;
let scMatch;
let scIdx = 1;
while ((scMatch = scRegex.exec(rawContent)) !== null) {
  const title = scMatch[1].trim();
  const body = scMatch[2];
  const hasDesc = /Scene Description:/i.test(body);
  const hasContent = /Exact Content to Display:/i.test(body);
  const hasFraming = /Suggested Framing:/i.test(body);
  const hasRationale = /Narrative Rationale:/i.test(body);
  console.log(`   Screenshot ${scIdx} (${title}):`);
  console.log(`     Scene Description: ${hasDesc}, Content: ${hasContent}, Framing: ${hasFraming}, Rationale: ${hasRationale}`);
  scIdx++;
}
