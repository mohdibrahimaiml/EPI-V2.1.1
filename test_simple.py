import json

print("="*70)
print("NOTEBOOK FUNCTIONALITY TEST")
print("="*70)

with open('epi_investor_demo_ULTIMATE.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"\nCells: {len(nb['cells'])}")

# Check viewer cell
viewer_cell = nb['cells'][8]
viewer_source = ''.join(viewer_cell['source'])

print("\nVIEWER CELL CHECK:")
print("-" * 70)

checks = {
    'IFrame import': 'from IPython.display import IFrame' in viewer_source,
    'zipfile import': 'import zipfile' in viewer_source,
    'Extracts viewer.html': "'viewer.html' in z.namelist()" in viewer_source,
    'Uses tempfile': 'tempfile' in viewer_source or 'temp_dir' in viewer_source,
    'Displays with IFrame': 'IFrame(' in viewer_source,
    'Has fallback (steps.jsonl)': "'steps.jsonl' in z.namelist()" in viewer_source,
    'Has error handling': 'try:' in viewer_source and 'except' in viewer_source,
    'Uses display(HTML())': 'display(HTML(' in viewer_source,
}

passed = 0
failed = 0

for check, result in checks.items():
    if result:
        print(f"  [OK] {check}")
        passed += 1
    else:
        print(f"  [FAIL] {check}")
        failed += 1

# Check record cell
record_cell = nb['cells'][6]
record_source = ''.join(record_cell['source'])

print("\n
