import pyttsx3  # converts text to speech
import datetime  # required to resolve any query regarding date and time
import speech_recognition as sr  # required to return a string output by taking microphone input from the user
import wikipedia  # required to resolve any query regarding wikipedia
import webbrowser  # required to open the prompted link in web browser
import requests
from GoogleNews import GoogleNews

# Global variables
# Global variables
engine = pyttsx3.init() # Initilaize text-to-speech engine
googlenews = GoogleNews() # Initlize Gooogle News Engine 

# Global CONSTANTS
YOUTUBE_LINK  = "https://www.youtube.com/watch?v=8pm_KoguqPM" # For opening Youtube Link
SLO_CORD = ["35.2913508", "-120.6618469"] # [lat, lon] of SLO, for Weather API
WEATHER_API_KEY = "d1032fab5119ba55d9fe5f5cab2967f0" # Weather API Key

   
if __name__ == "__main__":  # execution control
    pass
