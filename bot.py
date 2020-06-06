import discord
import asyncio
import json
from discord.ext import commands
from accuweather import weatherinfo
import os

client = commands.Bot(command_prefix="!")
token = os.getenv('Token')


@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ping(ctx):
    """Displays Bot's Ping"""
    await ctx.send(f"Pong! {round(client.latency *1000)}ms")

@client.command()
async def weather(ctx, city):
    data = weatherinfo(city)
    text = (data["Headline"]["Text"])
    date = (data["DailyForecasts"][0]["Date"])
    dayprecep_type = (data["DailyForecasts"][0]["Day"]["PrecipitationType"])
    dayprecep_int = (data["DailyForecasts"][0]["Day"]["PrecipitationIntensity"])
    embed = discord.Embed(
        title = f"Weather Report in {city}:",
        description = f"{text}",
        color = discord.Color.dark_gold()
    )
    embed.add_field(name = "Date:", value = f"{date}")
    embed.add_field(name = "Day Precepitation:", value = f"{dayprecep_type} \n {dayprecep_int}", inline=False)
    await ctx.send(embed=embed)

client.run(token)
