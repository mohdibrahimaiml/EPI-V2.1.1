import json

# Read the notebook
with open('epi_investor_demo_ULTIMATE.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Fix cell 6, line 56
# The problem is it has '\\n' (escaped backslash-n) instead of '\n' (newline)
record_cell = nb['cells'][6]

print("BEFORE:")
print(f"Line 56: {repr(record_cell['source'][56])}")

# Set the correct value
record_cell['source'][56] = 'except Exception as e:\n'

print("\nAFTER:")
print(f"Line 56: {repr(record_cell['source'][56])}")

# Save
with open('epi_investor_demo_ULTIMATE.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print("\nFIXED: Notebook saved")
print("Status: Ready for Colab upload")
