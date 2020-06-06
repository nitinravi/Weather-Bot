import discord
import asyncio
import json
from discord.ext import commands
from accuweather import city_id
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
async def cityid(ctx, city):
    data = city_id(city)
    await ctx.send(data)

client.run(token)
