import time
import discord
from discord.ext import commands
import requests
import random
from api import random_dog, random_duck, run_code_api, random_anime
from pytube import Channel
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='>', intents=intents)
csplst = ["камень", "ножницы", "бумага"]
reports = 0
c = Channel('https://www.youtube.com/channel/UCna8ZzxgyPVBzj0KKiUzYvw/videos')
vd = 13
@bot.command()
async def report(ctx, user: discord.User = None, *reason):
    author = ctx.message.author
    rearray = ' '.join(reason[:])
    if user:
        await user.send('You have been reported!')
    await ctx.send(f"{author} has reported {user}, reason: {rearray}")
    await ctx.message.delete()


@bot.command()
async def py(ctx, code):
    res = run_code_api(code)
    await ctx.send(res)


@bot.command()
async def dog(ctx):
    url = random_dog()
    await ctx.send(url)


@bot.command()
async def anime(ctx, category):
    url = random_anime(category)
    await ctx.send(url)


@bot.command()
async def duck(ctx):
    url = random_duck()
    await ctx.send(url)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def echo(ctx, message):
    await ctx.send(message)


@bot.command()
async def spam(ctx, spam):
    await ctx.send(spam * 100)


@bot.command()
async def helpcommands(ctx):
    await ctx.send("spam - x10 сообшение ping - pong cspsp - камень, ножницы, бумага")


@bot.command()
async def csp(ctx, msg):
    a = random.choice(csplst)
    await ctx.send(a)
    if msg == a:
        await ctx.send("ничья")
    elif msg == 'камень' and a == "ножницы":
        await ctx.send("вы выиграли")
    elif msg == "бумага" and a == "камень":
        await ctx.send("вы выиграли")
    elif msg == "ножницы" and a == "бумага":
        await ctx.send("вы выиграли")
    else:
        await ctx.send("вы проиграли")
@bot.command()
async def vidio (message):
    for url in c.video_urls[:1]:
        await message.send(url)
@bot.command()
async def allvidios(message):
    for url in c.video_urls:
        await message.send(url)

@bot.command()
async def hot_dog(ctx):
    url = ctx.message.attachments[0].url
    img_name = url.split('/')[-1]
    img_data = requests.get(url).content
    with open(img_name, 'wb') as handler:
        handler.write(img_data)

        
bad_words = ['лох', 'бот', 'слит']
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for bad_word in bad_words:
        if bad_word in message.content:
            await message.delete()
            await message.channel.send(f"your message has been censored {message.author.mention}.")
            return
    
    await bot.process_commands(message)
        
bot.run('OTc1NDA4MjcwODQxOTA1MjQy.GDyZYT.uR0kudD18aND03OZK6QibhTD3r5Ugt00Etm7Xw')