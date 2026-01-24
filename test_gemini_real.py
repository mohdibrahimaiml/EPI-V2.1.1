"""
Real-world test of Gemini integration with EPI.
This tests both the patcher AND the chat command.
"""
import os

# Check for API key first
api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("=" * 60)
    print("ERROR: No Gemini API key found!")
    print()
    print("Please set your API key:")
    print("  Windows: set GOOGLE_API_KEY=your-key-here")
    print("  Mac/Linux: export GOOGLE_API_KEY=your-key-here")
    print()
    print("Get a free key at: https://makersuite.google.com/app/apikey")
    print("=" * 60)
    exit(1)

print("=" * 60)
print("EPI Gemini Integration Test")
print("=" * 60)
print()

# Step 1: Import and configure Gemini
print("[1/4] Importing Google Generative AI...")
import google.generativeai as genai
genai.configure(api_key=api_key)
print("      OK - Configured with API key")

# Step 2: Create model
print("[2/4] Creating Gemini model (gemini-2.0-flash)...")
model = genai.GenerativeModel("gemini-2.0-flash")
print("      OK - Model created")

# Step 3: Make a real API call
print("[3/4] Making real API call to Gemini...")
print("      Prompt: 'What is 2+2? Reply with just the number.'")
response = model.generate_content("What is 2+2? Reply with just the number.")
print(f"      Response: {response.text.strip()}")

# Step 4: Make another call with more context
print("[4/4] Making second API call...")
print("      Prompt: 'Say hello in 3 words or less'")
response2 = model.generate_content("Say hello in 3 words or less")
print(f"      Response: {response2.text.strip()}")

print()
print("=" * 60)
print("TEST COMPLETE - Check the .epi file for captured calls!")
print("=" * 60)
