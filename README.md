# 🌍 Multilingual Translator AI

A powerful AI-powered translation application built with **Streamlit** and **Google's Gemini API**. Translate text into multiple languages with a beautiful, user-friendly interface.

## ✨ Features

- 🌐 Translate into **13+ languages** including Urdu, French, Spanish, Chinese, German, Arabic, Hindi, Turkish, Italian, Japanese, Russian, and Korean
- 🎨 Modern, responsive UI with emoji flair
- ⚡ Real-time translation powered by Gemini 2.0 Flash
- 📱 Mobile-friendly interface
- 🔒 Secure API key management

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- Google Gemini API Key

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Language_Translator_AI
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your API Key**
   - Copy `.env.example` to `.env`
     ```bash
     copy .env.example .env
     ```
   - Get your Gemini API Key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Paste it in `.env`:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

## 🎯 Usage

### Run the Streamlit App

```bash
streamlit run translator_ui.py
```

The app will open in your browser at `http://localhost:8501`

### Or Run CLI Version

```bash
python main.py
```

## 📁 Project Structure

```
Language_Translator_AI/
├── .env                 # API keys (DO NOT COMMIT - in .gitignore)
├── .env.example         # Template for .env (safe to commit)
├── .gitignore           # Git ignore rules
├── main.py              # CLI version of translator
├── translator_ui.py     # Streamlit web interface
└── requirements.txt     # Python dependencies
```

## 🔒 Security Notes

- **Never commit `.env` file** - It contains your API key
- The `.env` file is included in `.gitignore`
- Use `.env.example` as a template
- Keep your API key secret and rotate it if exposed

## 🛠️ Technologies Used

- **Frontend:** Streamlit
- **AI Model:** Google Gemini 2.0 Flash
- **API:** Google Generative AI
- **Language:** Python 3.13

## 📄 Requirements

See `requirements.txt` for all dependencies:
- streamlit
- google-generativeai
- python-dotenv
- httpx
- pydantic

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Noor Hassan**

---

Made with ❤️ | Powered by Gemini API & Streamlit
