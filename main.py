import datetime
import os
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")

    speak("I am EDITH sir, even  dead I am the hero")
    speak("  ")
    speak( "how may i help you sir ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        print(e)

        print("say that again please....")
        return"None"

    return query


if __name__ == '__main__':
    speak("hello")
    wishMe()

    while True:
        query = takeCommand().lower()
       #logic to execute task based on query

        if'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query , sentences=2)
            speak ("According to wikipedia")
            speak(results)
        

        elif'open youtube' in query :
             webbrowser.open("youtube.com")

        elif'open google' in query :
             webbrowser.open("google.com")

        elif'open github' in query :
             webbrowser.open("github.com")

        elif'open stack overflow' in query :
             webbrowser.open("stackoverflow.com")
              
        elif'open linkedin' in query :
             webbrowser.open("linkedin.com")

        elif'open drive' in query :
             webbrowser.open("drive.google.com")     

        elif'play music' in query:
            webbrowser.open("youtubemusic.com")
        
        elif'open python'in query:
            codePath = "C:\\Users\\muley\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
            os.startfile(codePath)
        
        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strTime}")

        elif'no thanks' in query:
            speak('thank you for using me sir . Have a good day !')
            sys.exit()

           
           
        speak ('Sir do you have any other job for me ?')    

