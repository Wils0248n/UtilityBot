![UtilityBot Banner](https://i.imgur.com/FQTjdml.png)

# Discord UtilityBot

UtilityBot is a Discord Bot that provides basic utility to your discord server. \
\
See [this guide](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) to setup your bot and get a bot token.

## Commands

!flip -> Flips a coin. \
!roll -> rolls a six sided dice. \
!owo -> Defiles the proceeding message. \
!clear -> clears a text channel. \
!clear <word> -> clears messages that contain <word>.

## Usage

```
python3 utilitybot.py <Bot-Token>
```

## Docker

Example of a bash script used to deploy UtilityBot in docker using the DockerFile

```
docker build -t utilitybot_image .
docker run -d \
    --name utilitybot \
    -v "$(pwd):/app" \
    -e "TOKEN=<Bot-Token>" \
    utilitybot_image
```
