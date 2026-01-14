# -*- coding: utf-8 -*-
"""
Complete notebook check - view and validate the entire demo cell.
"""

import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

NB_PATH = Path(__file__).parent / "epi_investor_demo.ipynb"

with open(NB_PATH, 'r', encoding='utf-8') as f:
    nb = json.load(f)

print("=" * 80)
print("FULL NOTEBOOK CHECK")
print("=" * 80)

# Show all cells
print(f"\nTotal cells: {len(nb['cells'])}")
for i, cell in enumerate(nb['cells']):
    cell_type = cell.get('cell_type', 'unknown')
    cell_id = cell.get('metadata', {}).get('id', 'no-id')
    if cell_type == 'code':
        src_preview = ''.join(cell['source'])[:50].replace('\n', ' ')
        print(f"  [{i}] {cell_type:8} id={cell_id:15} : {src_preview}...")
    else:
        src_preview = ''.join(cell['source'])[:50].replace('\n', ' ')
        print(f"  [{i}] {cell_type:8} id={cell_id:15} : {src_preview}...")

# Get demo cell
demo_cell = None
for cell in nb['cells']:
    if cell.get('metadata', {}).get('id') == 'demo':
        demo_cell = cell
        break

if not demo_cell:
    print("\n[ERROR] Demo cell not found!")
    sys.exit(1)

print("\n" + "=" * 80)
print("DEMO CELL FULL SOURCE CODE:")
print("=" * 80)

src = ''.join(demo_cell['source'])
print(src)

print("\n" + "=" * 80)
print("VALIDATION CHECKS:")
print("=" * 80)

errors = []
warnings = []

# Check 1: Agent code uses triple quotes
if '"""' in src or "'''" in src:
    print("[OK] Agent code uses triple-quoted strings")
else:
    errors.append("Agent code does not use triple-quoted strings")

# Check 2: No problematic escape sequences
lines = src.split('\n')
for i, line in enumerate(lines):
    # Check for broken escape sequences (like unmatched quotes after \n)
    if '\\n"' in line and line.count('"') % 2 != 0:
        errors.append(f"Line {i+1}: Possible broken escape sequence")
    if "\\n'" in line and line.count("'") % 2 != 0:
        errors.append(f"Line {i+1}: Possible broken escape sequence")

if not any("broken escape" in e for e in errors):
    print("[OK] No broken escape sequences detected")

# Check 3: imports at top
if 'import sys, time, re' in src:
    print("[OK] Required imports present")
else:
    warnings.append("Check imports - may be missing 're' module")

# Check 4: Agent code structure
if 'agent_code = """' in src or "agent_code = '''" in src:
    print("[OK] Agent code variable properly defined")
else:
    errors.append("Agent code variable not found or improperly defined")

# Check 5: Signature injection
if 're.sub(pattern, replacement' in src:
    print("[OK] Signature injection regex present")
else:
    errors.append("Signature injection missing")

# Check 6: Dual download
if src.count('files.download(') >= 2:
    print("[OK] Dual download calls present")
else:
    errors.append("Missing dual download calls")

# Check 7: json module alias (since json is also used in agent)
if 'json_mod' in src or 'import json as' in src:
    print("[OK] JSON module properly aliased")
else:
    warnings.append("JSON module may conflict with agent code")

print("\n" + "=" * 80)
print("RESULTS:")
print("=" * 80)

if errors:
    print(f"\n[ERRORS] {len(errors)}:")
    for e in errors:
        print(f"  X {e}")
else:
    print("\n[OK] NO ERRORS FOUND")

if warnings:
    print(f"\n[WARNINGS] {len(warnings)}:")
    for w in warnings:
        print(f"  ! {w}")

print("\n" + "=" * 80)
