# 🤖 Instructions for AI Agents (Antigravity, Claude Code, Cursor, Windsurf, Cline)

> **Welcome AI Assistant**:  
> You are operating inside the **LinkedIn Growth Agent & Build-in-Public Suite**.  
> This workspace contains a full-stack SaaS web application, 12 specialized LinkedIn marketing & humanizer skills, a React build-in-public daily publishing engine, and an automated architecture diagram pipeline using **Archify**.
>
> Read this document carefully before making changes or drafting content.

---

## 🧭 Repository Layout

```text
LinkedIN/
├── README.md               # 🌟 Master repository guide & open-source documentation
├── AGENTS.md               # 🤖 This file: instructions for AI assistants
├── .env.example            # 🔑 Universal environment variables template
├── LinkedIn Agent (2)/     # 💻 Full-Stack SaaS WebApp & LinkedIn Skills Engine
│   ├── server.py           # FastAPI backend (API endpoints, autopilot, scheduler)
│   ├── frontend/           # Modern React + Vite + Tailwind + Lucide SaaS frontend
│   ├── skills/             # 12 LinkedIn skills (post-writer, humanizer, hook-extractor)
│   ├── lib/                # Python publishing clients (Publora, Apify, Pixfaro)
│   └── references/         # 20 2026 hook formulas, founder angles, voice profiles
└── REACT_BuildInPublic/    # 🚀 Daily React learning archive & build-in-public engine
    ├── day-01/             # Day 1: Vite, #root mounting, and React Fragments
    ├── AGENTS.md           # Sub-guide for daily learning workflows
    └── README.md           # Progress tracker table
```

---

## 💻 Running the Full-Stack SaaS WebApp

### Development Mode (Recommended)
1. **Start the FastAPI Backend**:
   ```bash
   cd "LinkedIn Agent (2)"
   python -m uvicorn server:app --host 127.0.0.1 --port 8000 --reload
   ```
2. **Start the React Frontend**:
   ```bash
   cd "LinkedIn Agent (2)/frontend"
   npm install
   npm run dev
   ```
   Open `http://localhost:5173`. API requests to `/api` proxy automatically to port `8000`.

### Production Single-Server Mode
```bash
cd "LinkedIn Agent (2)/frontend"
npm run build
cd ..
python -m uvicorn server:app --host 0.0.0.0 --port 8000
```
Open `http://localhost:8000`. FastAPI serves the compiled frontend assets directly.

---

## 🎨 Archify Architecture Skill: Installation & Authoring Manual

Archify is the diagram engine used to generate interactive SVG architecture maps and high-res diagram images for technical posts.

### 1. How to Check if Archify is Installed
Check common skill directories or PATH:
- Windows: `%USERPROFILE%\.gemini\config\skills\archify\bin\archify.mjs`
- Mac/Linux: `~/.gemini/config/skills/archify/bin/archify.mjs` or `~/.claude/skills/archify/bin/archify.mjs`

Test via CLI:
```bash
node <archify-path>/bin/archify.mjs --help
```

### 2. How to Install Archify (If Not Detected)
Whenever you (the AI agent) detect that Archify is not installed on the user's system, install it using the skills CLI or git:
```bash
# Option A: Via Skills CLI (Recommended)
npx skills add https://github.com/tt-a1i/archify

# Option B: Git Clone into Agent Skills Path
git clone https://github.com/tt-a1i/archify.git ~/.gemini/config/skills/archify
cd ~/.gemini/config/skills/archify && npm install
```

### 3. Diagram Generation Protocol
1. **Author the JSON**: Write a typed candidate specification `<name>.architecture.json`:
   - Set `meta.quality_profile: "showcase"`
   - Set `meta.viewBox: "0 0 1760 820"` (or balanced 16:9)
   - Use standard component kinds (`frontend`, `backend`, `database`, `cloud`, `security`, `messagebus`, `external`)
2. **Validate**:
   ```bash
   node <archify-path>/bin/archify.mjs validate architecture <candidate>.json --quality showcase --json
   ```
   *Rule*: Must report 9/9 checks passed with 0 errors and 0 warnings.
3. **Deliver**:
   ```bash
   node <archify-path>/bin/archify.mjs deliver architecture <candidate>.json <output>.html --quality showcase --json
   ```
4. **PNG Export**:
   Capture a clean screenshot of the delivered HTML at 1760×820 and save as `<name>.png`.

---

## ✍️ LinkedIn Publishing & Humanizer Rules (Strict 2026 Standards)

When drafting or reviewing LinkedIn content, strictly apply the rules from `LinkedIn Agent (2)/skills/linkedin-humanizer/`:

### 🚨 Hard Formatting Constraints (Zero Tolerance)
1. **ZERO MARKDOWN BACKTICKS (`)**:
   LinkedIn's feed editor does NOT render markdown syntax. Backticks (`` `npm run dev` ``) display as literal ugly characters. Never output backticks in post text. Format commands on their own plain lines or use clean single quotes.
2. **DOUBLE LINE BREAKS (`\n\n`)**:
   Always place an empty line between every sentence or bullet point. Single line breaks collapse into an unreadable gray wall on mobile LinkedIn.
3. **ZERO AI EMOJI CLUSTERS**:
   Data proves `🚀`, `💡`, `✨` appear 2–3x more often in synthetic AI text than human writing. Strip them. Use clean, functional indicators (`1.`, `2.`, `•`, `→`) or occasional relatable emojis (`🤦‍♂️`, `⚡`).
4. **NO BANNED AI CLICHÉS**:
   Scrub: `game-changer`, `delve`, `leverage`, `tapestry`, `realm`, `journey`, `foster`, `robust`, `streamline`, `in today's fast-paced world`, `I am thrilled to share`.

### 📈 Structural Heuristics
- **Hook (Under 210 Characters)**: First line must be a number-first statement (+34% median likes). **NEVER open with a question** (-34% reach penalty).
- **Relatable Friction**: Share what actually went wrong, what surprised you, or what took 15 minutes to debug.
- **Closing Question**: End with a technical question for senior engineers (+3% reach lift).
- **P.S. Sign-Off**: Add a 1-line P.S. referencing the visual architecture diagram (+7.5% lift).
- **Hashtags**: 2 to 3 targeted hashtags maximum (`#reactjs #webdev`).

---

## 🚀 Daily Build-in-Public Routine

When the user provides daily learning notes (e.g., *"Here's what I built/learned today: ... "*):
1. Create `REACT_BuildInPublic/day-XX/`.
2. Generate `post.md` (clean text with 0 backticks + 4 screenshot recommendations).
3. Generate `architecture.json`, `architecture.html`, and `diagram.png` using Archify.
4. Update the tracker table in `REACT_BuildInPublic/README.md`.

---

## 🔒 Safety Invariant
**NEVER execute `git commit` or `git push` autonomously.** The human repository owner manages all version control commits.
