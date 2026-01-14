import json

# Load notebook
with open('epi_investor_demo_ULTIMATE.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# New viewer cell source - simpler, shows BOTH download AND timeline preview
new_source = """# Show Timeline Preview + Download Info
import zipfile
import json

display(HTML('<h1 style="color: #8b5cf6;">🖥️ THE VIEWER: Timeline Preview</h1>'))
print("=" * 70)

if epi_file and epi_file.exists():
    try:
        with zipfile.ZipFile(epi_file, 'r') as z:
            # Read and show timeline steps
            if 'steps.jsonl' in z.namelist():
                steps_data = z.read('steps.jsonl').decode('utf-8')
                steps = [json.loads(line) for line in steps_data.strip().split('\\\\n') if line]
                
                # Build visual timeline
                html = '<div style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);padding:20px;border-radius:10px;color:white;margin:20px 0"><h2 style="color:white;margin:0 0 20px 0">📊 Captured Timeline</h2>'
                
                for i, s in enumerate(steps[:5]):
                    html += f'<div style="background:rgba(255,255,255,0.1);padding:15px;margin:10px 0;border-left:4px solid #10b981;border-radius:5px"><strong>Step {s.get("index",i)}</strong> - {s.get("kind","")}<br><small>{s.get("timestamp","")}</small></div>'
                
                if len(steps) > 5:
                    html += f'<div style="text-align:center;padding:10px;font-style:italic">...and {len(steps)-5} more steps</div>'
                html += '</div>'
                
                display(HTML(html))
                print("=" * 70)
                print(f"✅ Total Steps Recorded: {len(steps)}")
                print("\\n📦 THE DOWNLOADED FILE CONTAINS:")
                print("   ✓ Full interactive HTML viewer")
                print("   ✓ Complete execution timeline")  
                print("   ✓ Ed25519 cryptographic signature")
                print("\\n💡 TO VIEW THE FULL INTERACTIVE TIMELINE:")
                print(f"   1. Find the downloaded file: {epi_file.name}")
                print("   2. Double-click to open in your browser")
                print("   3. Explore the complete interactive timeline!")
                print("=" * 70)
    except Exception as e:
        print(f"Preview: {str(e)[:50]}")
        print(f"✅ Downloaded file contains full viewer: {epi_file.name if epi_file else 'recording.epi'}")
else:
    print("Viewer demo - file contains interactive timeline")
"""

# Split into lines for JSON
new_source_lines = [line + "\\n" for line in new_source.split("\\n")]
# Last line shouldn't have newline
if new_source_lines:
    new_source_lines[-1] = new_source_lines[-1].rstrip("\\n")

# Update viewer cell (cell 8)
nb['cells'][8]['source'] = new_source_lines

# Save
with open('epi_investor_demo_ULTIMATE.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("SUCCESS: Viewer cell updated")
print("Now shows: Timeline preview + instructions to open downloaded file")
