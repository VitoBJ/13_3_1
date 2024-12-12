from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib. fsm_storage.memory import MemoryStorage
import asyncio

api = "7987427447:AAE6vFnFIQve_u5MCaCQSX4Yuh_SwgMwc3g"
bot = Bot(token = api)
dp = Dispatcher(bot,storage = MemoryStorage())

@dp.message_handler(text= "привет")
async def all_messege(messege):
    print("Urban messege")
    await messege.answer("Введите команду /start,чтобы начать общение")

@dp.message_handler(commands=["start"])
async def start_messege(messege):
    print("start messege")
    await messege.answer("Рады видеть Вас в нашем Боте")

@dp.message_handler()
async def all_message(messege):
    print("Вы получили сообщение.")
    await messege.answer(messege. text)







if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
