import pyttsx3
import speech_recognition  as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        talk("Good Morning Rahul sir! Please tell me how may I help you")
    elif hour >= 12 and hour < 18:
        talk(" hello sir Good Afternoon, get up be active , here i am")
    else:
        talk("Good evening sir...My name is jarvis and i am here for you")

def takecommand():
    r = sr.Recognizer()
    with sr .Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 700
        audio = r.listen(source)

    try:
        print("Recognising..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        # print(e)

        print("say that again please")
        return "None"

    return query

if __name__ == '__main__':
    wishme()
    while True:
        query =takecommand().lower()
        if 'wikipedia' in query:
            talk("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            talk("according to wikipedia")
            print(results)
            talk(results)

        elif 'remember' in query:
            with open('remember.txt', 'a') as f:
                query = query.replace('remember', '')
                f.write(query)
                talk("ok sir i will remember")

        elif 'what i told you' in query:
            with open('remember.txt','r') as f:
                data = f.read()
                talk(f"sir you told me {data}")



        elif "open youtube" in query:
            talk("ok sir opening")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            appPath2 = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            talk("sure sir here it is")
            os.startfile(appPath2)

        elif "play music" in query:
            music_dir = 'D:\\backup 2020\\songs\\New folder'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            talk(f"sir the time is {strTime}")

        elif "open microsoft edge" in query:
            appPath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            talk("ok sir opening")
            os.startfile(appPath)

        elif "ok bye" in query or "stop" in query:
            talk("ok bye  rahul sir take care")
            break

        elif " youtube" in query:
            song = query.replace("play on youtube", "")
            talk("ok sir ")
            talk('playing' + song)
            pywhatkit.playonyt(song)

        elif "eat" in query:
            talk("hmmmm i eat lots and lots of data haha by the way what do you eat") or talk("i eat much electricity")

        elif "what can you do for me" in query:
            talk("sir i can can play a song for you, i can open websites for you even i can search on wikipedia for you sir,"
                 "i can also send email dor you but it is risky at a moment sir")

        elif "who are you" in query:
            talk("Hello sir my name is Jarvis,Mr rahul shankar more has coded me in python, I am your desktop assistant, in short i am your desktop bot")

        elif "good morning" in query:
            talk(" Good Morning sir, Another day, loads of opportunities to fulfill your dreams. I wish you a very cheerful and energetic good morning. Have a great day ahead")

        elif "don't leave me buddy" in query:
            talk("never ever sir.... i never gonna leave you")

        elif "open any desk" in query:
            appPath1 = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
            talk("ok sir opening")
            os.startfile(appPath1)

        elif "what are you doing" in query:
            talk("Nothing sir I am just waving around your computer")

        elif "what should i do for you" in  query:
            talk("you dont need to do anything sir i am here to do ")

        elif "sing" in query:
            talk("sorry sir i think you dont added that thing till now in me, but i would like to sing so sir can you please add that feature in me")

        elif "thank you" in  query:
            talk("my pleasure sir")

        elif "to do " in query:
            talk("sorry sir you didi not tell me what is the program")

        elif "water" in query:
            talk("Yes sir , so talking about water, whatever we can say about water is not enough, shortly just I can say water is a life")

        elif "git" in query:
            talk("Git is a version control system")

        elif "sourcetree" in query:
            talk("sourcetree is source control sysytem from where we can control our file transfer to remote repositery")

        elif "one plus bullets" in query:
            talk(" one plus bullets are blutooth earphones costs around 2000 rupees")

        elif "pen" in query:
            talk("pen is an writing instrument")

