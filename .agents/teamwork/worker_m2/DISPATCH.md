## 2026-11-09T10:51:31Z
You are Worker agent for Milestone 2: Author LinkedIn Post and Screenshot Guide.
Identity: teamwork_worker
Your working directory: c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\worker_m2\
Mandatory read first: c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\ORIGINAL_REQUEST.md

Write Ownership:
You exclusively own `c:\Users\marsh\OneDrive\Desktop\LinkedIN\REACT_BuildInPublic\day-01\post.md` (and files inside your own working directory). You MUST NOT write to any other project files.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Context and Inputs:
- Read `c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\orchestrator\PROJECT.md`
- Read `c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\explorer_survey_2_gen2\handoff.md`
- Read `c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\explorer_survey_3\handoff.md`
- LinkedIn skills in `c:\Users\marsh\OneDrive\Desktop\LinkedIN\LinkedIn Agent (2)\skills\`:
  - `linkedin-post-writer`
  - `linkedin-hook-extractor`
  - `linkedin-humanizer`

Objective:
Author the complete Day 1 build-in-public package in `c:\Users\marsh\OneDrive\Desktop\LinkedIN\REACT_BuildInPublic\day-01\post.md`.

Requirements:
1. Day 1 LinkedIn Post Content:
   - Covers all 7 core concepts: Node.js runtime prerequisite, `npm create vite@latest` vs CRA (<300ms dev server boot), index.html root div (`<div id="root">`), top-level App component, components as functions, PascalCase naming convention vs lowercase HTML tags, and returning multiple elements using JSX fragments (`<> ... </>`) to eliminate "div soup".
   - Opening Hook: Apply formula F3 / F7 (number-first, timeline anchor). Never open with a question.
   - Closing: Experience-anchored open question for senior developers + high-converting P.S. note referencing the Archify architecture diagram.
   - Hashtags: Exactly 2 relevant hashtags at the very bottom (`#reactjs #webdev`).
2. Strict Formatting and Tone Constraints:
   - ZERO Markdown backticks (`) anywhere in the post body. Use plain text, quotes, or bracket syntax without backticks.
   - Clear double line breaks (`\n\n`) between every single thought, list item, and paragraph so the text never collapses on mobile.
   - Authentic, relatable, conversational human tone. Avoid corporate AI buzzwords (e.g. leverage, crucial, comprehensive, robust, landscape), avoid reveal bridges ("The result?", "Plot twist:"), avoid negative parallelism ("It's not X, it's Y"), avoid staccato stacks ("Short. Punchy. Done.").
3. Screenshot Recommendations:
   - Provide clear, actionable recommendations for 4 distinct screenshots:
     1. Terminal Setup: `npm create vite@latest`, Vite ready in ~280ms.
     2. Project File Tree: Minimalist structure showing `index.html` at root, `src/main.jsx`, `src/App.jsx`.
     3. Code Snippet: PascalCase functional component returning `<>` and `</>` React Fragments.
     4. Rendered Browser & DevTools: Chrome DevTools `#root` inspection proving zero extra phantom wrapper divs.
   - For each screenshot, provide: scene description, exact content to display, suggested framing (theme, padding, tools like Ray.so/Carbon), and narrative rationale.
4. Constraint: DO NOT run git commit or git push.

Output:
Write `c:\Users\marsh\OneDrive\Desktop\LinkedIN\REACT_BuildInPublic\day-01\post.md`.
Write `handoff.md` in `c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\worker_m2\handoff.md` documenting your implementation, verification checks (including regex verification of 0 backticks), and status. Send a message to parent when done.
