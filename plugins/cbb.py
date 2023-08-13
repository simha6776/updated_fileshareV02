#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from datetime import timedelta, datetime
import pytz
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

india = pytz.timezone("Asia/Kolkata")
global DATEDAY
DATEDAY = []
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
        await query.message.edit_text(text = f"Date change to {DATEDAY}")
    elif data == "tdy":
        DATEDAY.clear()
        tda = datetime.now(india)
        DATEDAY.append(str(tda.strftime("%d - %m - %Y")))
        await query.message.edit_text(text = f"Date change to {DATEDAY}")
    elif data == "tmr":
        DATEDAY.clear()
        tm = datetime.now(india)+timedelta(1)
        DATEDAY.append(str(tm.strftime("%d - %m - %Y")))
        await query.message.edit_text(text = f"Date change to {DATEDAY}")
    else:
        pass
