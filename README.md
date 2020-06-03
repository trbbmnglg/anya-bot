# anya-bot

This is a simple Conversational AI integrated in Facebook messenger to
help people in answering information about related to the pandemic COVID-19 virus in the Philippines.

Providing helpful insights of what COVID-19 is, its origin, what are the symptoms and ways to avoid it. Currently supported Tagalog conversation.

# Features
- Linear and non-linear conversation.
- Supported Tagalog language.
- Define COVID, symptoms and ways to avoid getting infected.
- Provide COVID emergency hotlines.
- Get latest total cases, deaths and recoveries separately and in summary.
- Scrape results from official site using Selenium and save it to a CSV lookup file.
- Scraping is cron setup "run every 30 minutes" since it doesn't need to be real-time.
- Run RASA components and scraping via a Jenkins build.
- Locally hosted with used of ngrok.

# Scripts
- getFreshCounts.py (use for scraping the cases of COVID)
    - change the absolute paths if you are just planning to host it locally
    - change the url
    - change the xpaths for cases, deaths and recovered variable
    - ensure that the case_summary.csv lookup is present

# Jenkins Configuration
- create jobs for any RASA component you want to run
- recommending to create per rasa command (i did for core, actions, validate and train)
- in build, ensure to cd on C:\Users\$USER\anaconda3\Scripts\
- add new line for "call activate $environment_name"
- then another line for the rasa command you want (e.g. rasa run, ras run actions)

# Deployment
- Facebook approved the app last May 30, 2020.
- People has been using it already.

# Instruction
- Visit https://m.me/covid19phanyabot.
- Start conversation.
- See below keywords for non-linear conversation.

# Keywords
- Ano ang COVID
- Pinagmulan ng COVID
- Sintomas 
- Iwasan ang COVID
- Gamot
- Bakuna
- Itsura ng COVID
- bilang ng kaso
- bilang ng namatay
- bilang ng gumaling
- covid update