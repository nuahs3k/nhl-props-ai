🏒 NHL AI Props

An AI-powered NHL player props and betting edge calculator.

This project:

📊 Collects player stats, team stats, injury news, and sportsbook odds

🤖 Uses Python to project player performance

💰 Finds the best betting value (edges) for the day’s games

✨ Features

📊 Player stats (historical + live)

🏒 Team advanced stats and matchups

🚑 Injury/news adjustments

💰 Sportsbook odds with edge calculations

📋 Daily Top 30 betting edges output

🖥 Requirements

Before you start, make sure you have:

Python 3.9+ → check with python --version or python3 --version

pip (Python package manager) → check with pip --version

Git → check with git --version

Code editor (recommended: VS Code; Notepad also works for quick edits)

Internet connection (APIs and scraping require live data)

(Optional) Virtual environment knowledge – tutorial steps included below, no prior setup needed

📂 Project Layout
nhl-props-ai/
│── requirements.txt   # Python dependencies
│── main.py            # Main script to run the bot
│
└── scripts/           # Python scripts for scraping & processing
    ├── scrape_players.py
    ├── scrape_stats.py
    ├── scrape_team.py
    ├── scrape_news.py
    ├── fetch_odds.py
    ├── process_data.py
    └── projections.py

🚀 Getting Started
Step 1: Clone the Repo (Download the Project)

Open PowerShell (Windows) or Terminal (Mac/Linux) and run:

git clone https://github.com/nuahs3k/nhl-props-ai.git
cd nhl-props-ai

Step 2: Set Up a Virtual Environment

This keeps your project’s libraries clean and separate.

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate


Mac/Linux (Terminal):

python3 -m venv venv
source venv/bin/activate


✅ You should now see (venv) at the start of your command line.

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Add Your API Keys

You’ll need two free API accounts:

Odds API
 → sportsbook odds

News API
 → injury/news data

How to set them up:

Sign up at each site (free tier is fine).

Copy your API key from the dashboard.

In the project folder, create a file named .env.

On Windows: open Notepad → paste → "Save As" → select All Files → name it .env

On Mac/Linux: open TextEdit or run nano .env in Terminal

Inside .env, paste:

ODDS_API_KEY=your_odds_api_key_here
NEWS_API_KEY=your_news_api_key_here


Save and close.

Step 5: Run the Bot
python main.py


If the NHL season hasn’t started → the bot will notify you.

If games are live → you’ll get a table of Top 30 betting edges.

🎯 Custom Player Tracking

Want to track specific players?

Open scripts/projections.py

Edit with the player name(s) you want

Run python main.py again → get player-specific projections

🛠 Troubleshooting & Common Errors

⚠️ 1. Python not recognized

'python' is not recognized as an internal or external command


➡️ Python isn’t installed or not in your PATH.
✅ Fix: Install Python and restart your terminal. On Windows, check “Add Python to PATH” during install.

⚠️ 2. Virtual environment won’t activate (Windows)

.\venv\Scripts\Activate : File C:\... is not digitally signed


➡️ Security policy blocked it.
✅ Fix (run as Admin once):

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


⚠️ 3. Missing packages

ModuleNotFoundError: No module named 'pandas'


➡️ Required libraries didn’t install.
✅ Fix: Run again inside your venv:

pip install -r requirements.txt


⚠️ 4. API key errors

Invalid API Key
KeyError: 'ODDS_API_KEY'


➡️ .env file missing or incorrect.
✅ Fix: Double-check .env contents:

ODDS_API_KEY=your_key_here
NEWS_API_KEY=your_key_here


⚠️ 5. Season hasn’t started

No stats available


➡️ The NHL season isn’t active yet.
✅ Fix: Wait until season starts.

⚠️ 6. Odds not showing up

Empty dataframe


➡️ Sportsbooks haven’t published odds yet.
✅ Fix: Try later, closer to game time.

⚠️ 7. Script crashes with random error
(e.g., Timeout, ConnectionError)
➡️ Website or API blocked the request.
✅ Fix: Wait a few minutes and retry.

⚠️ 8. Wrong directory

python: can't open file 'main.py': [Errno 2] No such file or directory


➡️ You’re not in the right folder.
✅ Fix:

cd nhl-props-ai
python main.py

🔮 Future Plans

Live projections during the season

Multiple sportsbook integrations

5+ years of historical data

AWS automation (Lambda/EC2 + CloudWatch + S3 + optional dashboard)

⚙️ Tech Stack

This project uses:

Python → core programming language

Pandas / NumPy → data wrangling & calculations

BeautifulSoup → HTML parsing & scraping

SportsPy → player & team stats collection

APIs → Odds API (sportsbook data), News API (injury/news)

dotenv → secure API key management

Requests → API & web requests

When the NHL season hasn’t started, the bot will notify you like this:

Fetching player list...
The requested page returned a valid response, but no data could be found. 
Has the season begun, and is the data available on www.sports-reference.com?
Season not started yet or no players found.


✅ This shows that the bot correctly checks for available stats and waits until the season begins.
🔄 Once the season starts, it will return the Top 30 daily player edges in a table-like format.
