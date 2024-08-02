import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import aiohttp

API_TOKEN = "5864062978:AAGqnnoeFr0n9oLPUpc9am8yzbl5JhzMT20"
API_URL = "http://web:8000/api/v1/messages/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def fetch_messages():
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as resp:
            messages = await resp.json()
            return messages


@dp.message(Command("start", "help"))
async def send_welcome(message: types.Message):
    await message.answer("Hi!\nI'm your bot!\nUse /messages to see all messages.")


@dp.message(Command("messages"))
async def list_messages(message: types.Message):
    messages = await fetch_messages()
    response = "\n".join([f"{msg['user']}: {msg['text']}" for msg in messages])
    await message.answer(response)


if __name__ == "__main__":
    dp.run_polling(bot)
