import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Momo is listening... Speak now")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except:
    print("Sorry, Momo could not understand you")
