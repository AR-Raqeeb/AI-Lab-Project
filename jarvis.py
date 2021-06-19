import speech_recognition as sr # this package will recognize the voice command
import pyttsx3 # this package will convert text-to-speech
import pywhatkit # this package can search and play videos on youtube following the voice command

listener = sr.Recognizer() # creating a speech recognizer to recognize the voice of the user
engine = pyttsx3.init() # initializing the text-to-speech engine

def talk(text):
    engine.say(text)
    engine.runAndWait()

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

run_jarvis()