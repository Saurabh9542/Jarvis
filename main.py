import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def speechToText():
    recoginizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recoginizer.adjust_for_ambient_noise(source)
        audio = recoginizer.listen(source)
        try:
            print("Recogonizing...")
            data = recoginizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Cound not hear you.")


def textToSpeech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 100)
    engine.say(x)
    engine.runAndWait()


# speak = speechToText()
# textToSpeech(speak)

if __name__ == "__main__":

    if speechToText().lower() == "jarvis activate":
        print("test")



# print(dir(pyttsx3))