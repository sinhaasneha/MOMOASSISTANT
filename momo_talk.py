import speech_recognition as sr
import pyttsx3

# initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

with sr.Microphone() as source:
    print("Momo is listening...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)
    speak("You said " + command)
except:
    speak("Sorry, I could not understand")
