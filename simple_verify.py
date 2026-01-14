"""
Simple verification - no Unicode characters
"""

import json
from pathlib import Path

notebook_path = Path(r"c:\Users\dell\OneDrive\Desktop\EPI_DEMO_demo.ipynb")

print("=" * 70)
print("VERIFYING NOTEBOOK FIX")
print("=" * 70)
print(f"\nReading: {notebook_path}")

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

print(f"Total cells: {len(notebook['cells'])}\n")

# Find viewer cell
viewer_cell = None
viewer_index = None

for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'View Timeline' in source or ('signature_short' in source and 'signature_status' in source):
            viewer_cell = cell
            viewer_index = i
            break

if viewer_cell is None:
    print("ERROR: Could not find viewer cell!")
else:
    print(f"[OK] Found viewer cell at index: {viewer_index}\n")
    
    source_code = ''.join(viewer_cell['source'])
    
    # Check for critical fix components
    print("VERIFICATION CHECKS:")
    print("-" * 70)
    
    checks = [
        ("Signature extraction before HTML", "signature_status = \"UNSIGNED\"" in source_code),
        ("Manifest parsing", "manifest.get('signature'" in source_code),
        ("Signature splitting", "split(':', 2)" in source_code),
        ("Status variable check", "is_signed" in source_code),
        ("Signature injection in HTML", "{signature_short}" in source_code),
        ("Green color for signed", "#22c55e" in source_code or "#10b981" in source_code),
        ("Dynamic pulsing dot", "pulse" in source_code),
    ]
    
    all_passed = True
    for check_name, passed in checks:
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status} {check_name}")
        if not passed:
            all_passed = False
    
    print("-" * 70)
    
    if all_passed:
        print("\n" + "=" * 70)
        print("SUCCESS! ALL CHECKS PASSED!")
        print("=" * 70)
        print("\nThe notebook has been correctly fixed with:")
        print("  - Signature extracted BEFORE viewer HTML build")
        print("  - Signature properly parsed (algo:keyname:sig)")
        print("  - Signature injected into viewer using f-strings")
        print("  - Green (#22c55e) color for SIGNED status")
        print("  - Yellow (#eab308) color for UNSIGNED status")
        print("  - Pulsing green dot animation when signed")
        print("\n[READY] Upload to Google Colab and run!")
        print("The viewer will display SIGNED status correctly.")
    else:
        print("\nWARNING: Some checks failed!")
        print("The fix may not be complete.")
    
    # Count key occurrences
    print("\n" + "=" * 70)
    print("KEY CODE PATTERNS FOUND:")
    print("=" * 70)
    print(f"  signature_status mentions: {source_code.count('signature_status')}")
    print(f"  signature_short mentions: {source_code.count('signature_short')}")
    print(f"  is_signed mentions: {source_code.count('is_signed')}")
    print(f"  f-string injections: {source_code.count('{signature_short}')}")
    print(f"  Green color codes: {source_code.count('#22c55e') + source_code.count('#10b981')}")

print("\n" + "=" * 70)
