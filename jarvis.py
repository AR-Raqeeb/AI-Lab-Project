import speech_recognition as sr # this package will recognize the voice command
import pyttsx3 # this package will convert text-to-speech
import pywhatkit # this package can search and play videos on youtube following the voice command
import datetime     # to know the current date and time
import wikipedia    # to explore wikipedia entries
import requests     # a library for making HTTP requests
import time
import webbrowser   # open any domain on the internet using browser


print('Loading your AI personal assistant - Jarvis')

engine=pyttsx3.init('sapi5')    # initializing the text-to-speech engine
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        talk("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        talk("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        talk("Hello,Good Evening")
        print("Hello,Good Evening")

def take_Command():
    r = sr.Recognizer()     # creating a speech recognizer to recognize the voice of the user
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"Command: {statement}\n")

        except Exception as e:
            talk("Pardon me, please say that again")
            return "None"
        return statement

talk("Loading your AI personal assistant Jarvis")
wishMe()


if __name__=='__main__':


    while True:
        talk("Tell me how can I help you now?")
        statement = take_Command().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            talk('your personal assistant Jarvis is shutting down,Good bye')
            print('your personal assistant Jarvis is shutting down,Good bye')
            break



        elif 'wikipedia' in statement:
            talk('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            talk("According to Wikipedia")
            print(results)
            talk(results)

        elif 'play' in statement:
            ytvideo = statement.replace('play', '')
            talk('playing' + ytvideo)
            pywhatkit.playonyt(ytvideo)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            talk("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            talk("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            talk("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            talk("whats the city name")
            city_name=take_Command()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                talk(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                talk(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            talk(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            talk('I am Jarvis, version 1 point O, your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail and stackoverflow , tell time, search wikipedia entries, tell weather' 
                  'in different cities , get top world news from the CNN and play any videos from youtube too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            talk("I was built by Raqeeb and Tahmid")
            print("I was built by Raqeeb and Tahmid")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            talk("Here is stack overflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://edition.cnn.com/world")
            talk('Here are some headlines from the CNN,Happy reading')
            time.sleep(10)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(6)


time.sleep(3)