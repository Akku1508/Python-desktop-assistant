import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os;

engine=pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty('voice',voices[0])
#print(voices[0])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning ma'am !!")
    elif hour>=12 and hour<18:
        speak("Good afternoon ma'am!!")
    else:
        speak("Good evening ma'am !!")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio,Language="en-in")
        print(f"User said:{query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query



takeCommand()
if __name__=="__main__":
    wishMe()
    if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2) 
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'play music' in query:
        music_dir = ""
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'open code' in query:
        codePath = ""
        os.startfile(codePath)


