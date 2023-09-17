from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from newsapi import NewsApiClient  # Додайте цей імпорт

bot = Bot(token='5934353266:AAFbnT36znbxiLsaqixCl20VXA7jQmTC-7c')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

newsapi = NewsApiClient(api_key='71e6bb489ba6419db09e2fa33fcfabca')


@dp.message_handler(Command('start'))
async def start_button(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('/news'))
    keyboard.add(KeyboardButton('/watchnews'))
    await message.reply("Натисніть кнопку 'News', щоб подивитися новини.", reply_markup=keyboard)

@dp.message_handler(Command('news'))
async def send_news(message: types.Message):
    top_headlines = newsapi.get_top_headlines(sources='techcrunch')

    if top_headlines['totalResults'] > 0:
        for article in top_headlines['articles']:
            await message.reply(article['title'] + "\n" + article['url'])
    else:
        await message.reply("На жаль, наразі новин немає.")

@dp.message_handler(Command('watchnews'))
async def show_bbs(message: types.Message):
    
    await message.reply("Ось посилання на BBC: [Посилання](https://www.bbc.com/news) \n Ось посилання на 1+1: [Посилання](https://www.youtube.com/watch?v=ASndlvhI8p0),", parse_mode='Markdown')

# Запуск
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
