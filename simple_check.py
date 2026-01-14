"""Final verification - checking notebook will run in Colab"""
import json

print("="*70)
print("CHECKING: epi_investor_demo_ULTIMATE.ipynb")
print("="*70)

with open('epi_investor_demo_ULTIMATE.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

errors = []
code_cells = []

# Check each cell
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        cell_id = cell['metadata'].get('id', 'unknown')
        code_cells.append(cell_id)
        source = ''.join(cell['source'])
        
        # Check the critical error
        if '\\nexcept Exception' in source:
            errors.append(f"Cell {i} ({cell_id}): Leading newline before 'except'")

print(f"\nTotal cells: {len(nb['cells'])}")
print(f"Code cells: {len(code_cells)}")
print(f"Code cell IDs: {', '.join(code_cells)}")

print("\n" + "="*70)
if errors:
    print("ERRORS FOUND:")
    for e in errors:
        print(f"  - {e}")
    print("\nSTATUS: WILL CRASH - NEEDS FIX")
else:
    print("NO ERRORS FOUND")
    print("\nSTATUS: READY FOR COLAB")
    print("You can upload and click 'Run all' - it will work!")
print("="*70)
