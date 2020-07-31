# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP

@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Module doesn't exist or Module name is invalid**")
    else:
<<<<<<< HEAD
        await event.edit("**All modules are listed below**\
            \nUsage: Type `.help` <module name> to know how it works")
=======
        await event.edit(f"**All modules are listed below**\
            \nUsage: Type `.help <module name>` to know how it works\
            \nModules loaded: {len(modules)}")
>>>>>>> d847fc158c1bbb5f61b05efe746a6102f64d49ef
        string = ""
        for i in sorted(CMD_HELP):
            string += "`" + str(i)
            string += "`  ⍋  "
        await event.reply(string)
