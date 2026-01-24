"""Test the chat command with automatic input."""
import subprocess
import os

# Set API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAs-fKsFJjwa0-uDjo2ekNjDccu1kNf_gY"

# Run chat command with input piped
process = subprocess.Popen(
    ["python", "-m", "epi_cli", "chat", "epi-recordings\\investor_demo_20260124_070100.epi"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    env=os.environ
)

# Send a question and then exit
input_text = "What steps are in this recording?\nexit\n"
stdout, stderr = process.communicate(input=input_text, timeout=60)

print("STDOUT:")
print(stdout)
print("\nSTDERR:")
print(stderr[:1000] if stderr else "(none)")
