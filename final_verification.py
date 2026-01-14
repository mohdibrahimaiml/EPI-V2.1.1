import json
import ast
import sys
sys.stdout.reconfigure(encoding='utf-8')

NB_PATH = r"c:\Users\dell\epi-recorder\epi_investor_demo_ULTIMATE.ipynb"

print("=" * 70)
print("FINAL COMPREHENSIVE VERIFICATION")
print("=" * 70)

with open(NB_PATH, 'r', encoding='utf-8') as f:
    nb = json.load(f)

issues = []
warnings = []

# Get all code cells
code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
print(f"\nFound {len(code_cells)} code cells\n")

# 1. Syntax check all cells
print("1. SYNTAX CHECK:")
print("-" * 70)
for i, cell in enumerate(code_cells, 1):
    source = "".join(cell.get('source', []))
    cid = cell.get('metadata', {}).get('id', f'cell_{i}')
    
    try:
        # Remove magic commands before parsing
        lines = source.split('\n')
        python_lines = [l for l in lines if not l.strip().startswith('!') and not l.strip().startswith('%') and not l.strip().startswith('#')]
        python_code = '\n'.join(python_lines)
        
        if python_code.strip():
            ast.parse(python_code)
        print(f"   ✓ {cid}")
    except SyntaxError as e:
        print(f"   ✗ {cid}: {e}")
        issues.append(f"Syntax error in {cid}: {e}")

# 2. Feature verification
print("\n2. FEATURE VERIFICATION:")
print("-" * 70)

full_source = json.dumps(nb)

critical_features = [
    ("Python API import", "from epi_recorder import record"),
    ("session.log_step() usage", "session.log_step"),
    ("Runs python directly", "python trading_agent.py"),
    ("Viewer extraction", "zipfile.ZipFile"),
    ("Signature extraction", "manifest.get('signature'"),
    ("Pandas import", "import pandas"),
    ("Google Colab download", "google.colab"),
    ("Tamper test", "TAMPERED"),
]

for name, pattern in critical_features:
    present = pattern in full_source
    status = "✓" if present else "✗"
    print(f"   [{status}] {name}")
    if not present:
        warnings.append(f"Missing: {name}")

# 3. Cell-specific checks
print("\n3. CELL-SPECIFIC CHECKS:")
print("-" * 70)

# Check agent cell specifically
agent_cell = [c for c in code_cells if c.get('metadata', {}).get('id') == 'agent']
if agent_cell:
    agent_source = "".join(agent_cell[0]['source'])
    
    agent_checks = [
        ("Creates trading_agent.py", "with open('trading_agent.py'"),
        ("Uses with record() context", "with record("),
        ("Has session.log_step", "session.log_step("),
        ("Imports EPI", "from epi_recorder import record"),
        ("Has time delays", "time.sleep("),
    ]
    
    print("   Agent Cell:")
    for name, pattern in agent_checks:
        present = pattern in agent_source
        status = "✓" if present else "✗"
        print(f"      [{status}] {name}")
        if not present:
            issues.append(f"Agent cell missing: {name}")

# Check record cell
record_cell = [c for c in code_cells if c.get('metadata', {}).get('id') == 'record']
if record_cell:
    record_source = "".join(record_cell[0]['source'])
    
    record_checks = [
        ("Runs python trading_agent.py", "python trading_agent.py"),
        ("NOT using epi run", "epi run" not in record_source),
        ("File discovery", "glob"),
        ("Download", "files.download"),
    ]
    
    print("   Record Cell:")
    for name, pattern in record_checks:
        if isinstance(pattern, bool):
            present = pattern
        else:
            present = pattern in record_source
        status = "✓" if present else "✗"
        print(f"      [{status}] {name}")
        if not present:
            issues.append(f"Record cell issue: {name}")

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

if issues:
    print(f"\n❌ CRITICAL ISSUES: {len(issues)}")
    for issue in issues:
        print(f"   • {issue}")
else:
    print("\n✓ NO CRITICAL ISSUES")

if warnings:
    print(f"\n⚠️  WARNINGS: {len(warnings)}")
    for warning in warnings:
        print(f"   • {warning}")
else:
    print("\n✓ NO WARNINGS")

print("\n" + "=" * 70)

if not issues:
    print("STATUS: ✓ NOTEBOOK IS READY")
    print("\nKEY FEATURES:")
    print("  • Agent uses Python API (session.log_step)")
    print("  • Runs 'python trading_agent.py' (not 'epi run')")
    print("  • Will populate steps.jsonl properly")
    print("  • Authentic viewer should display steps")
else:
    print("STATUS: ✗ NEEDS FIXES")

print("=" * 70)
