import sqlite3
import datetime
import discord
import json

from discord.ext import commands
from cryptography.fernet import Fernet

intents = discord.Intents.all()



with open('master.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

token = data["token"]

def get_prefix(bot, msg):

    with open('master.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)

    try:

        return data["guilds"][str(msg.guild.id)]["cp"]
    
    except:

        return data["default_cp"]

bot = commands.Bot(command_prefix=get_prefix, intents=intents)

@bot.event
async def on_ready():

    cogs = [
        "cogs.announce",
        "cogs.magk8blal",
        "cogs.matheq",
        "cogs.onjoin",
        "cogs.trans_words_sentences"
    ]

    try:
        
        for cog in cogs:

            bot.load_extension(cog)
            print(f'{cog} loaded')

    except:

        for cog in cogs:
            
            bot.reload_extension(cog)
            print(f'{cog} reloaded')

    print('online')

@bot.event
async def on_message(message):

    guild = message.guild.id

    with sqlite3.connect('main.db') as main_db:

        cursor = main_db.cursor()
        sql = 'SELECT guild_id FROM guild_info WHERE guild_id = ?'
        val = (message.guild.id,)
        cursor.execute(sql, val)
        result_one = cursor.fetchone()

        if result_one is not None:

            sql = 'SELECT member_id FROM member_info WHERE member_id = ?'
            val = (message.author.id)
            cursor.execute(sql, val)
            result_two = cursor.fetchone()

            if result_two is not None:

                start_of_conv_log = datetime.datetime.now().__format__('%m/%d/%y_%H:%M:%S')

                sql = 'SELECT {} FROM conversation_info WHERE date = ?'
                val =(str(start_of_conv_log))

                cursor.execute(sql, val)
                result = cursor.fetchone()

                with open('keys.key', 'r+') as new_key_file:
                    key = new_key_file.read()

                if key != '':

                    f = Fernet(str(key).encode())

                    new_message = f.encrypt(message)

                    try:

                        sql = 'INSERT INTO conversation_info WHERE date = ?'
                        val =  (new_message,)

                        cursor.execute(sql, val)
                        cursor.commit()
                        cursor.close()

                    except:

                        sql = 'UPDATE conversation_info ' # something else goes here
                        val = (new_message,)
                        cursor.execute(sql, val)
                        cursor.commit()
                        cursor.close()

                    with open(f'./convo_logs/{str(datetime.datetime.today())}.txt', 'a+') as convo_logs:
                        current_logs = convo_logs.read()

                        message_info = {
                            f"message_author_id: {message.author.id}\n"
                            f"message_author_name: {message.author.name}"
                            f"message_created_at: {message.created_at}"
                            f"message_content: {message.content}"
                        }

                        current_logs.write(message_info+'\n')

                else:

                    key = Fernet.generate_key()

                    with open('keys.key', 'w') as new_key_file:
                        new_key = new_key_file.read()

                    if new_key == '':

                        new_key.write(key.decode('utf8'))


if __name__ == '__main__':

    bot.run(token)