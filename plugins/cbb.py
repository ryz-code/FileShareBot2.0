#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"MADE BY TEAM SANGLIYANA",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                text="Owner", url=f"https://t.me/TEAM_SANGLIYANA"),
                        InlineKeyboardButton(
                text="CH1LD P0RN", url=f"https://t.me/+Vh9XhY9vNZ1jOGE1")
                    ],
                    [
                        InlineKeyboardButton("Close", callback_data = "close")
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
