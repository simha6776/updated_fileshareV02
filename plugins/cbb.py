#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
import pytz
import time
import asyncio
from config import OWNER_ID
from datetime import datetime, timedelta
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

global DATEDAY
DATEDAY = []
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    india = pytz.timezone("Asia/Kolkata")
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='https://t.me/kannada_serials_hdd'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://t.me/dj_serials_bot'>Click here</a>\n○ Channel : @link_serials\n○ Support Group : @dj_serials_bot</b>",
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
        await query.message.edit_text(text = f"<b>Date change to :'{DATEDAY[-1]}'</b>", reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
        			InlineKeyboardButton("Today",callback_data = 'tdy'), 
        			InlineKeyboardButton("Tommorow",callback_data='tmr') ]]))
        #await asyncio.sleep(600)
        #DATEDAY.clear()
    elif data == "tdy":
        DATEDAY.clear()
        tda = datetime.now(india)
        DATEDAY.append(str(tda.strftime("%d - %m - %Y")))
        await query.message.edit_text(text = f"<b>Date change to :'{DATEDAY[-1]}'</b>", reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
        			InlineKeyboardButton("Today",callback_data = 'tdy'), 
        			InlineKeyboardButton("Tommorow",callback_data='tmr') ]]))
        #await asyncio.sleep(600)
        #DATEDAY.clear()
    elif data == "tmr":
        DATEDAY.clear()
        tm = datetime.now(india)+timedelta(1)
        DATEDAY.append(str(tm.strftime("%d - %m - %Y")))
        await query.message.edit_text(text = f"<b>Date change to :'{DATEDAY[-1]}'</b>", reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Yesterday",callback_data='ystdy'), 
        			InlineKeyboardButton("Today",callback_data = 'tdy'), 
        			InlineKeyboardButton("Tommorow",callback_data='tmr') ]]))
        #await asyncio.sleep(600)
        #DATEDAY.clear()
    else:
        pass
        
