
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
with TelegramClient(
    StringSession(), 
    APP_ID, 
    API_HASH
) as client:
    session_str = client.session.save()
    s_m = client.send_message("me", session_str)
    s_m.reply("⬆️This StringSession is generated\nNow set var `STRING_SESSON` \nif u need any help ask in @remixsupport")
    print("please check your Telegram Saved Messages for the StringSession ")
