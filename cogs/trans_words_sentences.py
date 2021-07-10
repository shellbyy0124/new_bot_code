import discord

from discord.ext import commands
from discord.ext.commands import Cog
from googletrans import Translator

class TranslateMySentence(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command()
    async def trans(self, ctx, destlang:str, *, a:str):

        translator = Translator()

        orig_lang = translator.detect(text=a)

        new_trans = translator.translate(dest=destlang, text=a)
        
        embed = discord.Embed(
            color = discord.Colour.random(),
            title = 'ButtlerBots Translator',
            description = f'Original Sentence: {a.content}\nOriginal Language: {orig_lang}\nTranslated To: {destlang}\nTranslation: {new_trans.text}',
            inline = False
        ).set_thumbnail(
            url = self.bot.user.avatar_url
        )

        await ctx.message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(TranslateMySentence(bot))