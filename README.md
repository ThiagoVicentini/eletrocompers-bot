# Eletrocompers Bot
A bot made for the purpose of studying APIs. This bot uses the [Telegram API](https://core.telegram.org/bots/api) and can be added to a group and constantly check the receiving messages to start a new command. Through the commands the bot can connect with the [Steam API ](https://developer.valvesoftware.com/wiki/Steam_Web_API#GetGlobalAchievementPercentagesForApp_.28v0001.29), [Discord API](https://github.com/discord/discord-api-docs) and the [Reddit API](https://www.reddit.com/dev/api/)

## Commands
### /help
Send a menu with all the existing commands 

### /play
Connects with the Steam API and show a dict with of all the registered friends and the current game they're playing. You can control the registered friends through a file with the IDs of each friend on Steam.

### /r@something
Connects with the Reddit API and get the url of a random posts of the subreddit named "something"

## Using the bot
First of all you need to create your bot with de BotFather of Telegram. You can see how to do that [here](https://core.telegram.org/bots#6-botfather). You can add the bot to your group on Telegram or just send direct message to it.

After that, you need to clone this rep and create an environment file named ".env" in the root with all your tokens and keys for the APIs to work. 
```
REDDIT_CLIENT_ID="something"
REDDIT_CLIENT_SECRET="something"
REDDIT_PASSWORD="something"
REDDIT_USER="something"
TELEGRAM_KEY="something"
STEAM_KEY="something"
STEAM_ID="something"
```

Next you need to change the friends.txt file with your friends Steam IDs.

Finally, just execute the program.
```
python main.py
```

## Built with

* [Discord.py](https://discordpy.readthedocs.io/en/latest/) - Python API Wrapper for Discord.
* [praw.py](https://praw.readthedocs.io/en/latest/) - Python API Wrapper for Reddit.