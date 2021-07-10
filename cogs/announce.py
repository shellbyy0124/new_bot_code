import discord

from discord.ext import commands
from discord.ext.commands import Cog 

class AnnouncementCommands(commands.Cog):

    def __init__(self, bot):

        self.bot = bot 

    @commands.command()
    @commands.has_any_role('staff', 'dev')
    async def announce(self, ctx):

        def check(m):
            return ctx.message.author.id == m.author.id

        guild = ctx.message.guild.id
        user = ctx.message.author

        embed = discord.Embed(
            color = discord.Colour.random(),
            title = 'ButtlerBot Announcement Editor',
            description = 'Please Select The Type Of Announcement:\ncommunity, staff, developer',
            inline = False
        ).set_image(
            url = self.bot.user.avatar_url
        ).set_footer(
            text = 'This command will timeout if you do not respond in 30 seconds'
        )

        ans = await self.bot.wait_for('message', check=check, timeout=30)

        if ans.content.lower() == 'community':

            self.comp_comm_ann(guild, user)

        elif ans.content.lower() == 'staff':

            self.comp_staff_ann(guild, user)

        else:

            self.comp_dev_ann(guild, user)

def setup(bot):
    bot.add_cog(AnnouncementCommands(bot))