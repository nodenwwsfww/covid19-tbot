from main import bot, dp

from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Command, Text
from random import choice
from COVID19Py import COVID19
covid19 = COVID19()

start_markup = ReplyKeyboardMarkup(row_width=2)
button_news = KeyboardButton('📨Новости')
button_stats = KeyboardButton('📈Статистика')
button_help = KeyboardButton('🆘Помощь')
button_random_tip = KeyboardButton('🎲Случайный совет')
start_markup.row(button_news, button_stats)
start_markup.row(button_help, button_random_tip)

@dp.message_handler(commands=['start'])
async def send_start_message(message:Message):
    text = f"Привет, {message.from_user.first_name}!\n" \
           f"Я {(await bot.get_me()).first_name} — твой помощник в борьбе с коронавирусом"
    await message.answer(text, reply_markup=start_markup)

@dp.message_handler(Text(equals=["📨Новости", "📈Статистика", "🆘Помощь", "🎲Случайный совет"]))
async def menu_switch_handler(message: Message):

    if message.text == '📨Новости':
        await send_news_message(message)

    elif message.text == '📈Статистика':
        await send_statistic_message(message)

    elif message.text == '🆘Помощь':
        await send_help_message(message)

    elif message.text == '🎲Случайный совет':
        await send_random_tip(message)

@dp.message_handler(Command('news'))
async def send_news_message(message: Message):
    pass

@dp.message_handler(Command('statistic'))
async def send_statistic_message(message: Message):
    data = covid19.getAll(timelines=True)
    latest = data['latest']
    changes = covid19.getLatestChanges()

    text_line_first = 'Статистика распространения коронавируса по всему миру\n\n'
    text_line_second = f"Подтверждённых случаев: {latest[0]['confirmed']} (+{changes['confirmed']})"
    text_line_third = f"\nСмертей: {latest['deaths']} (+{changes['deaths']})"
    text_line_fourth = f"\nВыздоровлений: {latest['recovered']}(+{changes['recovered']})\n\n"
    await message.answer(text=text_line_first + text_line_second + text_line_third + text_line_fourth)

@dp.message_handler(Command('help'))
async def send_help_message(message: Message):
    text = "Список команд:" \
           "\n/menu — Меню\n/news — Новости\n/stats — Статистика\n" \
           "/help — Помощь\n/tip — Случайный совет"

    await message.answer(text=text)

@dp.message_handler(Command('tip'))
async def send_random_tip(message: Message):
    useful_tips = ["stickers/AvoidCrowds.tgs", "stickers/DontTouchYourFace.tgs", "stickers/HomeAlone.tgs"
                                                                                 "stickers/KeepDistance.tgs",
                   "stickers/KeepThemSafe.tgs", "stickers/NoHugs.tgs",
                   "stickers/StayHome.tgs", "stickers/WashYourHands.tgs"]

    sticker = open(choice(useful_tips), 'rb')
    await bot.send_sticker(message.from_user.id, sticker)