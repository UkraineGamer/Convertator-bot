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
download_directory = input(str("Please input file directory for temporary files for conversion: "))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I will assist you with conversion of your files!")
    await update.message.reply_text("Please notice that the files that you convert are not stored on the external device after conversion.")
    await main_choice_handler()

async def main_choice_handler():
    bot_ui.first_choice()
    await conversion_handler()

async def conversion_handler(update:Update, context:ContextTypes.DEFAULT_TYPE):
    conversion_type = str(bot_ui.output)

    if conversion_type == "video":
        bot_ui.if_video()
    elif conversion_type == "audio":
        bot_ui.if_audio()
    elif conversion_type == "image":
        bot_ui.if_image()
    else:
        await message.reply_text("Non exitent option chosen")

    await update.message.reply_text(f"send a {conversion_type} file to convert")
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
        
        if conversion_type == "video":
            conv.convert_video_extension()
        elif conversion_type == "audio":
            conv.convert_audio_extension()
        elif conversion_type == "image":
            conv.convert_image_extension()
        
        with open(outputpath, "rb") as f:
            await update.message.reply_document(f)
        await update.message.reply_text("Converted and sent")

    except subprocess.CalledProcessError:
        await update.message.reply_text("Conversion failed")

    finally:
        if os.path.exists(inputpath):
            os.remove(inputpath)
        if os.path.exists(outputpath):
            os.remove(outputpath)


def main():
    if not BOT_TOKEN:
        raise SystemExit("No bot token provided")
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO|filters.VIDEO|filters.AUDIO, ))
    app.add_handler(CommandHandler("start", start))

    print("Bot is up and running!")
    app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())