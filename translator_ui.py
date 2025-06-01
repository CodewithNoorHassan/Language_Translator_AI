import streamlit as st
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    st.error("❌ GEMINI_API_KEY is not set.")
    st.stop()

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

# Languages with emojis for flair
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

st.set_page_config(page_title="🌍 Multilingual Translator", page_icon="🌐", layout="wide")

# --- Header ---
st.markdown("""
    <style>
    .header {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #00b4d8;
        text-align: center;
        padding: 15px 0;
        font-weight: 700;
        font-size: 3rem;
        letter-spacing: 3px;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="header">🌍 Multilingual Translator</div>', unsafe_allow_html=True)

# --- Sidebar for language selection ---
with st.sidebar:
    st.header("⚙️ Settings")
    from_lang = st.selectbox(
        "Translate from:",
        options=list(language_options.keys()),
        index=0,
        format_func=lambda x: f"{language_options[x]}  {x}"
    )
    to_langs = st.multiselect(
        "Translate to:",
        options=[lang for lang in language_options.keys() if lang != from_lang],
        default=["Urdu", "French", "Spanish"],
        format_func=lambda x: f"{language_options[x]}  {x}"
    )

# --- Input Section ---
st.markdown("---")
st.markdown("### ✍️ Enter Text to Translate")
text = st.text_area(f"Type your text in {language_options[from_lang]} {from_lang} here...", height=160)

# --- Translation card UI ---
def translation_card(lang, text):
    return f"""
    <div style='
        background: #caf0f8;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        font-size: 1.1rem;
        font-weight: 600;
        color: #03045e;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    '>
        <span style='font-size: 1.4rem;'>{language_options.get(lang,"🌐")} <strong>{lang}:</strong></span><br>{text}
    </div>
    """

async def get_translation(user_input, from_language, target_languages):
    instructions = f"""
    You are a translation agent. Translate the following text from {from_language} into the languages:
    {', '.join(target_languages)}.
    
    Return translations clearly labeled like:
    Urdu: ...
    French: ...
    """
    agent = Agent(
        name="Multilingual Translator Agent",
        instructions=instructions
    )
    return await Runner.run(
        agent,
        input=user_input,
        run_config=config
    )

# --- Button & Translation Display ---
if st.button("🔁 Translate", use_container_width=True):
    if not text.strip():
        st.warning("⚠️ Please enter some text to translate!")
    elif not to_langs:
        st.warning("⚠️ Please select at least one target language!")
    else:
        with st.spinner("⏳ Translating..."):
            try:
                response = asyncio.run(get_translation(text, from_lang, to_langs))
                st.success("✅ Translation completed!")
                translations = response.final_output.split("\n")
                for line in translations:
                    if ":" in line:
                        lang_label, trans_text = line.split(":", 1)
                        st.markdown(translation_card(lang_label.strip(), trans_text.strip()), unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error during translation: {e}")

# --- Footer ---
st.markdown("---")
st.markdown("<center><small>Created with ❤️ by Noor Hassan | Powered by Gemini API & Streamlit</small></center>", unsafe_allow_html=True)
