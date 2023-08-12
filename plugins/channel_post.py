
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from plugins.data import ODD, EVEN
from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from datetime import datetime, timedelta
from helper_func import encode
import requests
import random
import string
import re

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, message: Message):
    dateexc = datetime.now().strftime("%d")
    media = message.video or message.document
    filname= media.file_name.split("S0")[0]#[1][2]etc
    if int(dateexc) % 2 != 0:
        if filname in media.file_name:
            chtid=int(ODD[filname][3])
            pic=ODD[filname][0]
            SL_URL=ODD[filname][1]
            SL_API=ODD[filname][2]
            e_pic = await client.send_photo(chat_id=chtid, photo=pic, caption=f"🔥please wait....")
            await asyncio.sleep(1)
    elif int(dateexc) % 2 == 0:
        if filname in media.file_name:
            chtid=int(EVEN[filname][3])
            pic=EVEN[filname][0]
            SL_URL=EVEN[filname][1]
            SL_API=EVEN[filname][2]
            e_pic = await client.send_photo(chat_id=chtid, photo=pic, caption=f"🔥please wait....")
            await asyncio.sleep(1)
    else:
        reply_text = await message.reply_text("❌Don't send me messages directly I'm only for serials!")
        
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    Tlink = f"https://telegram.me/{client.username}?start={base64_string}"
    
#    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={Tlink}')]])
    #await reply_text.edit(f"<b>Here is your link</b>\n\n{Tlink}\n\n<code>{Tlink}</code>", reply_markup=reply_markup, disable_web_page_preview = True)
    
    Slink = get_short(SL_URL,SL_API,Tlink)
    await e_pic.edit(FOMET.format(Slink, Slink))
 #   if not DISABLE_CHANNEL_BUTTON:
 #       await post_message.edit_reply_markup(reply_markup)

def aliyas():
    """Generate a random 8-letter alphanumeric string."""
    characters = string.ascii_letters + string.digits
    random_chars = ''.join(random.choice(characters) for _ in range(8))
    return random_chars
    


def get_short(SL_URL,SL_API,Tlink):
    rget = requests.get(f"https://{SL_URL}/api?api={SL_API}&url={Tlink}&alias={aliyas()}")
    rjson = rget.json()
    if rjson["status"] == "success" or rget.status_code == 200:
        return rjson["shortenedUrl"]
    else:
        return url

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={Tlink}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
