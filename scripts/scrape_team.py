# scripts/scrape_team.py
import pandas as pd
from sportsipy.nhl.teams import Teams

def get_team_stats():
    all_stats = []
    for team in Teams():
        all_stats.append({
            "Team": team.abbreviation,
            "Wins": team.wins,
            "Losses": team.losses,
            "OT": team.ot_losses,
            "GF": team.goals_scored,
            "GA": team.goals_against,
            "PP%": team.power_play_percentage,
            "PK%": team.penalty_kill_percentage
        })
    return pd.DataFrame(all_stats)
