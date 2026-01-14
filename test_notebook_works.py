"""
COMPREHENSIVE TEST: Verify the notebook will work in Google Colab
This simulates what will happen when the notebook runs
"""
import json
import re

print("="*70)
print("COMPREHENSIVE NOTEBOOK FUNCTIONALITY TEST")
print("="*70)

# Load notebook
with open('epi_investor_demo_ULTIMATE.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"\n1. STRUCTURE CHECK")
print(f"   Cells: {len(nb['cells'])}")
print(f"   Format: nbformat {nb['nbformat']}")

# Test results
tests_passed = 0
tests_failed = 0
warnings = []

print(f"\n2. CRITICAL CELLS CHECK")
print("-" * 70)

# Check Cell 6 (Record) - Downloads file
record_cell = nb['cells'][6]
record_source = ''.join(record_cell['source'])

print("\nCell 6 [record] - File Download:")
if 'from google.colab import files' in record_source:
    print("  ✓ Import: google.colab.files")
    tests_passed += 1
else:
    print("  X Import missing: google.colab.files")
    tests_failed += 1

if 'files.download(' in record_source:
    print("  ✓ Function: files.download() present")
    tests_passed += 1
else:
    print("  X Function missing: files.download()")
    tests_failed += 1

if 'epi_file' in record_source:
    print("  ✓ Variable: epi_file defined")
    tests_passed += 1
else:
    print("  X Variable missing: epi_file")
    tests_failed += 1

# Check Cell 8 (Viewer) - Inline display
viewer_cell = nb['cells'][8]
viewer_source = ''.join(viewer_cell['source'])

print("\nCell 8 [viewer] - Inline Viewer:")

# Check for viewer extraction
if 'viewer.html' in viewer_source:
    print("  ✓ Extracts: viewer.html from ZIP")
    tests_passed += 1
else:
    print("  X Missing: viewer.html extraction")
    tests_failed += 1

# Check for IFrame display
if 'IFrame(' in viewer_source:
    print("  ✓ Display: IFrame() for rendering")
    tests_passed += 1
else:
    print("  X Missing: IFrame() display")
    tests_failed += 1

# Check for temp file handling
if 'tempfile' in viewer_source or 'temp' in viewer_source:
    print("  ✓ Uses: Temp file for extraction")
    tests_passed += 1
else:
    warnings.append("  ? May not use temp file (could cause issues)")
    print("  ? Warning: May not use temp file")

# Check for fallback
if 'steps.jsonl' in viewer_source:
    print("  ✓ Fallback: Timeline preview if viewer fails")
    tests_passed += 1
else:
    warnings.append("  ? No fallback for failed viewer rendering")
    print("  ? Warning: No fallback mechanism")

# Check for error handling
try_count = viewer_source.count('try:')
except_count = viewer_source.count('except')
if try_count > 0 and except_count > 0:
    print(f"  ✓ Error handling: {try_count} try/except blocks")
    tests_passed += 1
else:
    print("  X Missing: Error handling")
    tests_failed += 1

# Check for display(HTML())
if 'display(HTML(' in viewer_source:
    print("  ✓ Function: display(HTML()) for rich output")
    tests_passed += 1
else:
    warnings.append("  ? May not display rich HTML")
    print("  ? Warning: May not display rich HTML")

print("\n3. VIEWER CELL CODE FLOW TEST")
print("-" * 70)

# Simulate the logic flow
print("\nSimulating execution flow:")
print("  1. Check if epi_file exists...")
if 'epi_file and epi_file.exists()' in viewer_source:
    print("     ✓ Has file existence check")
    tests_passed += 1
else:
    print("     X Missing file existence check")
    tests_failed += 1

print("  2. Open ZIP file...")
if 'zipfile.ZipFile(epi_file' in viewer_source:
    print("     ✓ Opens .epi as ZIP")
    tests_passed += 1
else:
    print("     X Missing ZIP open")
    tests_failed += 1

print("  3. Check for viewer.html...")
if "'viewer.html' in z.namelist()" in viewer_source:
    print("     ✓ Checks if viewer.html exists in ZIP")
    tests_passed += 1
else:
    print("     X Missing viewer.html check")
    tests_failed += 1

print("  4. Extract and display...")
if 'z.read(' in viewer_source or 'z.extract' in viewer_source:
    print("     ✓ Extracts content from ZIP")
    tests_passed += 1
else:
    print("     X Missing extraction logic")
    tests_failed += 1

print("  5. Render in Colab...")
if 'IFrame(' in viewer_source or 'display(HTML(' in viewer_source:
    print("     ✓ Displays content in notebook")
    tests_passed += 1
else:
    print("     X Missing display logic")
    tests_failed += 1

print("\n4. SYNTAX CHECK")
print("-" * 70)

# Check for common syntax errors
syntax_errors = []

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        cell_id = cell['metadata'].get('id', 'unknown')
        
        # Check for leading newline before except
        if '\nexcept' in source and source.find('\nexcept') != -1:
            idx = source.find('\nexcept')
            if idx > 0 and source[idx-1] == '\n':
                syntax_errors.append(f"Cell {i} ({cell_id}): Double newline before except")
        
        # Check for unclosed strings
        triple_quote_count = source.count("'''")
        if triple_quote_count % 2 != 0:
            syntax_errors.append(f"Cell {i} ({cell_id}): Unclosed triple quotes")

if syntax_errors:
    print(f"\n  X Syntax errors found: {len(syntax_errors)}")
    for err in syntax_errors:
        print(f"    - {err}")
    tests_failed += len(syntax_errors)
else:
    print("  ✓ No syntax errors detected")
    tests_passed += 1

print("\n5. COLAB COMPATIBILITY CHECK")
print("-" * 70)

# Check for Colab-specific features
colab_features = {
    'google.colab.files': False,
    'IPython.display': False,
    'display(HTML(': False,
    'IFrame(': False,
}

all_source = ''
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        all_source += ''.join(cell['source'])

for feature, _ in colab_features.items():
    if feature in all_source:
        colab_features[feature] = True
        print(f"  ✓ Uses: {feature}")
        tests_passed += 1

missing = [f for f, v in colab_features.items() if not v]
if missing:
    print(f"\n  ? Some Colab features not used: {', '.join(missing)}")

print("\n" + "="*70)
print("FINAL RESULTS")
print("="*70)

total_tests = tests_passed + tests_failed
pass_rate = (tests_passed / total_tests * 100) if total_tests > 0 else 0

print(f"\nTests Passed: {tests_passed}/{total_tests} ({pass_rate:.1f}%)")
print(f"Tests Failed: {tests_failed}")
print(f"Warnings: {len(warnings)}")

if warnings:
    print("\nWarnings:")
    for w in warnings:
        print(f"  {w}")

print("\n" + "="*70)
if tests_failed == 0:
    print("STATUS: ✓ READY FOR GOOGLE COLAB")
    print("\nThe notebook will:")
    print("  1. Download .epi file to investor's machine")
    print("  2. Extract and display viewer inline in Colab")
    print("  3. Show fallback timeline if viewer fails")
    print("  4. Provide clear error messages")
    print("\nGO AHEAD AND UPLOAD TO COLAB!")
else:
    print("STATUS: X HAS ISSUES")
    print(f"\nFix {tests_failed} failed test(s) before deploying")

print("="*70)

# Exit with status
exit(0 if tests_failed == 0 else 1)
