"""
CORRECT FIX - Extract the viewer.html and the embedded manifest JSON data
The signature is already in the manifest data, the viewer just needs to read it
"""

import json
from pathlib import Path

notebook_path = Path(r"c:\Users\dell\OneDrive\Desktop\EPI_DEMO_demo.ipynb")
backup_path = Path(r"c:\Users\dell\OneDrive\Desktop\EPI_DEMO_demo.ipynb.backup_final")

print("=" * 70)
print("CORRECT FIX - Using EPI's actual viewer mechanism")
print("=" * 70)

# Read notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Backup
print(f"\nCreating backup: {backup_path}")
with open(backup_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

# The CORRECT viewer cell - just extract and display the authentic viewer
viewer_cell_code = '''# @title 👁️ View EPI Timeline { display-mode: "form" }
import zipfile, html, os
from pathlib import Path
from IPython.display import display, HTML

epi_files = list(Path('.').glob('*.epi')) + list(Path('.').glob('epi-recordings/*.epi'))
epi_file = max(epi_files, key=os.path.getmtime) if epi_files else None

if not epi_file:
    print("❌ No .epi file found. Run the recording cell first.")
else:
    print(f"📂 Loading: {epi_file.name}")
    
    with zipfile.ZipFile(epi_file, 'r') as z:
        # Extract the AUTHENTIC viewer.html (already has manifest embedded)
        viewer_html = None
        
        for fname in z.namelist():
            if fname.endswith('viewer.html') or (fname.endswith('.html') and 'viewer' in fname.lower()):
                viewer_html = z.read(fname).decode('utf-8', errors='ignore')
                print(f"✅ Loaded authentic viewer: {fname}")
                print(f"📄 Size: {len(viewer_html)} characters")
                
                # Check if manifest data is embedded
                if 'epi-data' in viewer_html:
                    print("✅ Manifest data is embedded in viewer")
                elif '"manifest"' in viewer_html:
                    print("✅ Manifest JSON found in viewer")
                else:
                    print("⚠️ Warning: Manifest data may not be embedded")
                
                break
        
        if not viewer_html:
            print("❌ No viewer.html found in .epi file")
            print("This usually means the .epi file was not created properly.")
            print("Try running the recording cell again with auto_sign=True")
        else:
            # Display the authentic viewer AS-IS
            # The signature status is already in the embedded manifest JSON
            escaped = html.escape(viewer_html)
            iframe = f'<iframe srcdoc="{escaped}" width="100%" height="750" style="border:2px solid #334155;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,0.1)"></iframe>'
            
            print("=" * 70)
            print("✅ VIEWER LOADED")
            print("=" * 70)
            print("The viewer will automatically show the signature status")
            print("from the embedded manifest data.")
            print("=" * 70)
            
            display(HTML(iframe))
'''

# Replace viewer cell
viewer_replaced = False
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'srcdoc' in source and 'viewer' in source.lower():
            print(f"\nReplacing viewer cell at index {i}")
            cell['source'] = viewer_cell_code.split('\n')
            cell['source'] = [line + '\n' if j < len(cell['source'])-1 else line 
                             for j, line in enumerate(cell['source'])]
            viewer_replaced = True
            break

if not viewer_replaced:
    print("\n⚠️ WARNING: Could not find viewer cell to replace")
else:
    # Save
    print(f"Saving: {notebook_path}")
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

    print("\n" + "=" * 70)
    print("DONE! This is how EPI actually works:")
    print("=" * 70)
    print("1. The .epi file contains viewer.html")
    print("2. The viewer.html has manifest JSON embedded in it")
    print("3. The manifest.signature field contains the signature")
    print("4. The viewer JavaScript reads manifest.signature automatically")
    print("\nNo manual replacement needed - the viewer handles it!")
    print("\nIf it still shows 'Unsigned', the .epi file was not signed properly.")
    print("Make sure the recording cell uses auto_sign=True")
    print("=" * 70)
