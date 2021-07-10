import datetime
import random
import discord
import json

from discord.ext import commands, tasks
from discord.ext.commands import Cog 

class ChallengeFunctions(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.challenge_of_the_day.start()

    @commands.command(aliases=['challenge'])
    async def challenge_of_the_day(self, ctx):

        await self.bot.wait_until_ready()

        with open('challenges.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)

        category = random.choice(data.keys())
        instructions = data[category]["instructions"]
        description = data[category]["description"]
        diff_level = data[category]["difficulty_level"]
        creator = data[category]["challenge_creator"]
        challenge_name = data[category]["challenge_name"]

        embed = discord.Embed(
            color = discord.Colour.random(),
            title = f'ButtlerBots Challenge for {datetime.today()}',
            description = f'{challenge_name}\n{category}\n{creator}\n{diff_level}',
            inline = False
        ).add_field(
            name = 'Description',
            value = f'{description}',
            inline = False
        ).add_field(
            name = 'Instructions',
            value = f'{instructions}'
        ).set_thumbnail(
            url = self.bot.user.avatar_url
        )

        