
import json
import random
import speech_recognition as sr
import pyttsx3
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

# Speak out loud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen to microphone
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"🗣️ You: {text}")
        return text.lower()
    except:
        return ""

# Find matching intent
def predict_intent(user_input):
    tokens = word_tokenize(user_input)
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return intent
    return next(i for i in data["intents"] if i["tag"] == "unknown")

# Chatbot loop
def run_chatbot():
    speak("Dynamic Voice Chatbot activated. Say 'bye' to stop.")
    while True:
        user_input = listen()
        if not user_input:
            speak("Sorry, can you repeat that?")
            continue
        intent = predict_intent(user_input)
        response = random.choice(intent["responses"])
        speak(response)
        if intent["tag"] == "goodbye":
            break

if __name__ == "__main__":
    run_chatbot()
