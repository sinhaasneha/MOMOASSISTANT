import tkinter as tk
import threading
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

recognizer = sr.Recognizer()
running = False

# Speak
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Listen
def listen():
    with sr.Microphone() as source:
        status_label.config(text="🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-IN")
        return command.lower()
    except:
        return ""

# Brain
def brain(command):
    if "hey momo" not in command:
        return

    command = command.replace("hey momo", "").strip()

    if "stop" in command:
        speak("Goodbye Sneha")
        os._exit(0)

    elif "hello" in command:
        speak("Hello Sneha")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    else:
        speak("Sorry, I did not understand")

# Assistant loop
def run_momo():
    global running
    running = True
    speak("Momo is ready")
    status_label.config(text="🟢 Momo Active")

    while running:
        command = listen()
        brain(command)

# Start button
def start_momo():
    thread = threading.Thread(target=run_momo)
    thread.daemon = True
    thread.start()

# GUI
app = tk.Tk()
app.title("MOMO Voice Assistant")
app.geometry("350x200")
app.resizable(False, False)

title = tk.Label(app, text="🤖 MOMO", font=("Arial", 20))
title.pack(pady=10)

status_label = tk.Label(app, text="🔴 Momo Sleeping", font=("Arial", 12))
status_label.pack(pady=10)

start_btn = tk.Button(app, text="Start MOMO", font=("Arial", 12), command=start_momo)
start_btn.pack(pady=10)

app.mainloop()
