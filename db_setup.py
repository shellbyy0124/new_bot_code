# import sqlite3


# """
# CREATE TABLES
# """

# with sqlite3.connect('main.db') as main_db:

#     main_db.execute('''
#         CREATE TABLE IF NOT EXISTS guild_id(
#             guild_id INT PRIMARY,
#             guild_name TEXT
#         );
#         CREATE TABLE IF NOT EXISTS member_ids(
#             member_id INT PRIMARY,
#             member_name TEXT,
#             member_nick TEXT,
#             member_roles TEXT
#         );
#         CREATE TABLE IF NOT EXISTS  text_channels(
#             channel_id INT PRIMARY
#         );
#         CREATE TABLE IF NOT EXISTS  voice_channels(
#             voice_chan_id INT PRIMARY
#         );
#         CREATE TABLE IF NOT EXISTS roles(
#             role_name INT PRIMARY
#         );
#     );''')

#     main_db.commit()

# with sqlite3.connect('main.db') as main_db:

    # table_names = ['guild_id', 'member_ids', 'text_channels', 'voice_channels', 'roles']
    # variable_information = ['guild_id', 'guild_name', 'member_id', 'member_name', 'member_nick', 'member_roles', 'channel_id', 'voice_chan_id', 'role_id']
    
    # counter = 0
    # cursor = main_db.cursor()

    # for name in table_names:
    #     for info in variable_information:
            
    #         if str(name[counter]).startswith('guild'):
      
    #             sql = cursor.execute('''
    #                 CREATE TABLE IF NOT EXISTS '%s'(
    #                     {} INT,
    #                     {} TEXT
    #                 );''').__format__(info[0], info[1])
                    
    #             val_name = (str(name[counter]),)
    #             val = (info[0], info[1],)
    #             cursor.execute(sql, val_name, val)
    #             cursor.close()
    #             counter += 1

    #         elif str(name[counter]).startswith('member'):
                
    #             sql = cursor.execute('''CREATE TABLE IF NOT EXISTS ?(VALUES (?, ?, ?, ?,));''')
    #             val_name = (str(name[counter]),)
    #             val = (info[2], info[3], info[4], info[5],)
    #             cursor.execute(sql, val_name, val)
    #             cursor.close()
    #             counter += 1

    #         elif str(name[counter]).startswith('channel'):
                
    #             sql = cursor.execute('''CREATE TABLE IF NOT EXISTS ?(VALUES (?,));''')
    #             val_name = (str(name[counter]),)
    #             val = (info[6],)
    #             cursor.execute(sql, val_name, val)
    #             cursor.close()
    #             counter += 1

    #         elif str(name[counter]).startswith('voice'):
                
    #             sql = cursor.execute('''CREATE TABLE IF NOT EXISTS ?(VALUES (?,));''')
    #             val_name = (str(name[counter]),)
    #             val = (info[7],)
    #             cursor.execute(sql, val)
    #             cursor.close()
    #             counter +=1

    #         elif str(name[counter]).startswith('role'):
                
    #             sql = cursor.execute('''CREATE TABLE IF NOT EXISTS ?(VALUES (?,));''')
    #             val_name = (str(name[counter]),)
    #             val = (info[7],)
    #             cursor.execute(sql, val)
    #             cursor.close()
    #             counter += 1