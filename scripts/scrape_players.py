# scripts/scrape_players.py
import pandas as pd
from sportsipy.nhl.teams import Teams

def get_players():
    all_players = []
    for team in Teams():  # all NHL teams
        roster = team.roster
        for player in roster.players:
            all_players.append({
                "name": player.name,
                "team": team.abbreviation,
                "position": player.position
            })
    return pd.DataFrame(all_players)
