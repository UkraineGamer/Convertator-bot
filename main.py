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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text(
            "Send a file to convert, or use the menu when it is available."
        )


async def convert_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    


async def callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query:
        await query.answer()

    if query.data == "convert_audio":
        await convert_audio(update, context)

def main():
    if not BOT_TOKEN:
        raise SystemExit("No bot token provided")
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback_query))