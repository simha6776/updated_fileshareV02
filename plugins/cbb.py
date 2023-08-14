#(©)Codexbotz
import time
import aiohttp
import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait
from plugins.data import FOMET, BOTEFITMSG
from plugins.channel_post import list
from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON, OWNER_ID
from helper_func import encode
from pyshorteners import Shortener
import string
import re
from pyrogram import __version__
from bot import Bot
from datetime import timedelta, datetime
import pytz


pic = str(list[-1])
Slink = str(list[-2])
Tlink = str(list[-3])
india = pytz.timezone("Asia/Kolkata")
global DATEDAY
DATEDAY = [1]
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='https://t.me/link_serials'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://t.me/dj_serials_bot'>Click here</a>\n○ Channel : @link_serials\n○ Support Group : @dj_serials_bot</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
            
    elif data == "ystdy":
        DATEDAY.clear()
        ye = datetime.now(india)-timedelta(1)
        DATEDAY.append(str(ye.strftime("%d - %m - %Y")))
        # await query.message.edit_text(text = f"Date change to {DATEDAY}")
        
        e_pic = await client.send_photo(chat_id = query.from_user.id, photo=pic, caption=f"....")
        await time.sleep(3)
        await query.message.edit_text(BOTEFITMSG.format(filname, botfsno[0], Tlink, Slink, DATEDAY[-1]))
        await e_pic.edit(FOMET.format(DATEDAY[-1], Slink, Slink))
    elif data == "tdy":
        DATEDAY.clear()
        tda = datetime.now(india)
        DATEDAY.append(str(tda.strftime("%d - %m - %Y")))
        # await query.message.edit_text(text = f"Date change to {DATEDAY}")

        e_pic = await client.send_photo(chat_id = query.from_user.id, photo=pic, caption=f"....")
        await time.sleep(3)
        await query.message.edit_text(BOTEFITMSG.format(filname, botfsno[0], Tlink, Slink, DATEDAY[-1]))
        await e_pic.edit(FOMET.format(DATEDAY[-1], Slink, Slink))
    elif data == "tmr":
        DATEDAY.clear()
        tm = datetime.now(india)+timedelta(1)
        DATEDAY.append(str(tm.strftime("%d - %m - %Y")))
        # await query.message.edit_text(text = f"Date change to {DATEDAY}")

        e_pic = await client.send_photo(chat_id = query.from_user.id, photo=pic, caption=f"....")
        await time.sleep(3)
        await query.message.edit_text(BOTEFITMSG.format(filname, botfsno[0], Tlink, Slink, DATEDAY[-1]))
        await e_pic.edit(FOMET.format(DATEDAY[-1], Slink, Slink))
    else:
        pass
