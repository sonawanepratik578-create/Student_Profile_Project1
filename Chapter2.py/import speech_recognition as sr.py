import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# Initialize engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1)

# Set voice (Windows fix)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print("Robot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="hi-IN")
        print("You:", command)
        return command.lower()
    except:
        return ""

# Greeting
speak("Namaste! Main aapka smart robot hoon. Aap kya karna chahte hain?")

while True:
    command = listen()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("Abhi samay hai " + time)

    elif "google" in command:
        speak("Google khol raha hoon")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("YouTube khol raha hoon")
        webbrowser.open("https://www.youtube.com")

    elif "wikipedia" in command:
        speak("Kis topic ke baare mein?")
        topic = listen()
        try:
            info = wikipedia.summary(topic, sentences=2)
            speak(info)
        except:
            speak("Mujhe information nahi mili")

    elif "band karo" in command or "exit" in command:
        speak("Thik hai, milte hain!")
        break

    elif command != "":
        speak("Aapne kaha " + command)