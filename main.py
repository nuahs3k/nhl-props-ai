# main.py
import pandas as pd
from scripts.scrape_players import get_players
from scripts.scrape_stats import get_player_stats
from scripts.scrape_team import get_team_stats
from scripts.scrape_news import get_injury_news
from scripts.fetch_odds import fetch_odds
from scripts.projections import calculate_projections
from scripts.process_data import process_data

def run():
    print("Fetching player list...")
    players = get_players()
    if players.empty:
        print("Season not started yet or no players found.")
        return

    print("Scraping player stats...")
    player_stats = get_player_stats(players)
    if player_stats.empty:
        print("Player stats not available yet.")
        return

    print("Scraping team advanced stats...")
    team_stats = get_team_stats()
    if team_stats.empty:
        print("Team stats not available yet.")
        return

    print("Scraping injury/news adjustments...")
    injury_news = get_injury_news()
    
    print("Fetching odds from sportsbook API...")
    odds_df = fetch_odds()
    if odds_df.empty:
        print("Odds not available yet. Check your API key or wait for games to be posted.")
    
    print("Calculating projections...")
    projections = calculate_projections(player_stats, team_stats, injury_news)

    print("Processing data and calculating edges...")
    results = process_data(projections, odds_df)
    if results.empty:
        print("❌ No results after processing. Season may not have started.")
        return

    # Output top 30 edges
    top_edges = results.sort_values("edge", key=abs, ascending=False).head(30)
    print("\nTop 30 edges for today:")
    print(top_edges.to_string(index=False))

if __name__ == "__main__":
    run()
