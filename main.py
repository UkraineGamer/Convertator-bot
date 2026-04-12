import bot_interface
import asyncio
import conversion
import subprocess
import ffmpeg
from pathlib import Path
from telegram.ext import (ApplicationBuilder,
                          CommandHandler,
                          MessageHandler,
                          CallbackQueryHandler,
                          Application,
                          ContextTypes)
from telegram import (Update,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup)

BOT_TOKEN = "8789621071:AAGwxRv28i9aellHi9Q9ZF3SFR4swc0oESE"
bot_ui = bot_interface.Bot_interface(BOT_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Send a file to convert, or use the menu when it is available."
        )

async def main_choice_handler():
    bot_ui.first_choice()
    if str(bot_ui.output) == 'video':
        video_conversion()
    elif str(bot_ui.output) == 'audio':
        audio_conversion()
    elif str(bot_ui.output) == 'image':
        image_conversion()
    

def main():
    if not BOT_TOKEN:
        raise SystemExit("No bot token provided")
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback_query))