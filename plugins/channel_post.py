#(©)Codexbotz
import aiohttp
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait
from plugins.data import ODD, EVEN ,BOTEFITMSG, FOMET
from plugins.cbb import DATEDAY
from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from datetime import datetime
from helper_func import encode
from pyshorteners import Shortener
import string
import re


SAPI = "c5dbea7703b576144630660355aaa3dbd3a59cc5"
SSLINK = "upshrink.com"
@Client.on_message(filters.private & filters.user(ADMINS) & filters.command(["date"]))
async def date(bot, message):
    dat = await message.reply_text("Select Date.........",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
        			InlineKeyboardButton("Today",callback_data = 'tdy'), 
        			InlineKeyboardButton("Tommorow",callback_data='tmr') ]]))

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.text & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, message: Message):
    current_time = datetime.now()
    media = message.video or message.document
    # filname= media.file_name.split("S0")[0]#[1][2]etc
    ############# FOR UTSAV BOT ##################
    #filname = re.split("S\d", media.file_name)[0]#[1][2]etc
    ############# FOR DS BOT ##################
    filname = re.split(current_time.strftime("%B"), media.file_name)[0]#[1][2]etc
    #botfsno= re.findall("S0.+E\d+\d", media.file_name)
    if int(DATEDAY[-1][0:2]) % 2 != 0:#chaeking for ODD by given date
        if filname in ODD.keys():
            # chtid=int(ODD[filname][3])
            pic=ODD[filname][0]
            SL_URL=ODD[filname][1]
            SL_API=ODD[filname][2]
            bot_msg = await message.reply_text("Please Wait...!", quote = True, disable_web_page_preview = True)
            await asyncio.sleep(1)
        elif media.file_name in media.file_name:
            bot_msg = await message.reply_text("Please Wait...!", quote = True)
            link = await conv_link(client , message)
            sslink= await get_short(SSLINK, SAPI, link)
            await bot_msg.edit(f"<b>Here is your link</b>\n\n{link}\n\n<code>{link}</code>\n\nShort Link\n<code>{sslink}</code>")
        else:
            reply_text = await message.reply_text("❌Don't send me messages directly I'm only for serials!")
            
    elif int(DATEDAY[-1][0:2]) % 2 == 0:#chaeking for EVEN by given date
        if filname in EVEN.keys():
            # chtid=int(EVEN[filname][3])
            pic=EVEN[filname][0]
            SL_URL=EVEN[filname][1]
            SL_API=EVEN[filname][2] 
            bot_msg = await message.reply_text("Please Wait...!", quote = True, disable_web_page_preview = True)
            await asyncio.sleep(1)
        elif media.file_name in media.file_name:
            bot_msg = await message.reply_text("Please Wait...!", quote = True)
            link = await conv_link(client , message)
            sslink= await get_short(SSLINK, SAPI, link)
            await bot_msg.edit(f"<b>Here is your link</b>\n\n{link}\n\n<code>{link}</code>\n\nShort\n<code>{sslink}</code>")
        else:
            reply_text = await message.reply_text("❌Don't send me messages directly I'm only for serials!")
            
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
    Slink = await get_short(SL_URL, SL_API, Tlink)
    await bot_msg.edit("Analysing..!")
    await asyncio.sleep(1)
    await bot_msg.edit("Editing..!")
    await bot_msg.edit("Trying to send Poster.. ▣ ▢ ▢")
    await asyncio.sleep(1)
    await bot_msg.edit("Trying to send Poster.. ▣ ▣ ▢")
    await asyncio.sleep(1)
    await bot_msg.edit("Trying to send Poster.. ▣ ▣ ▣")
    await asyncio.sleep(1)
    if len(DATEDAY) != 0:
        await bot_msg.edit("Poster sent successfully...!")
        e_pic = await client.send_photo(chat_id=int(-1001956515516), photo=pic, caption= FOMET.format(DATEDAY[-1], Slink, Slink))
        #await bot_msg.edit(BOTEFITMSG.format(filname, botfsno[0], Tlink, Slink, DATEDAY[0]))
        await bot_msg.edit(BOTEFITMSG.format(filname, Tlink, Slink, DATEDAY[0]))
    else:
        await bot_msg.edit("Invalid DATE, Please set DATE again /date...?")
    
async def get_short(SL_URL, SL_API, Tlink):
    # FireLinks shorten
    try:
        api_url = f"https://{SL_URL}/api"
        params = {'api': SL_API, 'url': Tlink}
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, params=params, raise_for_status=True) as response:
                data = await response.json()
                url = data["shortenedUrl"]
        return url
    except Exception as error:
        return error

async def conv_link(client , message):
    try:
       post_message = await message.copy(chat_id = CHANNEL_ID, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = CHANNEL_ID, disable_notification=True)
    except Exception as e:
        print(e) 
        await client.send_message(message.chat.id, "Somthing is Wrong")
    converted_id = post_message.id * abs(CHANNEL_ID)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    # await client.send_massage(message.chat.id , f"<b>Here is your link</b>\n\n{link}\n\n<code>{link}</code>", disable_web_page_preview = True)
    return link
    
@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_id = message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://telegram.me/share/url?url={link}')]])
    try:
        await message.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
