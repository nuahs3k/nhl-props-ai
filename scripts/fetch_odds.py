# scripts/fetch_odds.py
import requests
import pandas as pd

ODDS_API_KEY = "d8475e9d02d7bdd135300c54d7b6c116"

def fetch_odds():
    url = f"https://api.the-odds-api.com/v4/sports/icehockey_nhl/odds/?regions=us&markets=h2h,spreads,totals&apiKey={ODDS_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Odds API not available yet.")
        return pd.DataFrame()
    data = response.json()
    all_odds = []
    for game in data:
        for book in game.get("bookmakers", []):
            for market in book.get("markets", []):
                all_odds.append({
                    "game": f"{game.get('home_team')} vs {game.get('away_team')}",
                    "market": market.get("key"),
                    "outcomes": market.get("outcomes")
                })
    return pd.DataFrame(all_odds)
