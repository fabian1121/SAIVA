from newsapi import NewsApiClient 
from ListenFunction import speak


def news():
    api_key = "bf4199210b42494687db9a8ae712edf6"
    newsapi = NewsApiClient(api_key=api_key)
    data = newsapi.get_top_headlines(language='en', country='in', page_size=10)
    articles = data["articles"]

    speak("Here are the top headlines")
    print("==============TOP HEADLINES==============")

    for item in articles:
        speak(item['title'])
        print(item['description'])

    speak("That's all for the news updates")

news()