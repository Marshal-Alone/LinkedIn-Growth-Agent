const fs = require('fs');
const content = fs.readFileSync('REACT_BuildInPublic/day-01/post.md', 'utf8');

const postMatch = content.match(/## LinkedIn Post Text \(Ready to Copy and Paste\)\s+([\s\S]*?)\s+---\s+## Visual Assets/);
const postBody = postMatch[1].trim();

// Sentence segmentation
const sentences = postBody.split(/(?<=[.?!])\s+/).map(s => s.trim()).filter(s => s.length > 0 && !s.startsWith('#'));

console.log('Total sentences in post body:', sentences.length);
sentences.forEach((s, idx) => {
  const words = s.split(/\s+/).length;
  console.log(`S${idx + 1} (${words}w): ${s}`);
});

// Check staccato stacks (3 consecutive sentences with <= 3 words)
for (let i = 0; i < sentences.length - 2; i++) {
  const w1 = sentences[i].split(/\s+/).length;
  const w2 = sentences[i+1].split(/\s+/).length;
  const w3 = sentences[i+2].split(/\s+/).length;
  if (w1 <= 3 && w2 <= 3 && w3 <= 3) {
    console.warn(`WARNING: Possible staccato stack at sentences ${i+1}-${i+3}: "${sentences[i]}" / "${sentences[i+1]}" / "${sentences[i+2]}"`);
  }
}
