from telethon import events, Button, custom
import re, os
from HYPERX.events import register
from HYPERX import telethn as tbot
from HYPERX import telethn as tgbot
PHOTO = "https://telegra.ph/file/71406119a6df4203ffb44.jpg"
@register(pattern=("/alive"))
async def awake(event):
  HYPERx = event.sender.first_name
  HYPERX = "🔥𝐇𝐄𝐋𝐋𝐎 𝐓𝐇𝐈𝐒 𝐈𝐒 𝙷𝚈𝙿𝙴𝚁 𝐗🔥 \n\n"
  HYPERX += "𝐀𝐋𝐋 𝐒𝐘𝐒𝐓𝐄𝐌 𝐖𝐎𝐑𝐊𝐈𝐍𝐆 𝐏𝐑𝐎𝐏𝐄𝐑𝐋𝐘\n\n"
  HYPERX += "𝐅𝐔𝐋𝐋 𝐔𝐏𝐃𝐀𝐓𝐄𝐃\n\n"
  HYPERX += "𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 : 𝟭.𝟮𝟯.𝟬 𝐋𝐀𝐓𝐄𝐒𝐓\n\n"
  HYPERX += "𝐓𝐇𝐀𝐍𝐊𝐒 𝐅𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐄 𝐇𝐄𝐑𝐄"
  BUTTON = [[Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", "https://t.me/HYPER_X_SUPPORT"), Button.url("𝐔𝐏𝐃𝐀𝐓𝐄𝐒", "https://t.me/HYPERx_UPDATES")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=HYPERX,  buttons=BUTTON)


__mod_name__ = "Alive⚜️"
