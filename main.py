import bot_interface
import asyncio
import conversion
import subprocess
import ffmpeg
import os
from pathlib import Path
from telegram.ext import (ApplicationBuilder,
                          CommandHandler,
                          MessageHandler,
                          CallbackQueryHandler,
                          Application,
                          ContextTypes,
                          filters)
from telegram import (Update,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup)

BOT_TOKEN = "8789621071:AAGwxRv28i9aellHi9Q9ZF3SFR4swc0oESE"
bot_ui = bot_interface.Bot_interface(BOT_TOKEN)
download_directory = "C:\Users\dimas\OneDrive\Desktop\Bot_files"
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

async def video_conversion(update:Update, context:ContextTypes.DEFAULT_TYPE):
    bot_ui.if_video()
    await update.message.reply_text("send a video file to convert")
    message = update.message 
    file = message.document
    filename = file.file_name
    os.makedirs(download_directory, exist_ok = True)
    inputpath = os.path.join(download_directory, filename)
    tgfile = await context.bot.get_file(file.file_id)
    await tgfile.download_to_drive(inputpath)
    await update.message.reply_text("File downloaded, converting...")
    try:
        outputpath = os.path.splitext(inputpath)[0] + f'{bot_ui.output}'
        conv = conversion.Conversion(inputpath, outputpath)
        conv.convert_video_extension()
        with open(outputpath, "rb") as f:
            await update.message.reply_document(f)
        await update.message.reply_text("Converted and sent")
    except subprocess.CalledProcessError:
        await update.message.reply_text("Conversion failed")
    finally:
        if os.path.exists(inputpath):
            os.remove(inputpath)

def main():
    if not BOT_TOKEN:
        raise SystemExit("No bot token provided")
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO|filters.VIDEO|filters.AUDIO))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback_query))