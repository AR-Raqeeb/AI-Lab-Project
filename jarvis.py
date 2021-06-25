import speech_recognition as sr # this package will recognize the voice command
import pyttsx3 # this package will convert text-to-speech
import pywhatkit # this package can search and play videos on youtube following the voice command
import datetime
import wikipedia
import requests, json , sys
import pyjokes

listener = sr.Recognizer() # creating a speech recognizer to recognize the voice of the user
engine = pyttsx3.init() # initializing the text-to-speech engine

def talk(text):
    engine.say(text)
    engine.runAndWait()

def weather(city): #weather used openweathermap api take city name as input
    # API key
    api_key = "e109b74f2efd786c4194d0efb32c9211"
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # city name
    city_name = city

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        return str(current_temperature)

def take_command():
    try:
        with sr.Microphone() as source: # declaring the Microphone as source
            print('Say Something...') # user can start giving command when they see this line
            voice = listener.listen(source) # calling the speech recognizer to listen to the source
            command = listener.recognize_google(voice) # using google API to convert the audio into text
            command = command.lower() # keeping the command in lowercase
        if 'jarvis' in command: # this block will run if the command contains the word "jarvis"
            command = command.replace('jarvis', '') # we are replacing the word jarvis with an empty string so that it doesn't show up in the command
            print(command) # the text we got from google API converter will be printed so we can check whether jarvis got the right command or not

    except: # if the command doesn't include the word "jarvis", then this block will run
        pass # we are going to ignore this block
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        ytvideo = command.replace('play', '')
        talk('playing' + ytvideo)
        pywhatkit.playonyt(ytvideo)


    if 'time' in command: #speck date & time
            time  = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)

    elif 'tell me about' in command: #read from wikipedia used wikipedia library
            look_for = command.replace('tell me about', '')
            info = wikipedia.summary(look_for, 1)
            print(info)
            talk(info)

    elif 'weather' in command: #weather In location
            weather_api = weather('Sylhet') #pass city name in weather api function
            talk(weather_api + 'degree fahreneit')

    elif 'joke' in command:  # tell jokes used pyjokes library
        talk(pyjokes.get_joke())

    else:
        talk('I did not get it but I am going to search it for you') #search at google used pywhatkit library
        pywhatkit.search(command)

while True:     #run alexa continuously -> take command from user one after another
    run_jarvis()