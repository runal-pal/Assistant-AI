import pyttsx3 as pv
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as web
import os
import smtplib
import random

engine = pv.init('sapi5')
voices = engine.getProperty('voices')
# To check which voices are available in the id
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# It is a speak function of the code
def speak(audio):
    ''' It a function which speak according to the input is given'''
    engine.say(audio)
    engine.runAndWait()


# It is a wishing function
def wishMe():
    """ It is a function to wish you according to the time """

    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        print("Robin : Good Morning !")
        speak("Good Morning Runal Sir")

    elif hour >= 12 and hour < 18:
        print("Robin : Good Afternoon !")
        speak("Good Afternoon Runal Sir")

    elif 1 <= hour < 6:
        print("Robin : Good Evening !")
        speak("Good Evening. Hello Sir, are you still awake")

    else:
        print("Robin : Good Evening")
        speak("Good Evening Sir")

    # print("I am Robin.")
    speak("I am Robin. Please tell me How may i help you ?")



def takeCommand():
    """It is a function it takes microphone input from the user and
    returns string output """

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening . . .")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing . . .")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"

    return query


def sendEmail(to, content):
    """ This function will send email to the person """
    server = smtplib.SMTP("smtp.gmail.com", 587) # To give access
    server.ehlo()
    server.starttls()
    server.login('jerrymail.email@gmail.com', 'something.') # Here will be your email id and passwd
    server.sendmail('jerrymail.email@gmail.com', to , content) # It will send your email
    server.close()


if __name__ == "__main__":
    # speak("Runal is a Smart Elf")
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:

            print("Searching Wikipedia .. . .")
            speak("Searching Wikipedia . . .")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            # Here inbuilt webbrowser module is used
            # speak("Opening youtube please wait.")
            web.open("www.youtube.com")

        elif 'open google' in query:
            # speak("Opening Google for search. Please wait.")
            web.open("www.google.com")

        elif 'open stackoverflow' in query:
            # speak("Opening Stack over flow")
            web.open("www.stackoverflow.com")

        elif 'open amazon' in query:
            web.open("www.amazon.in")

        elif 'play music' in query:
            # Using the model os to change the directory and play music there

            music_dir = 'C:\\Users\\Dragonor\\Desktop\\AssistantAI\\Music'  # Insert path to the directory here
            songs_list = os.listdir(music_dir)  # List the files in the directory
            # you can also use detect mp3
            songs = random.choice(songs_list)
            print(songs)
            os.startfile(os.path.join(music_dir, songs))  # os.path will open the file and path.join will join both
            # the files music_dir to song[0] that means play 0th position song
            # You can also use random module
            # and can 0 to length of song generate random numbers choices

        elif 'time please' in query:
            # To speak for the time right now
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = '"C:\\Users\\Dragonor\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            # Here inser the path for the Vs code
            os.startfile(codePath) # To open the file

        elif 'email to runal' in query:  # You can also create dictionary in the starting key is name and value is email
            try:
                # print("What should I say ?")
                speak("What should I say . . . ")
                content = takeCommand() # Whatever you say it will return it as a string
                to = "runal.p2@gmail.com"
                sendEmail(to, content)
                # print("Your Email has been sent")
                speak("Your Email has been sent")

            except Exception as e:
                print(e)
                print("Sorry Sir")
                speak("Sorry Sir. I am not able to send this email.")

        elif 'who are you' in query:
            print("I am Robin. And I want Love !")
            speak("Hello I am Robin. I am in under development a partial Artificial Intelligence"
                  "Created by Mr. Runal Pal. I am able to perform various "
                  "tasks.")

        elif 'how are you' in query:
            # print("Operational Sir")
            speak("I am Operational Sir. Thank you for asking !")

        elif 'what can you do' in query:
            speak(" Well I am able to perform tasks such as scraping, searching, automating and helping"
                  "humans. I can do what i learn and programmed by my master. ")

        elif 'i love you' in query:
            speak(" I cannot answer to this sir. I am not a human. but You are the best !")

        elif 'do you love me' in query:
            speak(" If only i could have Emotions Sir.")

        elif 'robin quit' in query:
            print("Have a Great day! Runal Sir. ")
            speak("Quitting Right Now, Meet you soon!")
            break
