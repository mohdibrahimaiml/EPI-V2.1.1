import zipfile
import json

epi_path = 'epi-recordings/test_gemini_real_20260124_060146.epi'

with zipfile.ZipFile(epi_path, 'r') as z:
    print('Files in .epi:', z.namelist())
    
    # Read steps.jsonl
    content = z.open('steps.jsonl').read().decode('utf-8')
    lines = [line for line in content.strip().split('\n') if line]
    
    print(f'\nTotal steps: {len(lines)}')
    print('\n' + '='*60)
    
    for line in lines:
        step = json.loads(line)
        kind = step.get('kind', 'unknown')
        content = step.get('content', {})
        provider = content.get('provider', 'N/A')
        
        print(f"Step {step['index']}: {kind} (provider={provider})")
        
        if kind == 'llm.request':
            contents = str(content.get('contents', ''))[:100]
            print(f"   -> Prompt: {contents}...")
        elif kind == 'llm.response':
            response = str(content.get('response', ''))[:100]
            print(f"   -> Response: {response}...")
        elif kind == 'llm.error':
            error = content.get('error', 'unknown')
            print(f"   -> ERROR: {error}")
