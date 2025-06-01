from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# List of languages
languages = ["Urdu", "French", "Spanish", "Chinese", "German", "Arabic", "Hindi", "Turkish"]

# Translator Agent
translator = Agent(
    name="Multilingual Translator Agent",
    instructions=f"""
    You are a highly intelligent translation agent. Your task is to translate the given text into the following languages:
    {', '.join(languages)}.

    Please return each translation with the language name clearly labeled.
    For example:
    Urdu: ...
    French: ...
    Spanish: ...
    ...
    """
)

# Get input from user
text_to_translate = input("Enter text to translate: ")

response = Runner.run_sync(
    translator,
    input=text_to_translate,
    run_config=config
)

print("\n🌍 Translations:\n")
print(response.final_output)
