from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

token = '5570314298:AAFfXyxWCFiFCZSGUXIqfv2GFJBYWotk9xw'
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть магазин', web_app=WebAppInfo(url='https://wildberries.ru')))
    await message.answer('Добро пожаловать в наш магазин', reply_markup=markup)

executor.start_polling(dp)