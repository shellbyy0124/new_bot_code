import discord
import sqlite3

from discord.ext import commands, tasks 
from discord.ext.commands import Cog 

class UpdateMyMessages(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.updateMessages.start()

def setup(bot):
    bot.add_cog(UpdateMyMessages(bot))