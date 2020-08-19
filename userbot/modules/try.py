import io
import math
from PIL import Image
import urllib.request
from userbot.events import register
from userbot import bot, CMD_HELP
from os import remove
#
@register(pattern="^.mff(?: |$)(.*)", outgoing=True)
async def flipsticker(event):
    reply = await event.get_reply_message()

    if reply and reply.sticker:
        sticker_webp_data = reply.sticker
    else:
        await event.reply("Reply to a sticker to flip that bitch!")
        return

    sticker_webp_io = io.BytesIO()
    await event.client.download_media(sticker_webp_data, sticker_webp_io)
    sticker_webp = Image.open(sticker_webp_io)
    sticker_webp = ImageOps.mirror(sticker_webp)
    sticker_flipped_io = io.BytesIO()
    sticker_webp.save(sticker_flipped_io, "WebP")
    sticker_flipped_io.name = "sticker.webp"
    sticker_flipped_io.seek(0)
    await event.reply(file=sticker_flipped_io)
CMD_HELP.update({
  "stkrflip":
  ".stkrflip\
\nUsage:flip sticker."
})
