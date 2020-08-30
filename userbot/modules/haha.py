#ported from X-TRA-TELEGRAM by @RoyalBoyPriyanshu


import asyncio
import os
import sys
import random, re
import asyncio
from telethon import events
from userbot.events import register
from asyncio import sleep
import time
from userbot import CMD_HELP



@register(pattern=".muth")

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "muth":

    await event.edit("Starting")

    animation_chars = [

            "8✊️===D",

            "8=✊️==D",

            "8==✊️=D",

            "8===✊️D",

            "8==✊️=D",

            "8=✊️==D",

            "8✊️===D",

            "8===✊️D💦",

            "8==✊️=D💦💦",

            "8=✊️==D💦💦💦",
        
            "The End 😂"

        ]

    for i in animation_ttl:
        
        await asyncio.sleep(animation_interval)
        
        await event.edit(animation_chars[i % 11])
        
@register(pattern=".brain")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 14)
    await event.edit("Starting")
    animation_chars = [    
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
          ]
    for i in animation_ttl:
    	await asyncio.sleep(animation_interval)
    	await event.edit(animation_chars[i %14 ])

@register(pattern=".gf")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 21)
    await event.edit("Starting lol")
    animation_chars = [
            "`Ruk jaa , Abhi teri GF ko Fuck karta hu `",
            "`Making your Gf warm 🔥`",
            "`Pressing her boobs 🤚😘`",
            "`Stimulating her pussy🖕`",
            "`Fingering her pussy 💧😍👅 `",
            "`Asking her to taste my DICK🍌`",
            "`Requested accepted😻💋, Ready to taste my DICK🍌`",
            "`Getting her ready to fuck 👀`",
            "`Your GF Is Ready To Fuck`",
            "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get Red\nTrying new SEX position to make her Squirt\n\nAlmost Done. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get White\nShe squirted like a shower💧💦👅\n\nAlmost Done..\n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get Red\nDoing Extreme SEX with her👄\n\nAlmost Done...\n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's Pussy Get Red\nWarming her Ass🍑 to Fuck!🍑🍑\n\nAlmost Done....\n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's ASS🍑 Get Red\nInserted my Penis🍌 in her ASS🍑\n\nAlmost Done.....\n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's ASS🍑 Get Red\ndoing extreme sex with her\n\nAlmost Done......\n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's Boobs🤚😘 are Awesome\nPressing her tight Nipples🤚👀\n\nAlmost Done.......\n\nFucked Percentage... 84%\n███████████████████▒▒▒▒▒▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's Lips Get Horny\nDoing French Kiss with your GF👄💋\n\nAlmost Done........\n\nFucked Percentage... 89%\n██████████████████████▒▒▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's Boobs🤚😘 are Awesome\nI am getting ready to cum in her Mouth👄\n\nAlmost Done.......\n\nFucked Percentage... 90%\n██████████████████████▒▒▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's Boobs🤚😘 are Awesome\nFinally, I have cummed in her Mouth👅👄\n\nAlmost Done.......\n\nFucked Percentage... 96%\n████████████████████████▒ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's is Awesome\nShe is Licking my Dick🍌 in the Awesome Way✊🤛🤛👅👄\n\nAlmost Done.......\n\nFucked Percentage... 100%\n█████████████████████████ `",
            "`Fucking Your GF😈😈\n\n\nYour GF's ASS🍑 Get Red\nCummed On her Mouth👅👄\n\nYour GF got Pleasure\n\nResult: Now I Have 1 More SEX Partner 👍👍`"
        ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 21])
        
@register(outgoing=True, pattern="^.fuk$")
async def fuck(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╱┏━━━┓.. ┏┓╱┏┓╭━━━╮ ╱╱┏┓ `"
                     "`\n╱┃┏━━┛.. ┃┃╱┃┃┃╭━╮┃╱┃┃ `"
                     "`\n╱┃┗━┓╱.. ┃┃╱┃┃┃┃╱┗┛┃┃ `"
                     "`\n╱┃┏━┛╱...┃┃╱┃┃┃┃╱┏┓┃┃ `"
                     "`\n╱┃┃╱.╱.╱ ┃╰━╯┃┃╰━╯┃╱┃┃ `"
                     "`\n╱┗┛╱ ╱ ╱ ╰━━━╯╰━━━╯ ╱╱┗┛ `")


CMD_HELP.update({
  "nope":
   "`.muth`\
\nUsage: Find yourself.\
\n\n`.brain`\
\nUsage: Your dump brain.\
\n\n`gf`\
\nUsage:Fu*cing your gf.\
\n\n`.fuk`\
\nUsage:Fuck!!"
})            
