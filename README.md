# 🌍 Multilingual AI Assistant 🤖

<div align="center">
  <img src="/assets/ai.gif" alt="AI Assistant Demo" width="700px">

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
  ![Google AI](https://img.shields.io/badge/Google_AI-4285F4?style=for-the-badge&logo=google&logoColor=white)
  ![Speech Recognition](https://img.shields.io/badge/Speech_Recognition-512BD4?style=for-the-badge&logo=speechrecognition&logoColor=white)
  
  <p><i>A powerful AI assistant capable of understanding and responding in multiple languages</i></p>
</div>

## ✨ Features

- 🎤 **Voice Recognition** - Understands speech input in multiple languages (English, Hindi, Malayalam, Tamil)
- 🧠 **AI-Powered Responses** - Leverages Google's Gemini 1.5 Pro model for intelligent responses
- 🔊 **Text-to-Speech** - Converts AI responses to natural-sounding speech
- 📱 **Interactive UI** - Clean Streamlit interface for easy interaction
- 📝 **Logging System** - Comprehensive logging for troubleshooting and performance monitoring
- 💾 **Download Options** - Save audio responses for later use

## 🚀 Demo

<div align="center">
  <img src="/assets/demo.gif" alt="Application Demo" width="600px">
</div>

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/MohammedJabir18/Multilingual-AI-Assistant.git

# Navigate to project directory
cd Multilingual-AI-Assistant

# Install required packages
pip install -r requirements.txt

# Run the application
streamlit run main.py
```

## 📋 Requirements

- Python 3.8+
- SpeechRecognition
- gTTS (Google Text-to-Speech)
- Google Generative AI
- Streamlit
- Internet connection for API calls

## 💡 How It Works

<div align="center">
  <img src="/assets/architecture.png" alt="Architecture Diagram" width="700px">
</div>

1. 🎙️ **Voice Input**: The system captures your voice through a microphone
2. 🔍 **Speech Recognition**: Converts speech to text in multiple languages
3. 🧠 **AI Processing**: Sends the text to Gemini AI model for processing
4. 📝 **Response Generation**: Gemini AI generates a contextual response
5. 🔊 **Speech Synthesis**: Converts the text response to speech
6. 👂 **Audio Playback**: Plays the response through your speakers

## 🌐 Supported Languages

- 🇬🇧 English (en-IN)
- 🇮🇳 Hindi (hi-IN)
- 🇮🇳 Malayalam (ml-IN)
- 🇮🇳 Tamil (ta-IN)

## 📊 Project Structure

```
Multilingual-AI-Assistant/
├── main.py                # Main application code
├── requirements.txt       # Package dependencies
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
└── Logs/                  # Application logs directory
    └── Application.log    # Log file (created at runtime)
```

## ⚙️ Configuration

Before running the application, replace the placeholder API key in `main.py`:

```python
# Replace with your actual Gemini API key
genai.configure(api_key="YOUR_API_KEY_HERE")
```

You can obtain a Gemini API key from the [Google AI Studio](https://makersuite.google.com/app/apikey).

## 🔍 Usage Example

```python
# Import the necessary functions
from main import takeCommand, gemini_model, text_to_speech

# Capture voice input
user_query = takeCommand()

# Generate AI response
ai_response = gemini_model(user_query)

# Convert response to speech
text_to_speech(ai_response)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This repository is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.

## 👨‍💻 Author

<div align="center">
  <img src="/assets/author.png" alt="Developer" width="400px">
  
  **Mohammed Jabir**
  
  [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MohammedJabir18)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohammed--jabir)
  [![Portfolio](https://img.shields.io/badge/Portfolio-1DA1F2?style=for-the-badge&logo=vercel&logoColor=white)](https://jabir-portfolio.vercel.app)
  [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/mohammedjabir__)
  [![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mohammedjabir__/)
  
  📧 Email: jabirahmedz111@gmail.com
</div>

## 🔗 Related Projects

This project is a submodule of [The Complete Python Course](https://github.com/MohammedJabir18/The-Complete-Python-Course.git), located in:
- Chapter 10 - Best Practices and Coding Style/Mega Projects/Multilingual AI Assistant

## ✅ Acknowledgements

- [Google Generative AI](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS](https://pypi.org/project/gTTS/)