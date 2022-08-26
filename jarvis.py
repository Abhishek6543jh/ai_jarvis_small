import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def whatsappmsg():
    speak("please fill the below details")
    number = input("\nEnter The number of recepient\n")
    msg = input("\nEnter the message here\n")
    hor= int(datetime.datetime.now().strftime("%H"))
    min= int(datetime.datetime.now().strftime("%M"))
    mmin = min + 1
    speak("please wait for  sometime to delever the msg")
    pywhatkit.sendwhatmsg(f'+91{number}' , msg ,hor,mmin)
     

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        engine.say("good morning,  Abhishek") 
    elif hour >=12 and hour <= 18:
        engine.say("good afternoon, Abhishek") 
        
    else :
        speak("good evening , Abhishek")


#takes microphone input from user and returns string output
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query = r.recognize_google(audio , language= "en-in")
        print("user said : \n\n" , query )

    except Exception as e :
        print ("say that again")
        return "none"
    return query
    
    
if __name__== "__main__":
    wishme()
    speak('i am jarvis , How may i help you boss')
    while True:
        query = command().lower()
        #LOGIC FOR XECECUTING TASKS BASED ON QUERY
        if "wikipedia" in query:
            speak( "searching wikipedia ....")
            query = query.replace("wikipedia", "")
            results =wikipedia.summary(query, sentences=4)
            speak("acording to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" or "open the youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open google" in query:
            webbrowser.open("www.google.com")
        elif "play music" in query:
            songs_dir = "C:\\Users\\kalth\\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir , songs[0]))
        elif "time" in query:
            thetime = datetime.datetime.now().strftime("%H:%M:%S")
            print(thetime)
            speak(f"\n\nthe time is {thetime}")
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")