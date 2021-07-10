import discord

from discord.ext import commands

class MathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def math(self, ctx, *, expression):
        """
        Evaluates math expressions after ensuring clean input data. WARNING: DO NOT REMOVE DATA CLEANING!!
        Supports anything using ( + - * / ( ) % . )
        """

        equation_pattern = r"^[-+*\/()\d %.]+$"
        match = re.match(equation_pattern, expression)

        if match:
            try:
                result = eval(expression)
                embed = discord.Embed(colour=discord.Colour.blue())
                embed.add_field(name=f"{ctx.author.name}'s result:", value=f'{expression}=\n{result}')
            except Exception:
                embed = discord.Embed(colour=discord.Colour.red())
                embed.add_field(name=f"Invalid Expression", value=f"Try again using a math expression")
        else:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.add_field(name=f"Invalid Expression", value=f'Expression must only use numbers, symbols and spaces')

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(MathCog(bot))
    print('math is loaded')