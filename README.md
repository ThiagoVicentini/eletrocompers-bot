# Eletrocompers Bot
A bot made for the purpose of studying APIs. This bot can be added to a group and constantly check the receiving messages to start a new command. Through the commands the bot can connect with the [Steam API ](https://developer.valvesoftware.com/wiki/Steam_Web_API#GetGlobalAchievementPercentagesForApp_.28v0001.29), [Discord API](https://github.com/discord/discord-api-docs) and the [Reddit API](https://www.reddit.com/dev/api/)

## Commands
### /help
Send a menu with all the existing commands 

### /play
Connects with the Steam API and show a dict with of all the registered friends and the current game they're playing

### /r@something
Connects with the Reddit API and get the url of a random posts of the subreddit named "something"

## Using the bot
After downloading the source code you need to create a file named "secret.py" with all your tokens and keys for the APIs to work
```
tokenTelegram="something"
tokenReddit='something'
tokenSteam='something'
password="something"
```

Then just execute the programa
```
python main.py
```

## Built with

* [Discord.py](https://discordpy.readthedocs.io/en/latest/) - Python API Wrapper for Discord.
* [praw.py](https://praw.readthedocs.io/en/latest/) - Python API Wrapper for Reddit.