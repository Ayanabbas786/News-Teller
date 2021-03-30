import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    news = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=b24ad1abb76f4932b3f75e87ce208487")
    news_converted = json.loads(news.text)
    speak("Hello, and welcome to News Teller.")
    play = input("Press enter to listen to today's headlines: ")
    speak("Okay, here are todays top ten headlines")
    print()
    for i in range(10):
        headline = news_converted["articles"][i]["title"]
        print(f"{i + 1}. {headline}")
        if i == 0:
            speak(f"The first news for today is, {headline}")
        else:
            speak(f"The next news is, {headline}")

speak("That's all for today's headlines! Will see you tomorrow with some new headlines")
