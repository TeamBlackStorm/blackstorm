# blackstorm - UserBot
# Copyright (C) 2021 TeamBlackStorm
#
# This file is a part of < https://github.com/TeamBlackStorm/blackstorm/ >

# https://github.com/xditya/TeleBot/blob/master/telebot/plugins/mybot/pmbot/incoming.py
"""
Incoming Message(s) forwarder.
"""

from telethon import events

from . import *

# if incoming


@asst.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def on_new_mssg(event):
    who = event.sender_id
    if is_blacklisted(who):
        return
    # doesn't reply to that user anymore
    if event.text.startswith("/") or who == OWNER_ID:
        return
    xx = await event.forward_to(OWNER_ID)
    add_stuff(xx.id, who)
