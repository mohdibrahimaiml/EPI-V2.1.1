"""List available Gemini models for this API key."""
import os
import warnings
warnings.filterwarnings("ignore")

os.environ["GOOGLE_API_KEY"] = "AIzaSyAs-fKsFJjwa0-uDjo2ekNjDccu1kNf_gY"

import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("Available models that support generateContent:")
print("=" * 60)

for model in genai.list_models():
    methods = model.supported_generation_methods
    if "generateContent" in methods:
        print(f"  - {model.name}")
