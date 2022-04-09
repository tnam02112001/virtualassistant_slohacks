# Imports
import pyttsx3  # converts text to speech
import datetime  # required to resolve any query regarding date and time
# required to return a string output by taking microphone input from the user
import speech_recognition as sr
import wikipedia  # required to resolve any query regarding wikipedia
import webbrowser  # required to open the prompted application in web browser
import requests
from GoogleNews import GoogleNews


# Global variables
engine = pyttsx3.init()  # Initilaize text-to-speech engine
googlenews = GoogleNews()  # Initlize Gooogle News Engine

# Global CONSTANTS
# For opening Youtube Link
YOUTUBE_LINK = "https://www.youtube.com/watch?v=8pm_KoguqPM"
SLO_CORD = ["35.2913508", "-120.6618469"]  # [lat, lon] of SLO, for Weather API
WEATHER_API_KEY = "d1032fab5119ba55d9fe5f5cab2967f0"  # Weather API Key


def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={SLO_CORD[0]}&lon={SLO_CORD[1]}&appid={WEATHER_API_KEY}"
    response = requests.get(url)
    print(response.content)
    response = response.json()
    name = response["name"]
    weather_des = response["weather"][0]["description"]
    temp = response["main"]["temp"]
    temp = (temp - 273.15) * 9 / 5 + 32
    temp = str(round(temp, 2))

    weather_return = f"The weather in {name} is {weather_des} with the temperature of {temp} fahrenheit"

    return weather_return


def speak(audio):  # function for assistant to speak
    engine.say(audio)
    engine.runAndWait()  # without this command, the assistant won't be audible to us


def welcome():  # function to wish the user according to the daytime
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak(
        "Hello Sir, I am Friday, your Artificial intelligence assistant. Please tell me how may I help you"
    )


def takecommand():  # function to take an audio input from the user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(
            source
        )  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio = r.listen(source)
        try:                                            # error handling
            print('Recognizing...')
            # using google for voice recognition
            query = r.recognize_google(audio, language='en-in')
            print(f'User said: {query}\n')

        except Exception as e:
            # 'say that again' will be printed in case of improper voice
            print('Say that again please...')
            return 'None'
    return query


if __name__ == "__main__":  # execution control
    welcome()

    while True:
        query = takecommand().lower()  # converts user asked query into lower case

        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.get().open_new(YOUTUBE_LINK)

        elif "google " in query:
            speak("Searching Google....")
            query = query.replace("google", "")
            googlenews.search(query)
            results = googlenews.get_texts()[:3]
            print(results)

            for each in results:
                speak(each)

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")

        elif "weather" in query:
            weather_des = get_weather()
            speak(weather_des)

        elif "bye" in query:
            speak("okay boss, please call me when you need me")
            quit()
