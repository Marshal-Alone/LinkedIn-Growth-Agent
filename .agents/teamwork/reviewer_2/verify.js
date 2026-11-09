const fs = require('fs');

const html = fs.readFileSync('REACT_BuildInPublic/day-01/architecture.html', 'utf8');

const nodeKindMatches = [...html.matchAll(/data-node-kind="([^"]+)"/g)].map(m => m[1]);
console.log('Node kinds found:', nodeKindMatches);

const legendKindMatches = [...html.matchAll(/data-legend-semantic-kind="([^"]+)"/g)].map(m => m[1]);
console.log('Legend kinds found:', legendKindMatches);

const cloudNodes = nodeKindMatches.filter(k => k === 'cloud');
const securityNodes = nodeKindMatches.filter(k => k === 'security');
const backendNodes = nodeKindMatches.filter(k => k === 'backend');

console.log('Legacy anomalies check:', {
  cloudCount: cloudNodes.length,
  securityCount: securityNodes.length,
  backendCount: backendNodes.length
});

const nodeIds = [...html.matchAll(/data-node-id="([^"]+)"/g)].map(m => m[1]);
console.log('Node IDs found in order:', nodeIds);

const edgeIds = [...html.matchAll(/data-edge-id="([^"]+)"/g)].map(m => m[1]);
console.log('Edge IDs found:', edgeIds);

const edgeLabels = [...html.matchAll(/data-edge-label="([^"]+)"/g)].map(m => m[1]);
console.log('Edge labels found:', edgeLabels);
