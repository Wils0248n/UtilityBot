import discord, asyncio, time, aiohttp, sys
from aiohttp import errors
from utilitybot import UtilityBot

utilitybot = UtilityBot()

# Initializes patch information and starts the bot
def main():
		while not utilitybot.bot.is_closed:
			try:
				utilitybot.bot.loop.run_until_complete(utilitybot.bot.start(sys.argv[1]))
			except aiohttp.errors.ClientOSError:
				print("Could not connect to Discord, reconnecting...")
				time.sleep(10)
			except RuntimeError as e:
				print("RuntimeError occured:\n\n" + str(e) + "\n\n")
				time.sleep(10)
			except IndexError:
				print("You must enter a bot token.\n")
				print("Usage: python3 run.py <bot-token>")
				sys.exit(1)
			except discord.errors.LoginFailure:
				print("Invalid bot token.\n")
				sys.exit(1)
			except Exception as e:
				print("Error Occured:\n\n" + str(e) + "\n\n")
				time.sleep(10)

@utilitybot.bot.event
async def on_message(message):
	if message.content == '!utilitybot':
		await utilitybot.bot.send_message(message.channel, embed=await utilitybot.get_embed_message())

	if message.content == '!flip':
		await utilitybot.bot.send_message(message.channel, "Coin Flipped: " + utilitybot.flip())

	if message.content == '!roll':
		await utilitybot.bot.send_message(message.channel, "Dice Rolled: " + utilitybot.roll())

	if message.content == '!clear':
		await utilitybot.clear_channel(message.channel)

	if message.content.startswith('!owo '):
		await utilitybot.bot.send_message(message.channel, "OwO notcies your message: " + utilitybot.OwOify(message.content))

	if message.content.startswith('!clear '):
		await utilitybot.clear_channel_with_word(message.channel, message.content.split(' ')[1])



@utilitybot.bot.event
async def on_ready():
	print(utilitybot.bot.user.name+ ' Ready!')
	await utilitybot.bot.change_presence(game=discord.Game(name="Utilitybot | !utilitybot"))

if __name__ == '__main__':
	main()
