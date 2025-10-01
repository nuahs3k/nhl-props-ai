# scripts/scrape_news.py
import requests
import pandas as pd

NEWS_API_KEY = "25f940562b944e77a2724eb8d60bb812"

def get_injury_news():
    url = f"https://newsapi.org/v2/everything?q=NHL+injury&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    news_list = []
    for article in articles:
        news_list.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url")
        })
    return pd.DataFrame(news_list)
