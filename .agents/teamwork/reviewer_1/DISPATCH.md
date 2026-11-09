## 2026-11-09T11:00:57Z
You are Reviewer agent for LinkedIn Post & Visuals (Reviewer 1).
Identity: teamwork_reviewer
Your working directory: c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\reviewer_1\
Mandatory read first: c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\ORIGINAL_REQUEST.md

Task:
Review `c:\Users\marsh\OneDrive\Desktop\LinkedIN\REACT_BuildInPublic\day-01\post.md` against all prompt requirements:
1. Formatting Constraints:
   - Verify ZERO Markdown backticks (`) anywhere in the post body and whole file.
   - Verify clear double line breaks (`\n\n`) between every single thought and paragraph so text does not collapse.
2. Tone & 2026 LinkedIn Heuristics:
   - Authentic, conversational human tone.
   - Hook formula (F3/F7, number-first, no opening question, under 140 chars before mobile fold).
   - Zero banned corporate AI buzzwords (e.g. leverage, crucial, landscape, comprehensive, robust).
   - Zero reveal bridges ("The result?", "Plot twist:"), zero negative parallelism ("It's not X, it's Y"), no staccato stacks ("Short. Punchy. Done.").
   - Closing question tailored to senior engineers + high-converting P.S. note referencing the Archify diagram.
   - 0-2 hashtags at the very bottom.
3. Content Coverage:
   - Node.js runtime prerequisite, `npm create vite@latest` vs CRA (<300ms server start), index.html root div `<div id="root">`, createRoot DOM mounting and top-level App component, components as functions, PascalCase naming convention vs lowercase HTML tags, JSX fragments `<> ... </>` eliminating div soup.
4. Screenshot Recommendations:
   - 4 Actionable screenshot scenes (Terminal, Project file tree, Code snippet, Chrome DevTools DOM).
   - Check that each provides scene description, exact content to display, suggested framing (Ray.so, Carbon, dark mode, 14px font), and narrative rationale.
5. Repository Safety:
   - Ensure zero git commit or git push commands are run.

Inspect worker reports: `c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\worker_m2\handoff.md`.
Deliver handoff report with explicit verdict: `APPROVE` or `REQUEST_CHANGES` to `c:\Users\marsh\OneDrive\Desktop\LinkedIN\.agents\teamwork\reviewer_1\handoff.md` and send message to parent.
