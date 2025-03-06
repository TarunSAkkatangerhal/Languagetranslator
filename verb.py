import streamlit as st
from googletrans import Translator, LANGUAGES
import speech_recognition as sr

# Initialize translator
translator = Translator()
recognizer = sr.Recognizer()

# Streamlit UI
st.title("LingoBridge - NGO Language Translator 🌍")
st.write("Translate text and speech for multilingual communication.")

# Language selection
languages = list(LANGUAGES.values())
src_lang = st.selectbox("Select Source Language", languages, index=languages.index("english"))
dest_lang = st.selectbox("Select Target Language", languages, index=languages.index("french"))

# Reverse lookup for language codes
src_lang_code = [k for k, v in LANGUAGES.items() if v == src_lang][0]
dest_lang_code = [k for k, v in LANGUAGES.items() if v == dest_lang][0]

# Text Translation
st.subheader("Text Translation")
text_input = st.text_area("Enter text to translate:")
if st.button("Translate"):
    if text_input:
        translated_text = translator.translate(text_input, src=src_lang_code, dest=dest_lang_code).text
        st.success(f"*Translated Text:* {translated_text}")

# Speech-to-Text Translation
st.subheader("Speech-to-Text Translation")
with st.expander("Record Your Voice"):
    st.write("Click below to start recording.")
    if st.button("Start Recording"):
        with sr.Microphone() as source:
            st.info("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5)
                speech_text = recognizer.recognize_google(audio, language=src_lang_code)
                translated_speech = translator.translate(speech_text, src=src_lang_code, dest=dest_lang_code).text
                st.success(f"*Recognized Speech:* {speech_text}")
                st.success(f"*Translated Speech:* {translated_speech}")
            except Exception as e:
                st.error("Could not recognize speech. Please try again.")

# NGO Phrasebook
st.subheader("NGO Phrasebook")
phrasebook = {
    "english": {"Help": "Help", "Where is the hospital?": "Where is the hospital?"},
    "french": {"Help": "Aide", "Where is the hospital?": "Où est l'hôpital?"},
    "spanish": {"Help": "Ayuda", "Where is the hospital?": "¿Dónde está el hospital?"}
}
if st.checkbox("Show Common NGO Phrases"):
    st.write(phrasebook.get(dest_lang, "No phrases available for this language."))
