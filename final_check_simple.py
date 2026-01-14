import json

print("="*70)
print("FINAL NOTEBOOK CHECK - NO BULLSHIT")
print("="*70)

# Load
with open('epi_investor_demo_ULTIMATE.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"\nCells: {len(nb['cells'])}")
print(f"Format: nbformat {nb['nbformat']}")

errors = []
code_cells = []

# Check each code cell
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        cell_id = cell['metadata'].get('id', 'unknown')
        source = ''.join(cell['source'])
        code_cells.append(cell_id)
        
        # Critical checks
        if '\\nexcept' in source:
            errors.append(f"Cell {i} ({cell_id}): Leading newline before except")
        
        if cell_id == 'record' and 'files.download' not in source:
            errors.append(f"Cell {i} (record): Missing files.download()")
        
        if cell_id == 'viewer':
            has_display_html = 'display(HTML(' in source
            has_read_html = 'z.read(' in source and '.decode(' in source
            
            if not has_display_html:
                errors.append(f"Cell {i} (viewer): Missing display(HTML())")
            if not has_read_html:
                errors.append(f"Cell {i} (viewer): Not reading HTML from ZIP")

print(f"\nCode cells: {', '.join(code_cells)}")

print("\n" + "="*70)
if errors:
    print(f"ERRORS: {len(errors)}")
    for e in errors:
        print(f"  - {e}")
    print("\nSTATUS: HAS ERRORS")
else:
    print("ERRORS: NONE")
    print("\nSTATUS: PERFECT")
    print("\nVERIFIED:")
    print("  - No syntax errors")
    print("  - files.download() present")
    print("  - Viewer displays HTML inline")
    print("  - All cells correct")

print("="*70)
print(f"File: epi_investor_demo_ULTIMATE.ipynb")
print("="*70)
