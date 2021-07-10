import discord
import json

from discord.ext import commands
from discord.ext.commands import Cog 

class UponJoiningServer(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        welcome_embed = discord.Embed(
            color = discord.Colour.random(),
            title = 'Thank You For Using ButtlerBot!',
            description = """Hi! Thanks for allowing me into your server! I plan
                             to be the best buttler to you, and your friends that
                             I can be! Please allow me to explain what is currently
                             happening. During this process, this message will change
                             as I go through each step. During each step I will explain
                             what I am doing and why. While this process is happening,
                             please do not make any changes of any kind to your discord.
                             This process will be quick and will take less than 3 minutes
                             to complete. Thank you for your patience!""", inline=False
        ).set_thumbnail(url = self.bot.user.avatar_url)

        embed2 = discord.Embed(
            color = discord.Colour.random(),
            title = 'Step 1!',
            description = """One thing I find most effective is to have my stuff
                             categorized. What I mean by that is I am currently looking
                             at your categories to see what you have. I come pre-set with
                             3 categories for your convinience.\nSupport\nProfiles\nLogs\n
                             The reason for these categories is to help you be able to find
                             items that correspond easier to find. The __Support__ category
                             will handle any and all things dealing with support within your
                             community from receiving help via a voice channel, or inside of
                             a text channel. I also come with a disclaimer on both that says
                             something along the lines of we do this for free, do not rush us
                             , haha, but in a more respectable manner. Once I have finished
                             looking at your catgeories and making the ones missing, I will
                             move to step 2.""", inline = False
        ).set_thumbnail(url = self.bot.user.avatar_url)

        embed3 = discord.Embed(
            color = discord.Colour.random(),
            title = 'Step 2!',
            description = """Now that you have the categories that I need, I will be checking
                             those categories, and adding channels to them that are missing.
                             The purpose of these channels match the names of the channels.
                             For example, if you use the warn command on a member, it will post
                             a copy of the warning in the __warn_logs__ channel. For this process,
                             I will be adding the following channels under their corresponding
                             category names:\n-Support\n--In_Voice_Support\n\n-Profiles\n--view_profile\n 
                             --create_profile\n\n-Logs\n--warn\n--mute\n--temp_ban\n--server_changes\nThe
                             purpose of these channels follows as described earlier, "to make it easier for
                             you as the guild owner, or guild staff member, to find what you are looking for
                             later. Once finished, I will move on to step 3.""",
            inline = False
        ).set_thumbnail(url = self.bot.user.avatar_url)

        embed4 = discord.Embed(
            color = discord.Colour.random(),
            title = 'Step 3!',
            description = """For the final step, I will be checking your roles.
                             Do not worry about rushing over to make them. I got you.
                             I am just looking to see if you have the roles
                             named:\nstaff\ndev\nwhich you may not have so I am going
                             to create the roles for you with no permissions whatsoever
                             so that you can go and give them to the appropriate people
                             which your staff would be your normal staff, and dev would be
                             those who would edit the discord server for you, or for you
                             yourself. Whatever the case, I am going to be using both of
                             those roles to ping them when needed. Please do not delete
                             these roles                           
                             """, inline = False
        ).set_thumbnail(url = self.bot.user.avatar_url)

        msg = await guild.owner.send(embed=welcome_embed)

        checks = []

        if len(checks) == 1:

            await msg.edit(embed=embed2)
            self.check_cats(guild, checks)

        elif len(checks) == 2:

            await msg.edit(embed=embed3)
            self.check_chans(guild, checks)

        elif len(checks) == 3:
            
            await msg.edit(embed=embed4)
            self.check_roles(guild, checks)

        elif len(checks) > 3:

            self.write_to_json(guild)

    async def check_cats(self, guild, checks):

        needed_categories = ['Support', 'Occupied Support Channels', 'Profiles', 'Logs']

        current_categories = []

        for i in guild.categories:

            current_categories.append(i.name)

        for j in needed_categories:

            if j not in current_categories:

                await guild.create_categories(name=str(j))

        checks.append('yes')

        self.check_chans(self, guild, checks)

        return checks

    async def check_chans(self, guild, checks):

        needed_support_channels = ['how_to_support', 'support_commands']
        needed_profiles_channels = ['how_to_create', 'profile_commands']
        needed_logs_channels = ['warnings', 'mutes', 'temp_bans', 'server_changes']

        category_support = discord.utils.get_category(guild.categories, name='Support')
        category_profiles = discord.utils.get_category(guild.categories, name='Profiles')
        category_logs = discord.utils.get_category(guild.categories, name='Logs')

        current_support_channels = []
        current_profiles_channels = []
        current_logs_channels = []

        counter = 0

        self.new_channels = []

        for i in category_support:
            for j in category_profiles:
                for k in category_logs:

                    current_support_channels.append(i.name)
                    current_profiles_channels.append(j.name)
                    current_logs_channels.append(k.name)

        for a in needed_support_channels:

            if a not in current_support_channels:

                counter += 1

                new_sup_chan = str(a) + str(counter)

                new_chan = await guild.create_text_channel(
                    category = category_support,
                    name = new_sup_chan
                )

                self.new_channels.append(new_chan.name)
                self.new_channels.append(new_chan.id)

        counter = 0

        for b in needed_profiles_channels:

            if b not in current_profiles_channels:

                counter += 1

                new_pro_chan = str(b) + str(counter)

                new_chan1 = await guild.create_text_channel(
                    category = category_profiles,
                    name = new_pro_chan
                )

                self.new_channels.append(new_chan1.name)
                self.new_channels.append(new_chan1.id)

        counter = 0

        for c in needed_logs_channels:

            if c not in current_logs_channels:

                counter += 1

                new_log_chan = str(c) + str(counter)

                new_chan2 = await guild.create_text_channel(
                    category = category_logs,
                    name = new_log_chan
                )

                self.new_channels.append(new_chan2.name)
                self.new_channels.append(new_chan2.id)

        checks.append('yes')

        self.check_roles(guild, checks)

        return checks

    async def check_roles(self, guild, checks):

        needed_roles = ['staff', 'dev']

        current_roles = []

        new_roles = []

        for i in guild.roles:
            
            current_roles.append(i.name)

        for j in needed_roles:

            if j not in current_roles:

                new_role = await guild.create_roles(name=str(j))

                new_roles.append(new_role.name)
                new_roles.append(new_role.id)

        checks.append('yes')

        self.write_to_json(guild)

        return checks

    async def write_to_json(guild):

        with open('master.json', 'r', encoding='utf-8-sig') as old:
            data = json.load(old)

        new_data = {
            str(guild.id) : {
                "guild_name" : str(guild.name),
                "guild_owner" : str(guild.owner.name),
                "guild_owner_id" : str(guild.owner.id),
                "member_count" : str(len([m for m in guild.members if not m.bot])),
                "guild_role_names" : str([r.name for r in guild.roles if not r.managed]),
                "guild_role_ids" : str([r.id for r in guild.roles if not r.managed])
            }
        }

def setup(bot):
    bot.add_cog(UponJoiningServer(bot))