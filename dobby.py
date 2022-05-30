import datetime
from re import sub
from time import time
from tkinter import E
from pip import main
import pyttsx3 #pip install pyttsx3
import pyjokes
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipvedia
import webbrowser
import os
import smtplib
import subprocess
from urllib.request import urlopen
import json
from googletrans import Translator #pip install googletrans==3.1.0a0

#pip install pipwin
#pipwin install pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#two voices availble in this api one male-David (voices[0].id) and other female-Zira (voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Dobby, your assistant. Please tell me what I can do for you")

def takeCommand():
    #it takes microphone input from user and returns strring output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        # press control on the function to view its full code
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sara.ahmed1447@gmail.com','IshratSaraAlvi@120506')
    server.sendmail('sara.ahmed1447@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\Sara\\python\\project\\Ok Dobby\\Song'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'date today' in query:
            strTime = datetime.datetime.now().strftime("%Y:%m:%d")
            print(strTime)
            speak(f"Today is {strTime}")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\saraa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'email to sara' in query:
            try :
                speak("what should I say?")
                content = takeCommand()
                to = "sara.ahmed2595@gmail.com"
                sendEmail(to, content)
                speak("Email sent")
                print("Email sent")
            except Exception as e:
                print(e)
                speak("Sorry, Unable to send mail at the moment")
        
        elif 'send a mail' in query or 'send an email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("To whom should I send this mail?")
                to = input()
                sendEmail(to, content)
                speak("Email sent!")
            except Exception as e:
                print(e)
                speak("Sorry, Unable to send mail at the moment")

        elif 'how are you' in query:
            speak("I am fine, thank you")
            speak("How are you?")
        
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'exit' in query:
            speak("Thank you for giving your time")
            exit()
        
        elif 'who created you' in query:
            speak("I was created by Sara")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Sara")
 
        elif 'why were you created' in query:
            speak("I was created as a Mini project by Sara Ahmed")
        
        elif 'write a note' in query:
            speak("What should I write in the note?")
            note = takeCommand()
            file = open('dobby.txt', 'w')
            speak("Should I include the date and time")
            dnt = takeCommand()
            if 'yes' in dnt or 'sure' in dnt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write('\n')
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing text in note")
            file = open('dobby.txt','r')
            print(file.read())
            speak(file.read(6))

        elif 'hibernate' in query:
            speak('Hibernating')
            subprocess.call('shutdown /h ')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("Locating")
            speak(query)
            webbrowser.open("http://www.google.com/maps/place/" + location + "")

        elif 'news' in query:
            try:
                url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=e8fa36a9bcfa4040bca494fd5bf3fa8b')
  
                jsonObj = urlopen(url)
                data = json.load(jsonObj)
                i = 1
                speak('The latest updates are')
                for item in data['articles']:
                    print(str(i) + '.' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + item['title'] + '\n')
                    i += 1
                    if i == 6:
                        exit()

            except Exception as e:
                print(str(e))

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "translate english to hindi" in query:
            # print(googletrans.LANGCODES) 
            
            try :
                speak("What do you wish to translate?")
                english = takeCommand()
                print(english)             
                translator = Translator()
                result = translator.translate(english, src='en', dest='hi')
                print("Translating...")
                print(result.text)
                print(result.pronunciation)
                
            
            except Exception as e:
                print(e)

        elif "translate hindi to english" in query:
            # print(googletrans.LANGCODES) 
            
            try :
                speak("What do you wish to translate?")
                hindi = takeCommand()
                print(hindi)             
                translator = Translator()
                result = translator.translate(hindi, src='hi', dest='en')
                print("Translating...")
                print(result.text)
                speak(result.text)
                
            
            except Exception as e:
                print(e)
