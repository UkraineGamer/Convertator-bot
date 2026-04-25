import bot_interface
import conversion
import subprocess
import os
from telegram.ext import (ApplicationBuilder,
                          CommandHandler,
                          MessageHandler,
                          CallbackQueryHandler,
                          ContextTypes,
                          filters)
from telegram import (Update,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup)

BOT_TOKEN = "8789621071:AAGwxRv28i9aellHi9Q9ZF3SFR4swc0oESE"
bot_ui = bot_interface.Bot_interface()
download_directory = os.getenv("DOWNLOAD_DIRECTORY", "tmp_downloads")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello, I will assist you with conversion of your files!")
    await update.message.reply_text("Please notice that the files that you convert are not stored on the external device after conversion.")
    bot_ui.output_clear()
    keyboard = bot_ui.first_choice(InlineKeyboardButton, InlineKeyboardMarkup)
    await update.message.reply_text("Please choose what you want to convert:", reply_markup=keyboard)


async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data or ""

    if data.startswith("type:"):
        conversion_type = data.split(":", maxsplit=1)[1]
        keyboard = bot_ui.extension_choice(conversion_type, InlineKeyboardButton, InlineKeyboardMarkup)
        await query.edit_message_text(
            text="Please choose the extension you want to convert to",
            reply_markup=keyboard,
        )
        return

    if data.startswith("ext:"):
        target_ext = data.split(":", maxsplit=1)[1]
        bot_ui.set_extension(target_ext)
        await query.edit_message_text(
            text=f"Send a {bot_ui.conversion_type} file to convert to {bot_ui.output}"
        )


async def conversion_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    conversion_type = bot_ui.conversion_type
    target_ext = bot_ui.output
    if not conversion_type or not target_ext:
        await update.message.reply_text("Please run /start and choose conversion options first.")
        return

    message = update.message
    tg_media = None
    filename = None

    if message.video:
        tg_media = message.video
        filename = message.video.file_name
    elif message.audio:
        tg_media = message.audio
        filename = message.audio.file_name
    elif message.photo:
        tg_media = message.photo[-1]
        filename = "photo.jpg"

    if not tg_media:
        await update.message.reply_text("Send a supported file: video, audio, or photo.")
        return

    if not filename:
        filename = "input_file.bin"

    os.makedirs(download_directory, exist_ok=True)
    inputpath = os.path.join(download_directory, filename)
    outputpath = os.path.splitext(inputpath)[0] + target_ext

    telegram_file = await context.bot.get_file(tg_media.file_id)
    await telegram_file.download_to_drive(inputpath)
    await update.message.reply_text("File downloaded, converting...")

    try:
        conv = conversion.Conversion(inputpath, outputpath)
        
        if conversion_type == "video":
            conv.convert_video_extension()
        elif conversion_type == "audio":
            conv.convert_audio_extension()
        elif conversion_type == "image":
            conv.convert_image_extension()
        else:
            await update.message.reply_text("Unsupported conversion type selected.")
            return

        with open(outputpath, "rb") as converted_file:
            await update.message.reply_document(converted_file)
        await update.message.reply_text("Converted and sent")
        bot_ui.output_clear()
    except (subprocess.CalledProcessError, FileNotFoundError):
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
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(callback_handler))
    app.add_handler(MessageHandler(filters.VIDEO | filters.AUDIO | filters.PHOTO, conversion_handler))

    print("Bot is up and running!")
    app.run_polling()

if __name__ == "__main__":
    main()
