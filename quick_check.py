from pathlib import Path
import zipfile, json

f = max(Path('epi-recordings').glob('*.epi'), key=lambda p: p.stat().st_mtime)
with zipfile.ZipFile(f) as z:
    m = json.loads(z.read('manifest.json'))
    print(f'File: {f.name}')
    sig = m.get('signature')
    if sig:
        print(f'Signed: YES')
        print(f'Signature: {sig[:60]}...')
    else:
        print('Signed: NO')
