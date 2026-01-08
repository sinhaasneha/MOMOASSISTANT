import speech_recognition as sr
import pyttsx3
import requests
import struct
import pyaudio
import pvporcupine
import time
import os

# ================== PICOVOICE ACCESS KEY ==================
ACCESS_KEY = "fkD6Pk6/fEwqxqdKIbM9p7HU+L4si8cQeqhUkf6onBIwYH0MEzuyVw=="

# ================== TTS ==================
engine = pyttsx3.init()
engine.setProperty("rate", 175)

def speak(text):
    print("Momo:", text)
    engine.say(text)
    engine.runAndWait()

# ================== SPEECH RECOGNITION ==================
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Momo is listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

# ================== BACKEND ==================
def send_to_backend(message):
    try:
        res = requests.post(
            "http://localhost:5000/api/momo",
            json={"message": message},
            timeout=5
        )
        return res.json().get("reply", "No reply from backend")
    except:
        return "Backend is not responding"

# ================== WAKE WORD ==================
def wake_word_listener():
    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=[os.path.join("wakewords", "hey-momo.ppn")]
    )

    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🟢 Say 'Hey Momo' to wake me up")

    try:
        while True:
            pcm = stream.read(
                porcupine.frame_length,
                exception_on_overflow=False
            )
            pcm = struct.unpack_from(
                "h" * porcupine.frame_length,
                pcm
            )

            if porcupine.process(pcm) >= 0:
                return
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()

# ================== MAIN ==================
print("Momo: Momo is ready")
speak("Momo is ready")

while True:
    # Wait for wake word
    wake_word_listener()

    speak("Yes Sneha")

    command = listen()
    if command == "":
        continue

    # STOP COMMAND
    if "stop" in command or "exit" in command:
        speak("Goodbye Sneha")
        break

    # NORMAL COMMAND
    reply = send_to_backend(command)
    speak(reply)

    time.sleep(0.5)
