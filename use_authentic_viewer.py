"""
PROPER FIX - Use the AUTHENTIC viewer.html from the .epi file
and just inject the signature status into it
"""

import json
from pathlib import Path

notebook_path = Path(r"c:\Users\dell\OneDrive\Desktop\EPI_DEMO_demo.ipynb")
backup_path = Path(r"c:\Users\dell\OneDrive\Desktop\EPI_DEMO_demo.ipynb.backup5")

print("=" * 70)
print("FIXING TO USE AUTHENTIC VIEWER")
print("=" * 70)

# Read notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Backup
print(f"\nCreating backup: {backup_path}")
with open(backup_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

# New viewer cell that uses AUTHENTIC viewer
viewer_cell_code = '''# @title 👁️ View Timeline (Authentic Viewer) { display-mode: "form" }
import zipfile, json, html, os
from pathlib import Path
from IPython.display import display, HTML

epi_files = list(Path('.').glob('*.epi')) + list(Path('.').glob('epi-recordings/*.epi'))
epi_file = max(epi_files, key=os.path.getmtime) if epi_files else None

if not epi_file:
    print("No .epi file found")
else:
    print(f"Loading: {epi_file.name}")
    
    with zipfile.ZipFile(epi_file, 'r') as z:
        # Extract signature from manifest
        sig_status = "Unsigned"
        sig_color = "#eab308"
        
        if 'manifest.json' in z.namelist():
            m = json.loads(z.read('manifest.json').decode('utf-8'))
            sig = m.get('signature', '')
            if sig and sig.strip():
                sig_status = "Signed"
                sig_color = "#22c55e"
                print(f"Status: SIGNED")
        
        # Try to load AUTHENTIC viewer from .epi file
        viewer_html = None
        for fname in z.namelist():
            if fname.endswith('viewer.html') or fname.endswith('.html'):
                try:
                    viewer_html = z.read(fname).decode('utf-8', errors='ignore')
                    print(f"Loaded authentic viewer: {fname}")
                    
                    # Inject signature status into the authentic viewer
                    # Replace "Unsigned" text with actual status
                    if 'Unsigned' in viewer_html:
                        viewer_html = viewer_html.replace('Unsigned', sig_status)
                    
                    # Update colors if needed
                    if sig_status == "Signed":
                        viewer_html = viewer_html.replace('#eab308', sig_color)
                        viewer_html = viewer_html.replace('⚠', '✓')
                    
                    break
                except:
                    pass
        
        # If no authentic viewer found, use minimal fallback
        if not viewer_html:
            print("No authentic viewer found, using fallback")
            steps = []
            if 'steps.jsonl' in z.namelist():
                for line in z.read('steps.jsonl').decode('utf-8').splitlines():
                    if line.strip():
                        steps.append(json.loads(line))
            
            viewer_html = f"""<!DOCTYPE html>
<html><head><script src="https://cdn.tailwindcss.com"></script></head>
<body style="background:#f8fafc;padding:20px">
<div style="max-width:900px;margin:0 auto;background:white;border-radius:12px;overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.1)">
  <div style="background:#1e293b;color:white;padding:20px;display:flex;justify-content:space-between">
    <div><h1 style="margin:0;font-size:18px">EPI Viewer</h1></div>
    <div style="color:{sig_color};font-weight:600">{sig_status}</div>
  </div>
  <div id="steps"></div>
</div>
<script>
const steps={json.dumps(steps)};
const c=document.getElementById('steps');
steps.forEach(s=>{{
  const d=document.createElement('div');
  d.style='padding:16px;border-bottom:1px solid #e2e8f0';
  d.textContent=(s.kind||'LOG')+': '+JSON.stringify(s.content||s.message||'');
  c.appendChild(d);
}});
</script></body></html>"""
        
        # Display viewer
        escaped = html.escape(viewer_html)
        wrapper = f'<iframe srcdoc="{escaped}" width="100%" height="700" style="border:2px solid {sig_color};border-radius:12px"></iframe>'
        display(HTML(wrapper))
'''

# Replace viewer cell
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'srcdoc' in source and 'viewer' in source.lower():
            print(f"\nReplacing viewer cell at index {i}")
            cell['source'] = viewer_cell_code.split('\n')
            cell['source'] = [line + '\n' if j < len(cell['source'])-1 else line 
                             for j, line in enumerate(cell['source'])]
            break

# Save
print(f"Saving: {notebook_path}")
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print("\n" + "=" * 70)
print("FIXED!")
print("=" * 70)
print("\nNow uses:")
print("  1. AUTHENTIC viewer.html from .epi file (if exists)")
print("  2. Injects correct signature status (Signed/Unsigned)")
print("  3. Updates colors accordingly")
print("\nUpload to Colab and test!")
print("=" * 70)
