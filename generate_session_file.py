# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# This script wont run your bot, it just generates a session.

from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv("config.env")

API_KEY = os.environ.get("1258088", None)
API_HASH = os.environ.get("f347197a7883a08674ff1e10011538d7", None)

bot = TelegramClient('userbot', API_KEY, API_HASH)
bot.start()
