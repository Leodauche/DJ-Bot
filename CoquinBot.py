import discord
import random
import aiohttp
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix=';')


@bot.event
async def on_ready():
	print ("CoquinBot pret")
	await bot.change_presence(game=discord.Game(name=';help'))


@bot.command(pass_context=True)
async def lewd(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/hentai') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def yuri(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/yuri') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def trap(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/trap') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def gif(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/nsfw_neko_gif') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def loli(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/smallboobs') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")


@bot.command(pass_context=True)
async def neko(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/lewdkemo') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def solog(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/solog') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")


@bot.command(pass_context=True)
async def feet(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/feet') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def futanari(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/futanari') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def holo(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/hololewd') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def feetg(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/feetg') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def cum(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/cum') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")



@bot.command(pass_context=True)
async def neko2(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/erokemo') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")


@bot.command(pass_context=True)
async def boobs2(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/les') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")


@bot.command(pass_context=True)
async def wallpaper(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/wallpaper') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")


@bot.command(pass_context=True)
async def lewdk(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/lewdk') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")


@bot.command(pass_context=True)
async def ngif(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/ngif') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def eroyuri(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/eroyuri') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def eroneko(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/eron') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def bj(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/bj') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def solo(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/solo') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def anal(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/anal') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def erofeet(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/erofeet') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")		



@bot.command(pass_context=True)
async def keta(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/keta') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")	


@bot.command(pass_context=True)
async def blowjob(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/blowjob') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")	

@bot.command(pass_context=True)
async def pussy(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/pussy') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def tits(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/tits') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def pussy2(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/pussy_jpg') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def pwankg(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/pwankg') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def classic(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/classic') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def kuni(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/kuni') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def erok(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/erok') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")

@bot.command(pass_context=True)
async def ero(ctx):
	await bot.delete_message(ctx.message)
	nsfw = discord.utils.get(ctx.message.server.channels , id="420994817804206080")
	if (ctx.message.channel == nsfw) :
		async with aiohttp.ClientSession() as session:
			async with session.get('https://nekos.life/api/v2/img/ero') as r: 
				if r.status == 200 :
					js = await r.json()
					await bot.send_message(ctx.message.channel, js['url'])
	else : 
		await bot.say("Vous ne pouvez pas utiliser cette commande dans ce channel")


bot.run(os.environ.get('BOT_TOKEN'))