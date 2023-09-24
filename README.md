# anime-quotes-discord-bot
A Discord bot sending a random anime quote everyday for users to guess.

## Usage in Discord
The bot sends a question with a quote on startup and on 00:00 every day. The players need to guess the character name and the anime title.
To submit an answer it has to be prefixed with a "!" sign. Character and title can only be guessed once per question.

## General usage of the build
First you need to create an .env file next to your main.py file. This should contain a variable called BOT_TOKEN which should be your Discord bot token.

The other variable should be called CHANNEL_ID and contains the channel ID from the channel in which the bot should post the questions.

After installing the requirements you can either run the main.py file or build the Docker container from the Docker file.

Currently there are only 5 quotes, stored in the quotes.json file. Feel free to add some of your own.
