# 💼 LinkedIn Growth Agent & Build-in-Public Suite

> A modern, full-stack SaaS platform and agentic AI suite designed to turn raw engineering notes, GitHub commits, and daily learning milestones into high-converting, humanized LinkedIn posts paired with automated **Archify** architecture diagrams.

[![React](https://img.shields.io/badge/Frontend-React_18_%2B_Vite-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Tailwind CSS](https://img.shields.io/badge/Styling-Tailwind_CSS-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Archify](https://img.shields.io/badge/Diagrams-Archify_2.17-black)](https://github.com/tt-a1i/archify)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🌟 What This Platform Does

This repository bridges the gap between **software engineering** and **developer personal branding**. It combines four core systems into a unified workflow:

1. **🖥️ Full-Stack SaaS WebApp**: A modern dark-mode dashboard (inspired by Linear, Raycast, and Stripe) featuring a Post Composer, GitHub Commit Scanner, Live LinkedIn Feed Preview, AI Humanizer, and 1-Click Scheduler.
2. **🧠 12 Agentic LinkedIn Skills**: A battle-tested library of skills for Claude Code, Codex, and Antigravity covering 20 2026 hook formulas (F1–F20), 10 founder angles (A1–A10), and automated AI-slop scrubbing.
3. **🚀 Daily React Build-in-Public Engine**: A structured system (`REACT_BuildInPublic/`) that transforms raw daily study notes into engaging, authentic posts accompanied by actionable developer screenshot recipes.
4. **🎨 Archify Diagram Pipeline**: An automated diagram compiler that generates verified, interactive HTML/SVG architecture maps and high-resolution PNGs ready to attach directly to LinkedIn posts.

---

## 🏗️ System Architecture

```
                                  USER INTERFACES
              ┌────────────────────────────────────────────────────────┐
              │  Modern React + Vite SaaS WebApp (Port 5173 / 8000)    │
              │  • Post Composer Studio       • GitHub Build-Log AI   │
              │  • AI Humanizer & De-AI       • Feed Mockup & Preview │
              │  • Scheduled Queue & Calendar • Story Bank & Voice    │
              └──────────────────────────┬─────────────────────────────┘
                                         │ REST API / Proxied Requests
                                         ▼
                               FASTAPI SERVER (server.py)
              ┌────────────────────────────────────────────────────────┐
              │  • Post Generation Engine      • Publora Bridge        │
              │  • AI De-AI & Scrubbing Audit • Apify Social Scraper  │
              │  • GitHub Commit Inspector    • 24/7 Autopilot Loop   │
              └──────────────┬───────────────────────────┬─────────────┘
                             │                           │
            ┌────────────────┴──────────────┐            │
            ▼                               ▼            ▼
   12 LINKEDIN SKILLS            ARCHIFY DIAGRAMS     DAILY ARCHIVE
   (LinkedIn Agent (2)/skills)   (JSON-IR -> HTML)    (REACT_BuildInPublic/)
   • linkedin-post-writer        • validate schema    • Day 1..30 posts
   • linkedin-humanizer          • showcase quality   • Screenshot guides
   • linkedin-hook-extractor     • interactive SVG    • Archify HTML & PNG
   • linkedin-comment-drafter    • PNG screenshot     • Real DOM proof
```

---

## 🖥️ The Full-Stack SaaS Web Application

The webapp lives in [`LinkedIn Agent (2)/`](file:///C:/Users/marsh/OneDrive/Desktop/LinkedIN/LinkedIn%20Agent%20(2)) and delivers an editorial developer experience:

### Key Features
* **Post Composer Studio**: Pick from 20 hook formulas (Controlled A/B, Obituary, Anaphora, Money Ledger) and 10 Founder Angles. Real-time character counter highlights the 900–1,300 sweet spot.
* **Pixel-Perfect LinkedIn Feed Mockup**: Preview your exact post appearance across mobile and desktop viewports, complete with the 210-character `…see more` fold line and reaction buttons.
* **GitHub Build-Log & DevOps Studio**: Connect your GitHub repository, inspect commits and file diffs, and generate authentic "shipped today" build-in-public posts with full context.
* **AI Humanizer & De-AI Studio**: Live vocabulary scanner highlights blacklisted buzzwords (*"streamline"*, *"leverage"*, *"delve"*, *"foster"*). 1-click auto-scrub removes AI rhythm patterns and normalizes line breaks.
* **Scheduled Queue & Publora Integration**: 1-click scheduling (in 5 minutes, tomorrow at 8:00 AM, or save as draft) with live status tracking and instant cancellation.
* **Smart Comment & Thread Drafter**: Paste any LinkedIn post URL to generate 3 high-signal, non-generic comment variations in the optimal 200–350 character range.

---

## 🚀 Running the WebApp Locally

### Option A: Development Mode (FastAPI + Vite Hot Reload)
1. **Start the FastAPI Backend**:
   ```bash
   cd "LinkedIn Agent (2)"
   python -m uvicorn server:app --host 127.0.0.1 --port 8000 --reload
   ```

2. **Start the Modern React Frontend**:
   ```bash
   cd "LinkedIn Agent (2)/frontend"
   npm install
   npm run dev
   ```
   Open **`http://localhost:5173`** in your browser. All API calls to `/api` proxy automatically to port 8000.

---

### Option B: Production Single-Server Mode (Zero Proxy)
1. **Build the React Frontend**:
   ```bash
   cd "LinkedIn Agent (2)/frontend"
   npm run build
   cd ..
   ```

2. **Launch Single Server**:
   ```bash
   python -m uvicorn server:app --host 0.0.0.0 --port 8000
   ```
   Open **`http://localhost:8000`** in your browser. FastAPI serves the compiled frontend assets directly.

---

### Option C: Docker & Cloud Deployment
```bash
cd "LinkedIn Agent (2)"

# Build and run Docker container
docker build -t linkedin-growth-agent .
docker run -d -p 8000:8000 --env-file .env linkedin-growth-agent
```
Compatible with 1-click deployments on **[Railway.app](https://railway.app)** or **[Render.com](https://render.com)**.

---

## 🧠 The 12 LinkedIn Agent Skills

Located in [`LinkedIn Agent (2)/skills/`](file:///C:/Users/marsh/OneDrive/Desktop/LinkedIN/LinkedIn%20Agent%20(2)/skills), these skills can be run inside Claude Code, Codex, Antigravity, or via the WebApp:

| Skill | Description | Primary Goal |
|---|---|---|
| **`linkedin-post-writer`** | Drafts posts using 20 2026 hook formulas & 10 founder angles | Reach & Engagement |
| **`linkedin-humanizer`** | Scrubs 2026 AI vocabulary, reveal bridges, and staccato fragments | De-AI / Anti-Slop |
| **`linkedin-hook-extractor`** | Reverse-engineers viral post hooks from successful examples | Hook Ideation |
| **`linkedin-content-planner`** | Generates 30-day editorial roadmaps across technical pillars | Strategy & Cadence |
| **`linkedin-comment-drafter`** | Writes high-signal comments in the 200–350 char sweet spot | Profile Visits |
| **`linkedin-profile-optimizer`** | Audits headlines, about sections, and featured media | Profile Conversion |
| **`linkedin-repurposer`** | Converts GitHub commits, articles, or transcripts into posts | Repurposing |
| **`linkedin-interviewer`** | Interviews the user to unearth authentic stories & metrics | Story Extraction |
| **`linkedin-reply-handler`** | Crafts authentic, non-generic replies to incoming comments | Comment Virality |
| **`linkedin-engager-analytics`** | Analyzes engagement patterns, top commenters, and reach | Analytics |
| **`linkedin-employee-advocacy`**| Coordinates company team posts without generic templates | Team Advocacy |
| **`linkedin-thread-monitor`** | Tracks high-performing discussions in your engineering niche | Market Intelligence |

---

## 🎨 Archify Architecture Diagrams (For Humans & AI Agents)

This project integrates the **Archify** skill to automatically generate verified architecture diagrams for technical posts.

### 1. How AI Agents & Humans Install Archify
If Archify is not already installed in your agent's skill environment, install it via the skills CLI:

```bash
# Recommended: Install via Skills CLI
npx skills add https://github.com/tt-a1i/archify

# Alternative: Clone directly to your agent configuration directory
git clone https://github.com/tt-a1i/archify.git ~/.gemini/config/skills/archify
cd ~/.gemini/config/skills/archify && npm install
```

### 2. Diagram Generation Commands
```bash
# 1. Validate the candidate JSON against the showcase quality profile (9/9 checks required)
node <archify-path>/bin/archify.mjs validate architecture candidate.json --quality showcase --json

# 2. Deliver the standalone, responsive HTML viewer
node <archify-path>/bin/archify.mjs deliver architecture candidate.json output.html --quality showcase --json

# 3. Capture high-res PNG (1760x820) for LinkedIn image attachment
```

---

## 🚀 The React Build-in-Public System

Inside [`REACT_BuildInPublic/`](file:///C:/Users/marsh/OneDrive/Desktop/LinkedIN/REACT_BuildInPublic), daily engineering notes are organized into production-ready publication bundles:

```text
REACT_BuildInPublic/
├── README.md               # Daily journey tracker & milestone table
├── AGENTS.md               # Dedicated operating instructions for AI assistants
├── .env.example            # Environment variables template
└── day-01/
    ├── post.md             # Verified post text (zero backticks) & screenshot recipes
    ├── architecture.json   # Archify source specification
    ├── architecture.html   # Standalone interactive SVG viewer
    └── diagram.png         # High-resolution PNG diagram (1760x820)
```

### Strict LinkedIn Formatting Rules (2026 Feed Standards)
* **Zero Markdown Backticks (`)**: LinkedIn does not render Markdown. Backticks display as raw, broken characters. All commands are formatted on plain lines.
* **Double Line Breaks (`\n\n`)**: Every single takeaway is separated by an empty line so it does not collapse into a gray wall on mobile.
* **Number-First Hook**: The first line uses a number-first statement (+34% median likes). Never open with a question (-34% penalty).
* **Genuine Friction**: Documents real beginner mistakes and debugging time rather than synthetic praise.
* **Closing Question & P.S.**: Closes with a technical discussion question (+3%) and a 1-line P.S. referencing the visual diagram (+7.5%).

---

## ⚙️ Environment Variables

Copy [`.env.example`](.env.example) to `.env`:
```bash
cp .env.example .env
```

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Primary LLM engine for post generation & skills reasoning |
| `GROQ_API_KEY` | High-speed inference fallback |
| `PUBLORA_API_KEY` | Connects 1-click publishing to LinkedIn & Bluesky |
| `LINKEDIN_PLATFORM_ID` | Your LinkedIn channel ID inside Publora |
| `APIFY_TOKEN` | Optional token for fetching LinkedIn profiles and post threads |
| `PIXFARO_TOKEN` | Optional token for generating on-brand feed visuals & quote cards |
| `GITHUB_TOKEN` | Personal Access Token to scan repositories and commits |

---

## 🤝 Contributing

Contributions, feature requests, and new hook formulas are welcome! Please open an Issue or submit a PR.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).
