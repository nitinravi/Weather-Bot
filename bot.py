import discord
import asyncio
import json
from discord.ext import commands
import os

token = os.getenv('Token')
client = commands.Bot(command_prefix="!")
client.run(token)