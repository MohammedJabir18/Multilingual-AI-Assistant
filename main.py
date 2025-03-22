import os
import logging
import speech_recognition as sr
from gtts import gTTS
import re
import google.generativeai as genai
import streamlit as st


# Logging function
def log_info(msg):
    DIR_LOC = "Logs"
    FILE_NAME = "Application.log"

    os.makedirs(DIR_LOC, exist_ok=True)
    path = os.path.join(DIR_LOC, FILE_NAME)

    logging.basicConfig(
        filename=path,
        format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
        datefmt="%d-%m-%Y %I:%M:%S %p"
    )
    logging.info(msg)


# Speech recognition function
def takeCommand():
    r = sr.Recognizer()

    # List of supported languages
    languages = {
        "English": "en-IN",
        "Hindi": "hi-IN",
        "Malayalam": "ml-IN",
        "Tamil": "ta-IN"
    }

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        for lang, code in languages.items():
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language=code)
                print(f"You said: {query}")
                return query
            except sr.UnknownValueError:
                print(f"Could not understand {lang}")
            except sr.RequestError:
                print("Google Speech Recognition API unavailable")
        
        return "Sorry! I did not catch that."

    except Exception as e:
        return "Microphone is not available. Please use text input."
 

# Text-to-speech function
def text_to_speech(text):
    print(text)
    print("Converting to audio file...")
    # Preprocess text to remove special characters
    sanitized_text = re.sub(r'[\*#@!%^&*()<>?/|}{~:]', "", text)

    try:
        tts = gTTS(text=sanitized_text, lang="en")
        tts.save("output.mp3")
    except Exception as e:
        log_info(f"Error in TTS for language: {str(e)}")


# Gemini AI Model function
def gemini_model(user_input):
    # Configure API key
    genai.configure(api_key="AIzaSyBoH0fpSEQQtl8LKcTpn6kzA_R7w7UJ5Z4")  # Replace with valid API key
    
    try:
        print("Generating response...")
        model = genai.GenerativeModel("gemini-1.5-pro-001")
        response = model.generate_content(user_input)
        return response.text

    except Exception as e:
        log_info(str(e))
        return "Check you internet connectivity"
    

# Main function
def main():
    log_info("Application Starting...")

     # Streamlit UI
    st.title("Multilingual AI Assistant")
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text = takeCommand()
            st.write(f"You said: {text}")
        
        with st.spinner("Generating response..."):
            result = gemini_model(text)
            st.write(result)

        with st.spinner("Converting to audio..."):
            text_to_speech(result)

        # Display audio player and download link
        with open("output.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()

        # st.text_area(label="Response:", value=result, height=350)
        st.audio(audio_bytes, format="audio/mp3")
        st.download_button(
            label="Download Result",
            data=audio_bytes, 
            file_name="output.mp3", 
            mime="audio/mp3"
        )
            

# Run main function
main()
