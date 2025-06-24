import streamlit as st
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check for API key
if not gemini_api_key:
    st.error("❌ GEMINI_API_KEY is not set.")
    st.stop()

# Configure AI model
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

# Language options with emoji flair
language_options = {
    "English": "🇬🇧",
    "Urdu": "🇵🇰",
    "French": "🇫🇷",
    "Spanish": "🇪🇸",
    "Chinese": "🇨🇳",
    "German": "🇩🇪",
    "Arabic": "🇸🇦",
    "Hindi": "🇮🇳",
    "Turkish": "🇹🇷",
    "Italian": "🇮🇹",
    "Japanese": "🇯🇵",
    "Russian": "🇷🇺",
    "Korean": "🇰🇷"
}

# Page config with real emoji (not surrogate pair)
st.set_page_config(page_title="Translator", page_icon="🌐", layout="wide")

# Inject minimal Tailwind-style CSS (mimicked)
st.markdown("""
    <style>
    .title {
        font-size: 3rem;
        color: #0ea5e9;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        font-size: 0.8rem;
        color: gray;
        margin-top: 40px;
    }
    .card {
        background: #f0f9ff;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🌍 Multilingual Translator</div>', unsafe_allow_html=True)

# Sidebar language selection
with st.sidebar:
    st.header("⚙️ Options")
    from_lang = st.selectbox(
        "Translate from:",
        options=list(language_options.keys()),
        index=0,
        format_func=lambda x: f"{language_options[x]} {x}"
    )

    default_targets = [lang for lang in ["Urdu", "French", "Spanish"] if lang != from_lang]
    to_langs = st.multiselect(
        "Translate to:",
        options=[lang for lang in language_options.keys() if lang != from_lang],
        default=default_targets,
        format_func=lambda x: f"{language_options[x]} {x}"
    )

# Input area
st.markdown("---")
st.subheader("✍️ Enter Text")
text = st.text_area(f"Type your text in {language_options[from_lang]} {from_lang}:", height=160)

# Translation UI card
def show_translation(lang, translated_text):
    st.markdown(f"""
    <div class='card'>
        <span style='font-size:1.3rem'>{language_options.get(lang, '🌐')} <strong>{lang}</strong></span><br>
        {translated_text}
    </div>
    """, unsafe_allow_html=True)

# Async translation
async def get_translation(user_input, from_language, target_languages):
    instructions = f"""
    You are a translation agent. Translate the following text from {from_language} into the following languages:
    {', '.join(target_languages)}.
    Return translations clearly labeled like:
    Urdu: ...
    French: ...
    """
    agent = Agent(
        name="Multilingual Translator Agent",
        instructions=instructions
    )
    return await Runner.run(agent, input=user_input, run_config=config)

# Translate button
if st.button("🔁 Translate", use_container_width=True):
    if not text.strip():
        st.warning("⚠️ Enter text to translate.")
    elif not to_langs:
        st.warning("⚠️ Select at least one target language.")
    else:
        with st.spinner("⏳ Translating..."):
            try:
                response = asyncio.run(get_translation(text, from_lang, to_langs))
                st.success("✅ Translation complete!")
                for line in response.final_output.split("\n"):
                    if ":" in line:
                        lang, trans = line.split(":", 1)
                        show_translation(lang.strip(), trans.strip())
            except Exception as e:
                st.error(f"❌ Error: {e}")

# Footer
st.markdown("<div class='footer'>Created with ❤️ by Noor Hassan | Powered by Gemini API & Streamlit</div>", unsafe_allow_html=True)
