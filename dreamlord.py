import discord
import random
import linecache
import re
import shelve
from random import shuffle
from avalon import *
#from wordgame import *
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
busyChannels = []
game = discord.Game(name="github.com/cameronleong", url="github.com/cameronleong")

@client.event
async def on_message(message):
	if message.author == client.user:			# we do not want the bot to reply to itself
		return

	if message.content.startswith('!hello'):
		msg = 'Greetings {0.author.mention}'.format(message)
		await message.channel.send(msg)

	if message.content.startswith('!avalon'):
		if message.channel in busyChannels:
			await message.channel.send("Channel busy with another activity.")
		else:
			busyChannels.append(message.channel)
			await message.channel.send("Starting **The Resistance: Avalon - Discord Edition** in `#"+message.channel.name+"`...")
			await avalon(client, message)
			busyChannels.remove(message.channel)

	"""
	if message.content.startswith('!word'):
		if message.channel in busyChannels:
			await client.send_message(message.channel, "Channel busy with another activity.")
		else:
			busyChannels.append(message.channel)
			await client.send_message(message.channel, "Starting **Guess-the-Word** in `#"+message.channel.name+"`...")
			await run(client, message)
			busyChannels.remove(message.channel)
	"""
	#if message.content.startswith('!score'):
	#	await scoreboard(client, message)

	if message.content.startswith('!help'):
		# message.channel.send()
		await message.author.send('Please visit https://cameronleong.github.io/avalon to find out more.')


@client.event
async def on_ready():
	print('Connected!')
	print('Username: ' + client.user.name)
	print('ID: ' + str(client.user.id))
	await client.change_presence(activity = game)


client.run(os.getenv("SECRET_TOKEN"))
