NHL AI Props

An AI-powered NHL player props and betting edge calculator. This project scrapes player stats, team advanced stats, injury/news adjustments, and sportsbook odds to generate sharp betting lines and identify top edges.

This project builds on my previous NBA AI Props
 project, incorporating improved scraping, advanced metrics, and matchup-based projections.

Features

Pulls NHL player stats (historical and current) using Sportsipy.

Scrapes team-level advanced stats and matchup adjustments.

Considers injury news and recent performance trends.

Pulls odds from sportsbooks to calculate edges.

Outputs top 30 projected edges for each game day in a table-like format.

Automatic player-to-team mapping with position data.

Project Folder Layout
nhl-props-ai/
│
├── scripts/                 # Contains all Python scripts for scraping and processing
│   ├── scrape_players.py
│   ├── scrape_stats.py
│   ├── scrape_team.py
│   ├── scrape_news.py
│   ├── fetch_odds.py
│   ├── process_data.py
│   └── projections.py
│
└── main.py                  # Main script to run the NHL AI Props bot

Getting Started

Clone the repo

git clone https://github.com/nuahs3k/nhl-props-ai.git
cd nhl-props-ai


Set up a virtual environment

python -m venv venv
.\venv\Scripts\Activate  # Windows PowerShell
source venv/bin/activate # Mac/Linux


Install required packages

pip install -r requirements.txt


Add your own API keys
You will need to obtain your own API keys for:

Odds API – for sportsbook data.

News API – for injury and news data.

Create a .env file or update the scripts with your API keys.

Run the bot

python main.py


If the season hasn't started, the bot will notify you and wait until stats are available.

Custom Player Projects

Designed to allow you to track custom players or create player-specific projections.

Supports advanced metrics and matchup adjustments for sharper edge calculations.

Troubleshooting / Known Issues

Season not started → no stats available.

Missing or invalid API keys → bot will skip data collection.

Output depends on sportsbooks publishing odds; early in the season may return fewer results.

Future Plans

Update project during the NHL season for live stats and projections.

Incorporate multi-source sportsbook odds for enhanced edge calculation.

Expand historical dataset analysis (past 5+ years) to refine projections.

AWS Automation:

Run the bot in the cloud daily using AWS Lambda or EC2.

Schedule jobs with CloudWatch Events.

Store historical outputs in S3 for analytics.

Optional API Gateway integration for real-time dashboard access.
