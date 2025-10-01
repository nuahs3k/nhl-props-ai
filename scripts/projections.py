# scripts/projections.py
import pandas as pd

def calculate_projections(player_stats, team_stats, injury_news):
    if player_stats.empty or team_stats.empty:
        return pd.DataFrame()
    
    # Simple example: weighted points by team GF/GA
    team_dict = team_stats.set_index("Team").to_dict("index")
    projections = player_stats.copy()
    projections["proj_points"] = projections.apply(
        lambda row: row["points"] * (team_dict[row["team"]]["GF"] / max(1, team_dict[row["team"]]["GA"])),
        axis=1
    )
    return projections
