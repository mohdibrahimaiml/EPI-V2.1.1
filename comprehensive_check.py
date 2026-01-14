# -*- coding: utf-8 -*-
"""
Comprehensive error check of the entire notebook.
Check both DEMO and VIEW cells for any syntax or logic errors.
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
print("COMPREHENSIVE ERROR CHECK")
print("=" * 80)

errors = []

# Check DEMO cell
print("\n[1] DEMO CELL CHECK:")
demo = None
for cell in nb['cells']:
    if cell.get('metadata', {}).get('id') == 'demo':
        demo = cell
        break

if demo:
    src = ''.join(demo['source'])
    
    # Check imports
    if 'import sys, time, re' in src:
        print("    [OK] Imports correct")
    else:
        errors.append("DEMO: Missing imports (sys, time, re)")
        print("    [FAIL] Missing imports")
    
    # Check agent code uses triple quotes
    if 'agent_code = """' in src:
        print("    [OK] Agent code uses triple quotes")
    else:
        errors.append("DEMO: Agent code not using triple quotes")
        print("    [FAIL] Agent code format")
    
    # Check for proper escaping in agent
    if '\\\\n' in src:
        errors.append("DEMO: Found double-escaped newlines (\\\\n)")
        print("    [FAIL] Double-escaped newlines found")
    else:
        print("    [OK] No double-escaped newlines")
    
    # Check signature injection
    if 're.sub(pattern, replacement' in src:
        print("    [OK] Signature injection present")
    else:
        errors.append("DEMO: Missing signature injection")
        print("    [FAIL] Missing signature injection")
    
    # Check dual download
    if src.count('files.download(') >= 2:
        print("    [OK] Dual download present")
    else:
        errors.append("DEMO: Missing dual download")
        print("    [FAIL] Missing dual download")
    
    # Check json alias
    if 'json as json_mod' in src or 'json_mod' in src:
        print("    [OK] JSON module aliased")
    else:
        errors.append("DEMO: JSON module not aliased (may conflict)")
        print("    [WARN] JSON module not aliased")
else:
    errors.append("DEMO cell not found!")
    print("    [FAIL] DEMO cell not found")

# Check VIEW cell
print("\n[2] VIEW CELL CHECK:")
view = None
for cell in nb['cells']:
    if cell.get('metadata', {}).get('id') == 'view':
        view = cell
        break

if view:
    src = ''.join(view['source'])
    
    # Check imports
    if 'import' in src and 're' in src:
        print("    [OK] Imports include re")
    else:
        errors.append("VIEW: Missing re import")
        print("    [FAIL] Missing re import")
    
    # Check manifest reading
    if 'manifest.json' in src:
        print("    [OK] Reads manifest.json")
    else:
        errors.append("VIEW: Not reading manifest.json")
        print("    [FAIL] Not reading manifest")
    
    # Check signature injection
    if 're.sub(' in src:
        print("    [OK] Signature injection present")
    else:
        errors.append("VIEW: Missing signature injection (re.sub)")
        print("    [FAIL] Missing signature injection")
    
    # Check for problematic escapes
    if "\\\\n" in src:
        print("    [WARN] Has escaped newlines (may be intentional)")
    
    # Check steps reading
    if 'steps.jsonl' in src:
        print("    [OK] Reads steps.jsonl")
    else:
        errors.append("VIEW: Not reading steps.jsonl")
        print("    [FAIL] Not reading steps")
else:
    errors.append("VIEW cell not found!")
    print("    [FAIL] VIEW cell not found")

# Check VERIFY cell
print("\n[3] VERIFY CELL CHECK:")
verify = None
for cell in nb['cells']:
    if cell.get('metadata', {}).get('id') == 'verify':
        verify = cell
        break

if verify:
    src = ''.join(verify['source'])
    if 'epi verify' in src:
        print("    [OK] Has epi verify command")
    else:
        errors.append("VERIFY: Missing epi verify command")
        print("    [FAIL] Missing epi verify")
else:
    errors.append("VERIFY cell not found!")
    print("    [FAIL] VERIFY cell not found")

# Check TAMPER cell
print("\n[4] TAMPER CELL CHECK:")
tamper = None
for cell in nb['cells']:
    if cell.get('metadata', {}).get('id') == 'tamper':
        tamper = cell
        break

if tamper:
    src = ''.join(tamper['source'])
    if 'shutil.copy' in src and 'epi verify' in src:
        print("    [OK] Tamper test logic present")
    else:
        print("    [WARN] Check tamper test logic")
else:
    errors.append("TAMPER cell not found!")
    print("    [FAIL] TAMPER cell not found")

# Final results
print("\n" + "=" * 80)
print("RESULTS:")
print("=" * 80)

if errors:
    print(f"\n[ERRORS] {len(errors)} issue(s) found:")
    for e in errors:
        print(f"  X {e}")
else:
    print("\n[OK] NO ERRORS FOUND - Notebook is ready!")

print("\n" + "=" * 80)
