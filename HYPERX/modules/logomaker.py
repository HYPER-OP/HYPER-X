from HYPERX.events import register
from HYPERX import OWNER_ID
from HYPERX import telethn as tbot
import os 
from PIL import Image, ImageDraw, ImageFont
import shutil 
import random
import wget
import glob
import time
from telethon.tl.types import InputMessagesFilterPhotos
TMP_DOWNLOAD_DIRECTORY = "./"


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SHINCHAN = ( "https://telegra.ph//file/111fd979e87e9f42f2c19.jpg", "https://telegra.ph//file/bfc0b1f66bf5a8b2c574c.jpg", "https://telegra.ph//file/cd2d1696620339084624c.jpg", "https://telegra.ph//file/bfc0b1f66bf5a8b2c574c.jpg", "https://telegra.ph//file/9ab646f7cf3c126495fbe.jpg", "https://telegra.ph//file/32456d888874c75ed29ee.jpg", "https://telegra.ph//file/c60bc9d86aa541a4df3dd.jpg", "https://telegra.ph//file/548ad05d1b525f523f321.jpg", "https://telegra.ph//file/2e6d3c6e3e4e674d5c0df.jpg", "https://telegra.ph//file/87af3475150eee832402d.jpg", "https://telegra.ph//file/a5b6ec4221d9bcc191c7d.jpg", "https://telegra.ph//file/d7003a9ce86a9b1f874a0.jpg", "https://telegra.ph//file/8226be18c2202cd1769e1.jpg", "https://telegra.ph//file/c4cddc6bd4977d6fd0915.jpg", "https://telegra.ph//file/81f30d3778e3045ebaac0.jpg", "https://telegra.ph//file/592ef483d76dcb7b1f8a1.jpg", "https://telegra.ph//file/2a0db95a8abc2b463437d.jpg", "https://telegra.ph//file/9e848a13cfab0611b3e63.jpg", "https://telegra.ph//file/1adb8ca9f3f558612ff00.jpg", "https://telegra.ph//file/ab0e4b42cf57a77ed58b3.jpg", "https://telegra.ph//file/e3bcad1d7bc01cb5372cc.jpg", "https://telegra.ph//file/c275505d38b8373fb8391.jpg", "https://telegra.ph//file/de62b9753f6689a7bfc77.jpg", "https://telegra.ph//file/dfd4074f97aa65742c25b.jpg", "https://telegra.ph//file/d188ad5fe891110ed8817.jpg", "https://telegra.ph//file/01bdfd9e85356862fd073.jpg", "https://telegra.ph//file/4dda10ab3bc3e02b4a3db.jpg", "https://telegra.ph//file/b8e13cd5ad49adcba46c0.jpg", "https://telegra.ph//file/b87d6bfdfdae591f45194.jpg", "https://telegra.ph//file/73a6ac7d3a3f040f85cdf.jpg", "https://telegra.ph//file/a4a04eebb4e221756245f.jpg", "https://telegra.ph//file/d2f6c27c471b451553be4.jpg", "https://telegra.ph//file/ed7f1f3139161cfe0ed7c.jpg", "https://telegra.ph//file/98709b420a05e58a4a1d5.jpg", "https://telegra.ph//file/0819127d4bf204b442d03.jpg", "https://telegra.ph//file/c5b54f42e7e0d9f6845c0.jpg", "https://telegra.ph//file/4b934457155bb60b10e6d.jpg", "https://telegra.ph//file/c31c37db2f7599829fcdc.jpg", "https://telegra.ph//file/e26c4f5e617056631032e.jpg", "https://telegra.ph//file/0f8b26570916d6c1d271d.jpg", "https://telegra.ph//file/fc55e688c200c944309c2.jpg", "https://telegra.ph//file/e36a163b460fb3c4b1692.jpg", "https://telegra.ph//file/b79604dfe25fcaff9bf4c.jpg", "https://telegra.ph//file/45caa3f45d7ed06a4b3ad.jpg", "https://telegra.ph//file/e5ee9ec14bb2868624a0b.jpg", "https://telegra.ph//file/0ce7f065eab79ab9d81fe.jpg", "https://telegra.ph//file/107dec6648489ec8219d2.jpg", "https://telegra.ph//file/37bc0c69374182d707d94.jpg", "https://telegra.ph//file/79f5b1b6d02f556963c4a.jpg", "https://telegra.ph//file/9f5a8e68a11495d5aa985.jpg", "https://telegra.ph//file/9e3b72b58927e13af6f46.jpg", "https://telegra.ph//file/137fc30c4605701fb65ea.jpg", "https://telegra.ph//file/7f16afd5b2a176a2d4057.jpg", "https://telegra.ph//file/bfafc5ab6c603b52f7677.jpg", "https://telegra.ph//file/c6943610b5e7648eb89f2.jpg", "https://telegra.ph//file/e38cce2ba228bfd47e0ae.jpg", "https://telegra.ph//file/95fb15423efd9826d7d50.jpg", "https://telegra.ph//file/5bcb0f847784c02951662.jpg", "https://telegra.ph//file/2b18905814111143fd471.jpg", "https://telegra.ph//file/536d6cd8d6c841f76c9a9.jpg", "https://telegra.ph//file/0de407e5b1738111187af.jpg", "https://telegra.ph//file/01bb952ca835c0a7fec07.jpg")

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:
     
    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    gey = random.choice(SHINCHAN)
    geyper = wget.download(gey)
    fnt = "./HYPERX/resources/Chopsic.otf"
    text = event.pattern_match.group(1)
    if len(text) <= 8:
        font_size_ = 100
        strik = 10
    elif len(text) >= 9:
        font_size_ = 50
        strik = 5
    else:
        font_size_ = 100
        strik = 20
    if not text:
        await event.reply("**Give some text to make a logo !!**")
    img = Image.open(geyper)
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "black"
    font = ImageFont.truetype(fnt, font_size_)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2)
    draw.text((x, y), text, font=font, fill="white", stroke_width=strik, stroke_fill="black")
    fname2 = "LogoByhyperx.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption=" 𝗠𝗔𝗗𝗘 𝗕𝗬 🔥 [𝙷𝚈𝙿𝙴𝚁𝐗](https://t.me/HYPER_X_SUPPORT)")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @HYPER_X_SUPPORT, {e}')


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
 ❍ /logo text :  Create your logo with your name

 """
__mod_name__ = "Logo"
