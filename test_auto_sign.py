# Test if auto_sign works
from epi_recorder import record
from pathlib import Path
import zipfile
import json

print("Testing auto_sign...")

with record("test_auto_sign.epi", workflow_name="Auto Sign Test", auto_sign=True) as epi:
    epi.log_step("TEST", {"message": "testing signature"})

# Check the file
test_file = Path("test_auto_sign.epi")
if test_file.exists():
    with zipfile.ZipFile(test_file, 'r') as z:
        manifest = json.loads(z.read('manifest.json'))
        sig = manifest.get('signature')
        
        if sig:
            print(f"SUCCESS! Signature: {sig[:50]}...")
        else:
            print("FAIL: No signature even with auto_sign=True")
            print(f"Manifest keys: {list(manifest.keys())}")
    
    test_file.unlink()
else:
    print("FAIL: File not created")
