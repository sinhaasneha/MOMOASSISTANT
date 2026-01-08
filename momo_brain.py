import datetime
import webbrowser
from momo_speak import speak

def brain(command):
    if "hello" in command:
        speak("Hello Sneha, I am Momo")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "who are you" in command:
        speak("I am Momo, your personal voice assistant")

    elif "stop" in command or "exit" in command:
        speak("Goodbye Sneha")
        return False   # 🔴 STOP SIGNAL

    else:
        speak("Sorry, I don't understand yet")

    return True        # 🟢 KEEP RUNNING
