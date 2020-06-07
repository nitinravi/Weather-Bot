import discord
import asyncio
import json
from discord.ext import commands
from accuweather import weatherinfo
import os
from discord.utils import get

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

    if (data["DailyForecasts"][0]["Day"]["HasPrecipitation"]) == True:

        dayprecep_type = (data["DailyForecasts"][0]
                          ["Day"]["PrecipitationType"])
        dayprecep_int = (data["DailyForecasts"][0]["Day"]
                         ["PrecipitationIntensity"])

        if dayprecep_int == "Heavy":
            suggestion = "Stay indoors \n Store essentials \n Make sure to turn your sprinklers off"
            emoji = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/237/cloud-with-rain_1f327.png"

        elif dayprecep_int == "Moderate":
            suggestion = "Its safe to head out \n Make sure to cover/protect yourself"
            emoji = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/237/umbrella_2602.png"

        elif dayprecep_int == "Light":
            suggestion = "Its a pleasant day \n Enjoy your day"
            emoji = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/lg/57/sun-behind-cloud_26c5.png"

    else:
        dayprecep_type = "NA"
        dayprecep_int = "NA"
        suggestion = "Enjoy your clear day"
        emoji = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/237/black-sun-with-rays_2600.png"

    embed = discord.Embed(
        title=f"Weather Report in {city}:",
        description=f"{text}",
        color=discord.Color.dark_gold()
    )
    embed.set_thumbnail(url=emoji)
    embed.add_field(name="Date:", value=f"{date}")
    embed.add_field(name="Day Precepitation:",
                    value=f"{dayprecep_type} \n {dayprecep_int}", inline=False)
    embed.add_field(name="Suggestion:", value=f"{suggestion}", inline=False)

    await ctx.send(embed=embed)

client.run(token)
