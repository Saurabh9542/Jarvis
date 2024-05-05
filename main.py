import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time

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
            print("Cound not hear you. Can you please repeat")
            speechToText()


def textToSpeech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    engine.say(x)
    engine.runAndWait()


# speak = speechToText()
# textToSpeech(speak)

if __name__ == "__main__":

    if speechToText().lower() == "jarvis activate":
        textToSpeech("Jarvis is activated...")
        while True:
            data = speechToText().lower()
            if "your name" in data:
                name = "My name is Jarvis"
                textToSpeech(name)
            
            elif "old are you" in data:
                age = "I am 5 years old"
                textToSpeech(age)
            
            elif "time is it" in data:
                time = datetime.datetime.now().strftime("%I%M%P")
                textToSpeech(time)
            
            elif "open youtube" in data:
                webbrowser.open("https://www.youtube.com/")

            elif "open linkedin" in data:
                webbrowser.open("https://www.linkedin.com/in/saurabh22")

            elif "open github" in data:
                webbrowser.open("https://www.github.com/saurabh9542")

            elif 'joke' in data:
                jokes = pyjokes.get_joke(language='en', category="all")
                textToSpeech(jokes)

            elif "deactivate" in data:
                textToSpeech('Thank you')
                break

            time.sleep(3)
    else:
        print("Thanks")
