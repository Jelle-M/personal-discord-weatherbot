[![Build Status](https://travis-ci.com/MoskiMBA/personal-discord-weatherbot.svg?branch=master)](https://travis-ci.com/MoskiMBA/personal-discord-weatherbot)
![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)


# personal-discord-weatherbot
Receive automated weather updates through discord.

Every 24 hours receive a push notification on both desktop and mobile to get the current weather. 

## Requirements

Setup discord bot (see references) and register to Dark Sky to accquire API tokens/keys.
Place them in `weather_bot/config/token.py` like below.
```
# weather_bot/config/token.py

# -*- coding: utf-8 -*-

"""This file contains the necessary tokens/keys."""
DISCORD_BOT_TOKEN = (
    'NTQ-DISCORD-TOKEN-udA'
)
DARK_SKY_TOKEN = 'be1-DARK-SKY-TOKEN-de8'

```


## TODO

Easiest implementation of this cross platform problem would be to use a discord bot that contacts a weather api and uses the @mention feature to show the weather forecast.


Repo init

- [x] Init README.md
- [x] CI
- [ ] Issues
- [ ] Docs/requirements/howto

Test individual components

- [x] Contact API to receive weather information
- [x] Run simple discord bot locally
- [ ] Deploy bot on Heroku

Integrate a simple discord bot with api request

- [ ] Send request to discord bot, returns weather info
- [ ] Automaticly every x time, trigger discord bot
- [ ] Format output of bot

Publish bot

## References
1. [Python Wrapper](https://github.com/csparpa/pyowm) to contact [OpenWeatherMap API](https://openweathermap.org/api):.
Offers current weather data and a 5 day forecast.

1. [4CAST Weather bot](https://github.com/lluisrojass/discord-forecast-bot) fetches and provides weather
conditions and a 3 day forecast. Uses [Yahoo's YQL weather endpoint](https://developer.yahoo.com/weather/). This project has trouble connecting to the API, perhaps due to retirement of the existing weather API. The new API requires a form to be filled in and proocessing can take up to 3 business days. 

1. [Host discord bot on Heroku](https://boostlog.io/@anshulc95/how-to-host-a-discord-bot-on-heroku-for-free-5a9c230798a8b60096c43336)

1. How to create discord bot with python
    - [Discord.py](https://github.com/Rapptz/discord.py)
    - https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token
    - https://www.devdungeon.com/content/make-discord-bot-python
    - https://medium.com/@moomooptas/how-to-make-a-simple-discord-bot-in-python-40ed991468b4

1. Dark Sky weather API
    - [Python wrapper for the Dark Sky API](https://pypi.org/project/darkskylib/)
    - [Dark Sky weather API](https://darksky.net)


