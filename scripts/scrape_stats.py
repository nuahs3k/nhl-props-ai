# scripts/scrape_stats.py
import pandas as pd
from sportsipy.nhl.teams import Teams

def get_player_stats(players_df):
    all_stats = []
    for team in Teams():
        roster = team.roster
        for player in roster.players:
            all_stats.append({
                "name": player.name,
                "team": team.abbreviation,
                "position": player.position,
                "games_played": player.games_played,
                "goals": player.goals,
                "assists": player.assists,
                "points": player.points,
                "plus_minus": player.plus_minus,
                "penalty_minutes": player.penalty_minutes,
                "shots": player.shots
            })
    if not all_stats:
        return pd.DataFrame()
    return pd.DataFrame(all_stats)
