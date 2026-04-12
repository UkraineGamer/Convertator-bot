import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

bot = Bot(token="8789621071:AAGwxRv28i9aellHi9Q9ZF3SFR4swc0oESE")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Video", callback_data="click"),
        InlineKeyboardButton(text="Audio", callback_data="audio")]
    ])
    await message.answer("Please choose what you want to convert", reply_markup=keyboard)


@dp.callback_query()
async def handle_callback(callback):
    if callback.data == "click":
        await callback.answer()
        await callback.message.answer("Send me your video which you want to convert")
    if callback.data == "audio":
        await callback.answer()
        await callback.message.answer("Send me your audio which you want to convert")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())