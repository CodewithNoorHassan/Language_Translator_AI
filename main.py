from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

# Configure Gemini API
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

# List of languages
languages = ["Urdu", "French", "Spanish", "Chinese", "German", "Arabic", "Hindi", "Turkish"]

# Get input from user
text_to_translate = input("Enter text to translate: ")

# Build prompt
prompt = f"""
You are a highly intelligent translation agent. Your task is to translate the given text into the following languages:
{', '.join(languages)}.

Please return each translation with the language name clearly labeled.
For example:
Urdu: ...
French: ...
Spanish: ...
...

Text to translate: {text_to_translate}
"""

response = model.generate_content(prompt)

print("\n🌍 Translations:\n")
print(response.text)
