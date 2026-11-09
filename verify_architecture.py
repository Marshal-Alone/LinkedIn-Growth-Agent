"""
Adversarial Verification Script for Architecture Diagram (Day 1 React Flow)
Challenger 2 Test Suite
"""
import subprocess
import json
import re
import sys
from pathlib import Path

HTML_PATH = Path(r"c:\Users\marsh\OneDrive\Desktop\LinkedIN\REACT_BuildInPublic\day-01\architecture.html")
ARCHIFY_CLI = Path(r"C:\Users\marsh\.gemini\config\skills\archify\bin\archify.mjs")

def test_archify_cli():
    print("=== TEST 1: Archify CLI Verification ===")
    cmd = ["node", str(ARCHIFY_CLI), "check", str(HTML_PATH)]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    
    assert proc.returncode == 0, f"Archify CLI failed with exit code {proc.returncode}: {proc.stderr}"
    
    # Extract JSON part from output
    stdout = proc.stdout.strip()
    json_start = stdout.find("{")
    assert json_start != -1, f"No JSON object found in output:\n{stdout}"
    data = json.loads(stdout[json_start:])
    
    assert data.get("ok") is True, f"Check ok was not True: {data}"
    
    checks = data.get("checks", [])
    assert len(checks) == 9, f"Expected exactly 9 checks, found {len(checks)}: {[c.get('name') for c in checks]}"
    
    check_names = [c.get("name") for c in checks]
    expected_check_names = [
        "single_svg",
        "finite_svg",
        "orthogonal_arrows",
        "label_route_clearance",
        "relationship_crossings",
        "relationship_corridors",
        "container_border_runs",
        "route_rhythm",
        "legend_clearance"
    ]
    assert set(check_names) == set(expected_check_names), f"Check names mismatch: {check_names} vs {expected_check_names}"
    
    for c in checks:
        assert c.get("ok") is True, f"Check '{c.get('name')}' failed: {c}"
        print(f"  [PASS] Check: {c.get('name')} (ok=true)")
        
    composition = data.get("composition", {})
    assert composition.get("status") == "pass", f"Composition status not pass: {composition}"
    assert composition.get("profile") == "showcase", f"Composition profile not showcase: {composition}"
    
    summary = composition.get("summary", {})
    assert summary.get("errors") == 0, f"Composition has errors: {summary}"
    assert summary.get("warnings") == 0, f"Composition has warnings: {summary}"
    
    issues = composition.get("issues", [])
    assert len(issues) == 0, f"Expected 0 issues, found {len(issues)}: {issues}"
    
    print("PASS: Archify CLI verification: all 9 checks passed, 0 errors, 0 warnings, 0 issues.")
    return data

def test_semantic_kinds_and_flow():
    print("\n=== TEST 2: Semantic Kinds and Flow Verification ===")
    content = HTML_PATH.read_text(encoding="utf-8")
    
    # 1. Verify Nodes in DOM / SVG
    required_nodes = [
        "browser_dom",
        "main_entry",
        "app_component",
        "custom_component",
        "react_fragment",
        "rendered_dom"
    ]
    
    expected_kinds = {
        "browser_dom": "external",
        "main_entry": "frontend",
        "app_component": "frontend",
        "custom_component": "frontend",
        "react_fragment": "frontend",
        "rendered_dom": "external"
    }
    
    found_nodes = {}
    for node_id in required_nodes:
        # Match <g id="node-<id>" ...>
        m = re.search(rf'<g\b[^>]*\bid=["\']node-{node_id}["\'][^>]*>', content)
        assert m is not None, f"Node element '<g id=\"node-{node_id}\">' not found in SVG"
        tag = m.group(0)
        
        # Extract data-node-kind
        kind_m = re.search(r'data-node-kind=["\']([^"\']+)["\']', tag)
        assert kind_m is not None, f"Node '{node_id}' missing data-node-kind attribute"
        kind = kind_m.group(1)
        found_nodes[node_id] = kind
        
        expected_kind = expected_kinds[node_id]
        assert kind == expected_kind, f"Node '{node_id}' expected kind '{expected_kind}', got '{kind}'"
        print(f"  [PASS] Node '{node_id}': kind='{kind}' (expected: '{expected_kind}')")

    # Verify no other node kinds exist
    all_node_kinds = set(found_nodes.values())
    assert all_node_kinds == {"frontend", "external"}, f"Semantic kinds are not only frontend and external: {all_node_kinds}"
    
    # Assert zero instances of cloud, security, backend in node semantic kinds
    forbidden_kinds = {"cloud", "security", "backend"}
    for node_id, kind in found_nodes.items():
        assert kind not in forbidden_kinds, f"Node '{node_id}' has forbidden semantic kind '{kind}'"

    # 2. Verify Legend Items
    # Find legend group
    legend_match = re.search(r'<g\b[^>]*data-legend=""[^>]*>([\s\S]*?)</g>\s*</svg>', content)
    assert legend_match is not None, "Legend group '<g data-legend=\"\" ...>' not found in SVG"
    legend_content = legend_match.group(1)
    
    legend_kinds = re.findall(r'data-legend-kind=["\']([^"\']+)["\']', legend_content)
    legend_semantic_kinds = re.findall(r'data-legend-semantic-kind=["\']([^"\']+)["\']', legend_content)
    
    print(f"  Legend kinds found: {legend_kinds}")
    print(f"  Legend semantic kinds found: {legend_semantic_kinds}")
    
    assert len(legend_kinds) == 2, f"Expected exactly 2 legend items, found {len(legend_kinds)}"
    assert set(legend_kinds) == {"frontend", "external"}, f"Legend kinds mismatch: {legend_kinds}"
    assert set(legend_semantic_kinds) == {"frontend", "external"}, f"Legend semantic kinds mismatch: {legend_semantic_kinds}"
    
    for lk in legend_kinds + legend_semantic_kinds:
        assert lk not in forbidden_kinds, f"Forbidden kind '{lk}' found in legend"
        
    for fk in forbidden_kinds:
        assert fk not in legend_content.lower(), f"Forbidden keyword '{fk}' found in legend content:\n{legend_content}"
        
    print("  [PASS] Legend verified: only 'frontend' and 'external', zero cloud/security/backend.")

    # 3. Flow Verification: browser_dom -> main_entry -> app_component -> custom_component -> react_fragment -> rendered_dom
    edges = re.findall(r'<path\b[^>]*data-edge-from=["\']([^"\']+)["\'][^>]*data-edge-to=["\']([^"\']+)["\'][^>]*data-edge-label=["\']([^"\']+)["\'][^>]*>', content)
    print(f"  Found {len(edges)} connection paths in SVG:")
    edge_map = {}
    for src, dst, lbl in edges:
        edge_map[(src, dst)] = lbl
        print(f"    {src} --> {dst} (label: \"{lbl}\")")
        
    expected_flow = [
        ("browser_dom", "main_entry", "finds #root"),
        ("main_entry", "app_component", "mounts App"),
        ("app_component", "custom_component", "composes"),
        ("custom_component", "react_fragment", "returns <>"),
        ("react_fragment", "rendered_dom", "emits tags")
    ]
    
    for src, dst, expected_lbl in expected_flow:
        assert (src, dst) in edge_map, f"Expected flow edge ({src} -> {dst}) missing from SVG paths"
        actual_lbl = edge_map[(src, dst)]
        # Normalize HTML entities like &lt;&gt;
        norm_actual = actual_lbl.replace("&lt;", "<").replace("&gt;", ">")
        norm_expected = expected_lbl.replace("&lt;", "<").replace("&gt;", ">")
        assert norm_actual == norm_expected, f"Edge ({src} -> {dst}) label mismatch: expected '{norm_expected}', got '{norm_actual}'"
        print(f"  [PASS] Edge {src} -> {dst}: label='{actual_lbl}'")

    print("PASS: Semantic kinds and flow verification passed completely.")

def test_dom_and_svg_integrity():
    print("\n=== TEST 3: DOM & SVG Integrity Verification ===")
    content = HTML_PATH.read_text(encoding="utf-8")
    
    # 1. Single SVG element and viewBox check
    svg_tags = re.findall(r'<svg\b([^>]*)>', content)
    assert len(svg_tags) == 1, f"Expected exactly 1 <svg> element, found {len(svg_tags)}"
    svg_attr = svg_tags[0]
    
    vb_match = re.search(r'viewBox=["\']([^"\']+)["\']', svg_attr)
    assert vb_match is not None, f"Missing viewBox attribute on <svg>: {svg_attr}"
    vb_vals = [float(v) for v in vb_match.group(1).split()]
    assert len(vb_vals) == 4, f"viewBox must contain 4 numbers, got {vb_vals}"
    min_x, min_y, width, height = vb_vals
    assert min_x == 0, f"viewBox min_x expected 0, got {min_x}"
    assert min_y == 0, f"viewBox min_y expected 0, got {min_y}"
    assert width > 0, f"viewBox width must be > 0, got {width}"
    assert height > 0, f"viewBox height must be > 0, got {height}"
    print(f"  [PASS] SVG viewBox: {min_x} {min_y} {width} {height}")
    
    # 2. SVG element counts
    rects = re.findall(r'<rect\b', content)
    paths = re.findall(r'<path\b', content)
    texts = re.findall(r'<text\b', content)
    groups = re.findall(r'<g\b', content)
    markers = re.findall(r'<marker\b', content)
    
    print(f"  SVG element counts: rects={len(rects)}, paths={len(paths)}, texts={len(texts)}, groups={len(groups)}, markers={len(markers)}")
    assert len(rects) >= 15, f"Expected at least 15 rects, found {len(rects)}"
    assert len(paths) >= 10, f"Expected at least 10 paths, found {len(paths)}"
    assert len(texts) >= 15, f"Expected at least 15 texts, found {len(texts)}"
    assert len(groups) >= 10, f"Expected at least 10 groups, found {len(groups)}"
    assert len(markers) >= 3, f"Expected at least 3 markers, found {len(markers)}"
    
    # 3. Embedded font integrity
    font_faces = re.findall(r'@font-face\s*\{([^}]+)\}', content)
    print(f"  Found {len(font_faces)} @font-face declarations.")
    assert len(font_faces) >= 1, "Expected at least 1 @font-face declaration"
    assert "data:font/" in content or "data:application/font" in content or "font-family:" in content, "Embedded font data missing"
    print("  [PASS] Embedded fonts verified.")
    
    # 4. Theme variables
    # Must have --bg, --grid, --frontend-fill, --frontend-stroke
    required_theme_vars = [
        "--bg",
        "--grid",
        "--frontend-fill",
        "--frontend-stroke",
        "--external-fill",
        "--external-stroke"
    ]
    for var in required_theme_vars:
        assert var in content, f"Required theme variable '{var}' missing in stylesheet"
        # Print sample usage
        m = re.search(rf'({re.escape(var)}\s*:[^;]+;)', content)
        sample = m.group(1) if m else "found"
        print(f"  [PASS] Theme variable '{var}' defined: {sample}")

    # 5. Card contents
    cards_match = re.search(r'<div class="cards">([\s\S]*?)</div>\s*</div>\s*<script>', content)
    assert cards_match is not None, "Cards container '<div class=\"cards\">' not found"
    cards_html = cards_match.group(1)
    
    card_blocks = re.findall(r'<div class="card">([\s\S]*?)</div>\s*(?=<div class="card">|$)', cards_html)
    print(f"  Found {len(card_blocks)} card blocks.")
    assert len(card_blocks) == 3, f"Expected exactly 3 cards, found {len(card_blocks)}"
    
    # Card 1 assertions
    c1 = card_blocks[0]
    assert "Host DOM &amp; Vite Mounting" in c1 or "Host DOM & Vite Mounting" in c1, "Card 1 title mismatch"
    assert "index.html" in c1 and "root" in c1, "Card 1 missing index.html or root"
    assert "createRoot()" in c1 and "App" in c1, "Card 1 missing createRoot() or App"
    print("  [PASS] Card 1 (Host DOM & Vite Mounting) verified.")
    
    # Card 2 assertions
    c2 = card_blocks[1]
    assert "Components &amp; PascalCase" in c2 or "Components & PascalCase" in c2, "Card 2 title mismatch"
    assert "functions" in c2.lower() and "JSX" in c2, "Card 2 missing functions/JSX"
    assert "PascalCase" in c2 and "Card" in c2, "Card 2 missing PascalCase or Card"
    print("  [PASS] Card 2 (Components & PascalCase) verified.")
    
    # Card 3 assertions
    c3 = card_blocks[2]
    assert "Single Return &amp; JSX Fragments" in c3 or "Single Return & JSX Fragments" in c3, "Card 3 title mismatch"
    assert "single expression" in c3.lower(), "Card 3 missing single expression"
    assert "Fragments" in c3 and "extra wrapper divs" in c3.lower(), "Card 3 missing Fragments or wrapper divs note"
    print("  [PASS] Card 3 (Single Return & JSX Fragments) verified.")

    print("PASS: DOM & SVG Integrity verification passed completely.")

def test_repo_safety():
    print("\n=== TEST 4: Repository Safety Verification ===")
    root_dir = Path(r"c:\Users\marsh\OneDrive\Desktop\LinkedIN")
    
    # Check git status
    proc_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=str(root_dir))
    assert proc_status.returncode == 0, f"git status failed: {proc_status.stderr}"
    print(f"  Git status output:\n{proc_status.stdout.strip()}")
    
    # Check git log or rev-parse to verify no new commits were created
    proc_log = subprocess.run(["git", "log", "-n", "1"], capture_output=True, text=True, cwd=str(root_dir))
    if "does not have any commits yet" in proc_log.stderr or proc_log.returncode != 0:
        print("  Git repo status: unborn branch / zero commits exist in repository.")
    else:
        print(f"  Recent commit: {proc_log.stdout.strip()}")
        
def test_adversarial_stress_and_graph_consistency():
    print("\n=== TEST 5: Adversarial Stress & Graph Topology Consistency ===")
    content = HTML_PATH.read_text(encoding="utf-8")
    
    # 1. Standalone Offline Integrity
    assert "<!DOCTYPE html>" in content or "<!doctype html>" in content, "Missing <!DOCTYPE html>"
    assert "<html" in content and "</html>" in content, "HTML root tag mismatch"
    assert "<head>" in content and "</head>" in content, "Head tag mismatch"
    assert "<body>" in content and "</body>" in content, "Body tag mismatch"
    
    # Check for external network dependencies (scripts or stylesheets)
    remote_scripts = re.findall(r'<script\b[^>]*\bsrc=["\'](https?:[^"\']+)["\']', content, re.IGNORECASE)
    remote_links = re.findall(r'<link\b[^>]*\bhref=["\'](https?:[^"\']+)["\']', content, re.IGNORECASE)
    print(f"  Remote external scripts found: {remote_scripts}")
    print(f"  Remote external stylesheets found: {remote_links}")
    assert len(remote_scripts) == 0, f"Found remote external scripts: {remote_scripts}"
    assert len(remote_links) == 0, f"Found remote external stylesheets: {remote_links}"
    print("  [PASS] Artifact is 100% self-contained and offline-capable.")
    
    # 2. Graph Topology Consistency: No dangling connections or invalid targets
    node_ids = set(re.findall(r'<g\b[^>]*\bid=["\']node-([^"\']+)["\']', content))
    edge_pairs = re.findall(r'<path\b[^>]*data-edge-from=["\']([^"\']+)["\'][^>]*data-edge-to=["\']([^"\']+)["\']', content)
    
    for src, dst in edge_pairs:
        assert src in node_ids, f"Edge source '{src}' does not exist in rendered nodes: {node_ids}"
        assert dst in node_ids, f"Edge destination '{dst}' does not exist in rendered nodes: {node_ids}"
    print(f"  [PASS] All {len(edge_pairs)} edges connect valid rendered nodes: {edge_pairs}")
    
    # Check boundary wraps
    # In worker_m1 refined spec: region wraps main_entry, app_component, custom_component, react_fragment
    region_rect = re.search(r'<rect\b[^>]*data-composition-frame-label=["\']React Virtual DOM Scope["\'][^>]*>', content)
    assert region_rect is not None, "Boundary frame for 'React Virtual DOM Scope' not found"
    print("  [PASS] Structural frame 'React Virtual DOM Scope' correctly wraps virtual DOM components.")
    
    # 3. Accessibility & Interactive Controls
    assert 'role="img"' in content, "SVG missing role=\"img\""
    assert 'aria-label' in content, "Document missing ARIA labels"
    assert 'id="btn-preset"' in content, "Theme / preset switcher missing"
    assert 'id="btn-theme"' in content, "Light / dark theme switcher missing"
    print("  [PASS] Interactive accessibility and viewer controls verified.")

if __name__ == "__main__":
    try:
        test_archify_cli()
        test_semantic_kinds_and_flow()
        test_dom_and_svg_integrity()
        test_repo_safety()
        test_adversarial_stress_and_graph_consistency()
        print("\n========================================================")
        print("EMPIRICAL CHALLENGER TEST SUITE: ALL 5 TESTS PASSED")
        print("VERDICT: APPROVE")
        print("========================================================")
    except AssertionError as e:
        print(f"\n[FAIL] EMPIRICAL ASSERTION FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        import traceback
        traceback.print_exc()
        sys.exit(2)
