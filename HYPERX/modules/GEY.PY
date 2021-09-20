import os
import time
import string
import random
import datetime
import aiofiles
import asyncio
import traceback
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

from HYPERX import MONGO_DB_URI

LOG_CHANNEL = -1001548069995

db = Database(MONGO_DB_URI, HYPERxGROUP_BOT)

async def handle_user_status(bot, cmd):
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"**📣 Notification** \n\n#NEW_USER **start use your bot!** \n\nFirst name: `{cmd.from_user.first_name}` \nUser id: `{cmd.from_user.id}` \nProfile link: [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})"
        )

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
                datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text(f"sorry, you're banned, ask in @{GROUP_SUPPORT} if you think this was an mistake.", quote=True)
            return
    await cmd.continue_propagation()
