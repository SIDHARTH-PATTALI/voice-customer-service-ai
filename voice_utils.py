import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

def speak(text):
    """Speak the text out loud"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user's voice and return recognized text"""
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            question = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {question}")
            return question
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            speak("Speech recognition is not available.")
            return None
