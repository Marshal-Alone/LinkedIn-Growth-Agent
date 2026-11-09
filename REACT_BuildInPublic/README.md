# 🚀 React Build-in-Public System

> An agentic daily publishing engine that turns raw technical learning notes into high-converting, humanized LinkedIn posts, paired with production-ready **Archify** architecture diagrams and authentic developer screenshot recipes.

[![React](https://img.shields.io/badge/React-18%2B-blue?logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Bundler-Vite-646CFF?logo=vite)](https://vitejs.dev/)
[![Archify](https://img.shields.io/badge/Diagrams-Archify_2.17-black)](https://github.com/tt-a1i/archify)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 💡 Why This Exists

Documenting your coding journey in public ("Building in Public") is one of the highest-leverage career moves an engineer can make. However, **90% of developer posts fail to get traction because:**

1. **Broken LinkedIn Formatting**: LinkedIn does not render Markdown. Using backticks (`` `code` ``) makes your post look unformatted and amateur.
2. **The "Gray Wall of Text"**: LinkedIn’s mobile app collapses single line breaks into dense, unreadable paragraphs.
3. **Robotic AI Tone**: Generic AI prompts generate clichés (*"game-changer"*, *"delve"*, *"leverage"*, *"in today's fast-paced world"*) and spammy emoji clusters (`🚀`, `💡`, `✨`) that trigger audience fatigue.
4. **No Visual Proof**: Text-only claims get scrolled past. Real engineers value architecture diagrams, terminal logs, and DevTools inspections.

This repository provides a **battle-tested, agent-automated system** to solve all four problems every single day.

---

## 🏗️ How It Works

```
  ┌─────────────────────────────────────────────────────────────┐
  │ 1. Developer Learns & Takes Raw Notes                       │
  │    "Learned Vite, index.html root div, and <></> Fragments" │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 2. AI Coding Agent (Reads AGENTS.md & LinkedIn Skills)       │
  │    • Applies 2026 Hook Formula (Number-first, statement)    │
  │    • Enforces Zero-Backticks & Double-Spaced Mobile Layout  │
  │    • Generates 4-Scene Developer Proof Screenshot Recipes   │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 3. Archify Diagram Engine                                   │
  │    • Validates candidate JSON against showcase profile      │
  │    • Compiles standalone interactive HTML (architecture.html)│
  │    • Exports high-res diagram image (diagram.png)           │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 4. Ready-to-Publish Daily Bundle (day-XX/)                  │
  │    • post.md (Copy/paste text + screenshot directions)      │
  │    • diagram.png (Direct LinkedIn image attachment)         │
  └─────────────────────────────────────────────────────────────┘
```

---

## 📂 Repository Structure

```text
REACT_BuildInPublic/
├── README.md               # Overview, quickstart & daily progress tracker
├── AGENTS.md               # Operating instructions for AI assistants & pair programmers
├── .env.example            # Environment variables template
└── day-01/
    ├── post.md             # Verified LinkedIn post draft & screenshot guide
    ├── architecture.html   # Standalone interactive SVG viewer (Archify 2.17)
    ├── architecture.json   # Archify JSON specification
    └── diagram.png         # High-resolution PNG diagram (1760x820)
```

---

## 📅 Daily Journey Tracker

| Day | Core Milestone | Key Technical Concepts | Artifacts |
|---|---|---|---|
| **Day 01** | **Vite & Mounting Tree** | Vite sub-300ms boot, `#root` DOM entry, PascalCase naming, `<> ... </>` Fragments | [day-01/post.md](day-01/post.md) · [Diagram](day-01/diagram.png) |
| **Day 02** | *Upcoming* | JSX syntax rules, attributes (`className`), event handlers | *In progress* |
| **Day 03** | *Upcoming* | Props, component reusability, unidirectional data flow | *In progress* |
| **Day 04** | *Upcoming* | `useState` hook, re-renders, state immutability | *In progress* |
| **Day 05** | *Upcoming* | Controlled form inputs & lifting state up | *In progress* |

---

## ⚡ Quickstart

### Prerequisites
- [Node.js](https://nodejs.org/) v18.0.0 or higher
- An AI coding environment ([Antigravity](https://antigravity.google.com/), [Claude Code](https://claude.ai/), [Cursor](https://www.cursor.com/), [Windsurf](https://codeium.com/windsurf), or [Cline](https://github.com/cline/cline))

### 1. Setup Your Environment
```bash
# Clone the repository
git clone https://github.com/your-username/REACT_BuildInPublic.git
cd REACT_BuildInPublic

# Copy environment variables
cp .env.example .env
```

### 2. Scaffold Your Practice React App
```bash
npm create vite@latest react-learning-app -- --template react
cd react-learning-app
npm install
npm run dev
```

---

## 🎨 Setting Up the Archify Diagram Skill

This repository uses **Archify** to generate verified architecture, sequence, and workflow diagrams.

### Installing Archify for Your AI Agent
If your AI assistant does not have the Archify skill installed globally, install it using the skills CLI:

```bash
# Install via Skills CLI
npx skills add https://github.com/tt-a1i/archify

# Or clone directly into your agent skills path:
git clone https://github.com/tt-a1i/archify.git ~/.gemini/config/skills/archify
cd ~/.gemini/config/skills/archify && npm install
```

### Compiling Diagrams
```bash
# 1. Validate the candidate JSON (must pass 9/9 checks with 0 errors)
node <archify-path>/bin/archify.mjs validate architecture day-01/architecture.json --quality showcase --json

# 2. Deliver the standalone HTML viewer
node <archify-path>/bin/archify.mjs deliver architecture day-01/architecture.json day-01/architecture.html --quality showcase --json

# 3. Capture PNG for LinkedIn attachment (via headless browser or screenshot tool)
```

---

## ✍️ LinkedIn Publishing Guidelines (2026 Feed Standards)

When drafting posts, always adhere to these rules (codified in [`AGENTS.md`](AGENTS.md)):

* **Zero Backticks**: Never use `` `inline code` `` inside post text. Format commands on their own plain lines or use clean quotes.
* **Double Line Breaks**: Every single idea or bullet point must have an empty line (`\n\n`) beneath it.
* **Number-First Hook**: Open with an odd-precision count or concrete statement within the first 210 characters (*+34% median likes*). **Never open with a question** (*-34% penalty*).
* **Genuine Developer Friction**: Mention what tripped you up, what took 15 minutes to debug, or what surprised you.
* **Closing Operational Question**: End with a direct technical question inviting experienced engineers to comment (*+3% reach*).
* **Actionable P.S.**: Include a one-line P.S. referencing the architecture diagram (*+7.5% lift*).

---

## 📸 The 4-Scene Screenshot Formula

Accompany every daily post with real developer screenshots instead of generic graphics:
1. **Terminal Velocity**: Clean terminal showing rapid boot time (`ready in 280 ms`) framed with [Ray.so](https://ray.so) or [Carbon](https://carbon.now.sh).
2. **File Explorer**: Minimal tree showing folder layout and key entry files.
3. **Code Highlight**: A 10–15 line snippet highlighting the day's core concept (e.g. PascalCase component return).
4. **DevTools DOM**: Browser split-view showing the rendered DOM without unnecessary wrapper `<div>`s.

---

## 🤝 Contributing

Contributions, feedback, and discussion are welcome! If you have suggestions for hook formulas, Archify diagram presets, or new React milestones, feel free to open an Issue or Pull Request.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
