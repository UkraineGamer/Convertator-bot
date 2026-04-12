import telegram
import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

bot = Bot(token="8789621071:AAGwxRv28i9aellHi9Q9ZF3SFR4swc0oESE")
dp = Dispatcher()

class Bot_interface:
    def __init__(self, bot):
        self.bot = bot
        self.dp = Dispatcher()
        self.output = ''

    async def first_choice(self):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Video", callback_data="video"),
            InlineKeyboardButton(text="Audio", callback_data="audio"),
            InlineKeyboardButton(text="Image", callback_data="image")]
        ])
        await self.bot.send_message(chat_id=self.chat_id, text="Please choose what you want to convert", reply_markup=keyboard)

        @dp.callback_query()
        async def handle_callback(callback):
            if callback.data == "video":
                self.output = 'video'
            if callback.data == 'audio':
                self.output = 'audio'
            if callback.data == 'image':
                self.output = 'image'


    async def if_video(self):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=".MP4", callback_data=".mp4"),
            InlineKeyboardButton(text=".MOV", callback_data=".mov"),
            InlineKeyboardButton(text=".MKV", callback_data=".mkv")]
        ])
        await self.bot.send_message(chat_id=self.chat_id, text="Please choose the extension you want to convert to", reply_markup=keyboard)
        @dp.callback_query()
        async def handle_callback(callback):
            if callback.data == ".mp4":
                self.output = '.mp4'
            if callback.data == ".mov":
                self.output = '.mov'
            if callback.data == ".mkv":
                self.output = '.mkv'


    async def if_image(self):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=".JPG", callback_data=".jpg"),
            InlineKeyboardButton(text=".JPEG", callback_data=".jpeg"),
            InlineKeyboardButton(text=".PNG", callback_data=".png")]
        ])
        await self.bot.send_message(chat_id=self.chat_id, text="Please choose the extension you want to convert to", reply_markup=keyboard)
        @dp.callback_query()
        async def handle_callback(callback):
            if callback.data == ".jpg":
                self.output = '.jpg'
            if callback.data == ".jpeg":
                self.output = '.jpeg'
            if callback.data == ".png":
                self.output = '.png'


    async def if_audio(self):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=".MP3", callback_data=".mp3"),
            InlineKeyboardButton(text=".AAC", callback_data=".acc"),
            InlineKeyboardButton(text=".OGG", callback_data=".ogg")]
        ])
        await self.bot.send_message(chat_id=self.chat_id, text="Please choose the extension you want to convert to", reply_markup=keyboard)
        @dp.callback_query()
        async def handle_callback(callback):
            if callback.data == ".mp3":
                self.output = '.mp3'
            if callback.data == ".acc":
                self.output = '.acc'
            if callback.data == ".ogg":
                self.output = '.ogg'

    async def output_clear(self):
        self.output = ''



# @dp.message(Command("start"))
# async def start(message: Message):
#     keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="Video", callback_data="click"),
#         InlineKeyboardButton(text="Audio", callback_data="audio")]
#     ])
#     await message.answer("Please choose what you want to convert", reply_markup=keyboard)


# @dp.callback_query()
# async def handle_callback(callback):
#     if callback.data == "click":
#         await callback.answer()
#         await callback.message.answer("Send me your video which you want to convert")
#     if callback.data == "audio":
#         await callback.answer()
#         await callback.message.answer("Send me your audio which you want to convert")

# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())