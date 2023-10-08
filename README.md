# anime-quotes-discord-bot
A Discord bot sending a random anime quote everyday for users to guess.

## Users guide
The bot sends a question with a quote on startup and on 00:00 every day. The players need to guess the character name and the anime title.
Use the "/anime" command to guess the title or the "/character" command to guess the character. The answer is submitted hidden so other people can't see your answer if it was correct.
Every question can be answered by multiple users.

## Server owners guide
Add the bot by using this link https://discord.com/api/oauth2/authorize?client_id=1152233813439680542&permissions=3072&scope=bot to your server.
After joining you can set one channel for the bot to post the daily questions by using the "/settings" command. You can change the channel at any point in time.


## Building the docker image
First you need to create an .env file next to your main.py file. This should contain a variable called BOT_TOKEN which should be your Discord bot token.

After installing the requirements you can either run the main.py file or build the Docker container from the Docker file.

Currently there are only 5 quotes, stored in the quotes.json file. Feel free to add some of your own.
