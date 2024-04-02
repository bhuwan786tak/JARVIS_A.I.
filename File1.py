import pyttsx3
import speech_recognition
import requests
import bs4
from bs4 import BeautifulSoup
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio: object) -> object:
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from Greetme import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("OK sir, You can call me anytime again")
                    break

                # Basic commands (Greetings)

                elif 'hello' in query:
                    speak("Hello Sir, How are you ?")
                elif "I am Fine" in query:
                    speak("That's great Sir")
                elif 'how are you' in query:
                    speak("Perfect Sir, Thank you for asking")
                elif 'Thankyou' in query:
                    speak("Your Welcome, Sir")
                elif 'Hi Jarvis' in query:
                    speak("Hello, Sir")
                elif 'thankyou' in query:
                    speak("Your Welcome, Sir")

                # Commands for opening and closing apps

                elif "open" in query:
                    from DictionaryOfApps import openappweb
                    openappweb(query)
                elif "close" in query:
                    from DictionaryOfApps import closeappweb
                    closeappweb(query)

                # commands for searching on google, youtube, wiki

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                # Commands for Temperature or Weather

                elif "temperature" in query:
                    search = "temperature"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")


                elif "set an alarm" in query:
                    print("input time example: 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time:  ")
                    alarm(a)
                    speak("Done, Sir")

                # Command for Time

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is{strTime}")

                # Command to exit code and stop

                elif "Finally Sleep" in query:
                    speak("Going to sleep, sir")
                    exit()


