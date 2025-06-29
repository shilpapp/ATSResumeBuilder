import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
MODEL   = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

if not api_key:
    raise ValueError("OPENAI_API_KEY not set in .env")

client = OpenAI(api_key=api_key)

# Paths
RESUME_FILE = "resume_data.json"
PROMPT_FILE = "prompt.txt"
OUTPUT_FILE = "resume_data_updated.json"

# Read resume
with open(RESUME_FILE, "r", encoding="utf-8") as f:
    resume_data = json.load(f)

# Read prompt
with open(PROMPT_FILE, "r", encoding="utf-8") as f:
    user_prompt = f.read().strip()

# Build messages
system_prompt = (
    "You are a resume assistant. Based on the user's request, "
    "update the given resume JSON. Output ONLY the updated JSON, no markdown or explanations."
)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": f"""Resume:\n{json.dumps(resume_data, indent=2)}\n\nPrompt:\n{user_prompt}"""}
]

# ChatGPT API call
response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    temperature=0.3
)


# Extract and try to parse JSON
result = response.choices[0].message.content
try:
    updated_resume = json.loads(result)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(updated_resume, f, indent=2)
    print(f"✅ Resume updated and saved to '{OUTPUT_FILE}'")
except json.JSONDecodeError:
    print("❌ GPT returned invalid JSON. Here's the output:\n")
    print(result)
