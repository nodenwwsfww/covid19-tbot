import asyncio

from aiogram import Bot, Dispatcher, executor
from config import API_TOKEN, admin_id

loop = asyncio.get_event_loop()
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

import mysql.connector

class DB:
    mydb = mysql.connector.connect(
        host="localhost",
        port="811",
        user="root",
        password="root"
    )
    mycursor = mydb.cursor()

async def on_shutdown(dp):
    await bot.close()

async def on_startup(dp):
    await bot.send_message(chat_id=admin_id, text='BOT | Successfully started')

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
