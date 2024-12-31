import speech_recognition as sr
import pyttsx3 
import webbrowser
import openai

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)  
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate                       #printing current voice rate
engine.setProperty('rate', 175)     

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-in')
            return query
        except Exception as e:
            return speak("Some Error Occured. Sorry from Ultron.")


if __name__ == "__main__":
    speak("Hello, myself Ultron")
    while True:
        print("Listening...")
        text = take_command()
        sites = [['youtube','https://www.youtube.com'], ['wikipedia', 'https://www.wikipedia.com'],['google','https://www.google.com'],['instagram', 'https://www.instagram.com']]
        try:
            if ('shut down') in text.lower():
                speak("Shutting down....")
                break
            for site in sites:
                if f"open {site[0]}".lower() in text.lower():
                    speak(f'opening {site[0]} sir...')
                    webbrowser.open(site[1])
        except Exception as e:
            continue

#Now the openai api is not free so we can't use it further and this project isn't very interesting so I am dropping it now.