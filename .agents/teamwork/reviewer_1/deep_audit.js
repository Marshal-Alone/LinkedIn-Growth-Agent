const fs = require('fs');

const content = fs.readFileSync('REACT_BuildInPublic/day-01/post.md', 'utf8');
const lines = content.split(/\r?\n/);

console.log('Total lines:', lines.length);

console.log('\n--- Checking lines 4 to 63 (0-indexed 3 to 62) ---');
for (let i = 4; i <= 62; i++) {
  console.log(`L${i + 1} [${lines[i].trim() === '' ? 'BLANK' : 'TEXT'}]: ${lines[i]}`);
}

console.log('\n--- Checking consecutive blank/text in post body ---');
let prevBlank = true;
let violations = [];
for (let i = 4; i <= 60; i++) {
  const isBlank = lines[i].trim() === '';
  if (!isBlank && !prevBlank) {
    violations.push({ line: i + 1, text: lines[i] });
  }
  prevBlank = isBlank;
}

if (violations.length === 0) {
  console.log('SUCCESS: Every single paragraph/thought in post body is separated by blank line (\\n\\n).');
} else {
  console.log('VIOLATIONS in post body:', violations);
}

// Check Unicode backticks and quote variants across whole file
const suspiciousChars = [
  { name: 'GRAVE ACCENT / Backtick (0x60)', char: '\u0060' },
  { name: 'MODIFIER LETTER GRAVE ACCENT (0x02CB)', char: '\u02CB' },
  { name: 'MODIFIER LETTER LOW GRAVE ACCENT (0x02CE)', char: '\u02CE' },
  { name: 'REVERSED PRIME (0x2035)', char: '\u2035' }
];

suspiciousChars.forEach(sc => {
  const matches = (content.match(new RegExp(sc.char, 'g')) || []).length;
  console.log(`Character ${sc.name}: ${matches}`);
});
