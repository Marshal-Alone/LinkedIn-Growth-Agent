# 🤖 Instructions for AI Agents & Pair Programmers

> **Notice to AI Assistants (Antigravity, Claude Code, Cursor, Windsurf, Cline, Copilot)**:  
> When the user asks you to help them document their React learning journey, you must follow the operating manual below. Do not generate generic AI summaries or textbook lectures.

---

## 🎯 Mission
When the user shares raw notes, terminal commands, or code for a new learning day (e.g., *"Here is what I learned today on Day 2: ... "*):
1. **Create the daily directory**: `day-XX/`.
2. **Draft the LinkedIn Post**: Fully humanized, compliant with 2026 engagement heuristics, and formatted for the mobile LinkedIn feed.
3. **Generate Visual Proof Recommendations**: 4 specific screenshot setups (terminal, folder tree, code snippet, browser inspection) with exact tools, padding, and callouts.
4. **Author & Render an Archify Architecture Diagram**: Interactive SVG (`architecture.html`) and high-resolution PNG (`diagram.png`).
5. **Update the Tracker**: Add the entry to `README.md`.

---

## 🛠️ Archify Skill: Installation & Usage Guide

Archify renders validated, interactive HTML/SVG architecture diagrams from a small typed JSON specification.

### 1. Check if Archify is Installed
Check common skill directories:
- Windows: `%USERPROFILE%\.gemini\config\skills\archify\bin\archify.mjs`
- Mac/Linux: `~/.gemini/config/skills/archify/bin/archify.mjs` or `~/.claude/skills/archify/bin/archify.mjs`

Run check:
```bash
node <path-to-archify>/bin/archify.mjs --help
```

### 2. If Archify is Missing: How to Install
If Archify is not detected on the host system, install it using the skills CLI or clone it:
```bash
# Via Skills CLI
npx skills add https://github.com/tt-a1i/archify

# Or clone directly into your agent skills directory
git clone https://github.com/tt-a1i/archify.git ~/.gemini/config/skills/archify
cd ~/.gemini/config/skills/archify && npm install
```

### 3. Diagram Authoring & Delivery Pipeline
For each day's technical concept:
1. **Author the JSON Candidate**: Create `day-XX/architecture.json` conforming to the Archify `architecture` schema.
   - `meta.quality_profile`: `"showcase"`
   - `meta.viewBox`: `"0 0 1760 820"` (or balanced 16:9)
   - Component kinds: `frontend`, `backend`, `database`, `cloud`, `security`, `messagebus`, `external`.
2. **Validate**:
   ```bash
   node <archify-path>/bin/archify.mjs validate architecture day-XX/architecture.json --quality showcase --json
   ```
   *Requirement*: 9/9 checks passed, 0 errors, 0 warnings.
3. **Deliver HTML**:
   ```bash
   node <archify-path>/bin/archify.mjs deliver architecture day-XX/architecture.json day-XX/architecture.html --quality showcase --json
   ```
4. **Generate PNG**:
   Capture a 1760×820 screenshot of `architecture.html` using headless Chrome or puppeteer and save to `day-XX/diagram.png`.

---

## ✍️ LinkedIn Humanizer & Formatting Rules (Strict)

### 🚨 Hard Formatting Constraints (Zero Tolerance)
- **ZERO MARKDOWN BACKTICKS (`)**: LinkedIn's post editor does NOT render markdown backticks. If you include `` `npm create vite` ``, it prints literal backticks and looks broken. Never use backticks in the post text.
- **DOUBLE LINE BREAKS (`\n\n`)**: Always place an empty line between every sentence or numbered point. Single line breaks collapse into an unreadable gray wall on mobile LinkedIn.
- **ZERO AI EMOJI CLUSTERS**: MagicPost 2026 data shows `🚀`, `💡`, `✨` appear 2–3x more often in AI slop than human posts. Use clean, functional indicators (e.g. `1.`, `2.`, `•`, `→`, or occasional `🤦‍♂️`, `⚡`) instead of emoji spam.
- **NO BANNED AI CLICHÉS**: Scrub words like `game-changer`, `delve`, `leverage`, `tapestry`, `realm`, `journey`, `foster`, `robust`, `streamline`, `in today's fast-paced world`, or `I am thrilled to share`.

### 📈 Structural Heuristics (2026 Feed Multipliers)
1. **The Hook (First 210 Characters)**:
   - Line 1 must be a statement or an odd-precision number (e.g., *"Day 1 of learning React: 3 vanilla JavaScript mental models that collapsed in my first 45 minutes."* → **+34% median likes**).
   - **NEVER OPEN WITH A QUESTION**: Opening with a rhetorical question is penalized by **-34%**.
2. **Relatable Friction**:
   - Include real beginner friction (e.g., *"Spent 15 minutes debugging why `<button>` didn't run my component before learning components require PascalCase"*).
3. **Closing Operational Question**:
   - End with a targeted technical question for senior engineers (+3% reach lift).
4. **P.S. Sign-off**:
   - Include a 1-line P.S. noting the visual asset (+7.5% reach lift).
5. **Hashtags**:
   - 2 to 3 relevant hashtags maximum (`#reactjs #webdev`).

---

## 📁 Repository Organization
Every day must be archived inside its own directory:
```text
REACT_BuildInPublic/
├── README.md               <-- Main progress table
├── AGENTS.md               <-- This file
├── .env.example            <-- Environment template
└── day-XX/
    ├── post.md             <-- Final post text + screenshot guide
    ├── architecture.json   <-- Archify input specification
    ├── architecture.html   <-- Standalone interactive diagram viewer
    └── diagram.png         <-- High-res diagram to attach on LinkedIn
```

---

## 🔒 Safety Invariant
**NEVER execute `git commit` or `git push` autonomously.** All git version control commits must be performed manually by the human repository owner.
