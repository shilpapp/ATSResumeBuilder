# 🧠 Resume Parser to JSON Generator (Python Only)

A Python-only tool to convert plain-text resumes and job descriptions into structured JSON.
Supports keywords and OpenAI for smart formatting.
Easy to use with a single input file (prompt.txt).
Ideal for use with resume platforms like Reactive Resume https://rxresu.me/. 
---

## 🚀 Features

- Parses plain-text resume (TSX/text format)
- Accepts keywords and job description (JD) as input
- Outputs structured JSON (resume schema)
- 100% Python — no Node.js required

---

## 📦 Requirements

- Python 3.8 or later
- `openai` library (optional if you're using AI-based features)

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔐 1. How to Create an OpenAI API Key

1. Go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
2. Log in or sign up
3. Click “Create new secret key”
4. Copy and save it securely

Add the key to your environment variables (Linux/macOS):

```bash
export OPENAI_API_KEY="your-api-key-here"
```

For Windows Command Prompt:

```cmd
set OPENAI_API_KEY=your-api-key-here
```

---

## 🧾 2. Where to Put Inputs

Use the `prompt.txt` file to provide:

- Your **resume** (TSX or plain text format)
- Your **job description (JD)**
- Any **keywords** (optional)

**Format Example in `prompt.txt`:**

```
===RESUME===
Paste your resume content here

===JD===
Paste your job description here

===KEYWORDS===
React, TypeScript, Accessibility, DevOps
```

The script will automatically extract and process each section.

---

## 🐍 3. Run the Python Script

Run the Python script to parse and generate the JSON resume:

```bash
python resume_updater_script.py
```

This will generate:

```
✅ Output: resume_data_updated.json
```

The file will be saved in your working directory and can be uploaded to resume tools like Reactive Resume.

---

## 📂 Output

- `resume_data_updated.json` — Structured resume in JSON format

---

Now your ATS Dynamic resume json ready to upload on https://rxresu.me/. 

## 🧑‍💻 Maintainer

Created with ❤️ by **Shilpa Pendharkar**  
[LinkedIn Profile](https://www.linkedin.com/in/shilpa-pendharkar/)
