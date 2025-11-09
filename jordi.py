"""
JORDI 2.0 — Voice + Text Hybrid AI Assistant 🤖
Works with both voice and text input seamlessly.
Author: Aditya Kharde
"""

import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import speech_recognition as sr
import os
import sys

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"JORDI 🧠: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning Aditya!")
    elif 12 <= hour < 18:
        speak("Good afternoon Aditya!")
    else:
        speak("Good evening Aditya!")
    speak("I’m JORDI, your personal AI assistant. How can I help you today?")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("🔍 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"🧍‍♂️ You said: {query}")
    except Exception as e:
        speak("Sorry, I didn’t catch that. Please say that again or type your command.")
        return "none"
    return query.lower()

def take_command():
    try:
        query = listen_command()
        if query == "none" or len(query.strip()) == 0:
            query = input("🧍‍♂️ You (type): ").lower()
    except:
        query = input("🧍‍♂️ You (type): ").lower()
    return query

def run_jordi():
    greet_user()
    while True:
        query = take_command()

        # Basic greetings
        if 'hello' in query or 'hi' in query:
            speak("Hello Aditya! What would you like me to do?")

        # Time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        # Open YouTube
        elif 'open youtube' in query:
            speak("Opening YouTube for you.")
            webbrowser.open("https://www.youtube.com")

        # Open Google
        elif 'open google' in query:
            speak("Opening Google for you.")
            webbrowser.open("https://www.google.com")

        # Play song or video
        elif 'play' in query:
            song = query.replace('play', '')
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        # Wikipedia search
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("Sorry, I couldn’t find any result for that.")

        # Open clock / time settings
        elif 'clock' in query:
            speak("Opening system time and date settings.")
            os.system("timedate.cpl")

        # Open notepad
        elif 'open notepad' in query:
            speak("Opening Notepad for you.")
            os.system("notepad")

        # Quit
        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye Aditya! Have a productive day ahead.")
            sys.exit()

        # Unknown command
        else:
            speak("Sorry, I didn’t understand that. Please repeat or try typing it.")

# Run Jordi
if __name__ == "__main__":
    run_jordi()
