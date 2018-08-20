#SoundBot par Léo
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix='~')
players = {}

bot.remove_command('help')

if not discord.opus.is_loaded():
    discord.opus.load_opus()


@bot.event
async def on_ready():
	print ("SoundBot pret")
	await bot.change_presence(game=discord.Game(name="~play"))



@bot.command(pass_context=True)
async def join(ctx):

	bot_voice_channel = bot.voice_client_in(ctx.message.server)
	user_voice_channel = ctx.message.author.voice.voice_channel.name
	print("user : ",user_voice_channel)
	if bot_voice_channel == None :
		await bot.join_voice_channel(ctx.message.author.voice.voice_channel)

	else :
		bot_voice_channel_name = bot_voice_channel.channel.name
		print("bot_voice_channel_name = " , bot_voice_channel)

		if bot_voice_channel_name != user_voice_channel :
			print("changer de chan")
		else :
			await bot.say("Je suis deja dans ton channel fdp")


@bot.command(pass_context=True)
async def pause(ctx):
	players[ctx.message.server.id].pause()
	print("pause")


@bot.command(pass_context=True)
async def resume(ctx):
	players[ctx.message.server.id].resume()
	print("resume")


@bot.command(pass_context=True)
async def stop(ctx):
	players[ctx.message.server.id].stop()
	print("stop")


@bot.command(pass_context=True)
async def leave(ctx):
	 voice_channel = bot.voice_client_in(ctx.message.server)
	 await voice_channel.disconnect()


@bot.command(pass_context=True)
async def play(ctx, url):
	voice_channel = bot.voice_client_in(ctx.message.server)
	if voice_channel == None :
		await bot.join_voice_channel(ctx.message.author.voice.voice_channel)
		voice_channel = bot.voice_client_in(ctx.message.server)

	player = await voice_channel.create_ytdl_player(url)
	players[ctx.message.server.id] = player
	player.start()


@bot.command(pass_context=True)
async def say(ctx,*,message):
	await bot.say(str(message))

bot.run("NDQxMzQ4NTI0ODQ4NzA5NjMy.Dlx5rA.dicKXrX5GYjXnhnA-Dy67itt9RE")