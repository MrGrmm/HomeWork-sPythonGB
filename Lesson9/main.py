from aiogram import Bot, Dispatcher, executor, types
from random import randint

bot = Bot('6076464585:AAFiRKPs3VGtyE3feTD2ub4fV_qLiJxTPy4')
dp = Dispatcher(bot)

async def on_start(_):
    print('Бот запущен')

total = 0
first_move = 0


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name} Давай сыграем в конфетки!! Напиши команду \help чтобы узнать подробности')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('/start - запуск бота\n/help - все команды\n/set - установить количество конфет\n/stop - закончить игру')

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    try:
        count = int(message.text.split()[1])
        total = count
        await message.answer(f'Общее количество конфет = {total}')
    except:
        await message.answer('Введите /set 100  где 100 это количество конфет')

@dp.message_handler(commands=['begin'])
async def mes_begin(message: types.Message):
    global first_move
    first_move = randint
    await message.answer('/start - запуск бота\n/help - все команды\n/set - установить количество конфет\n/stop - закончить игру')

@dp.message_handler()
async def mes_help(message: types.Message):
    global total

    if message.text.isdigit():
        if (total - int(message.text)) > 0:
            total -= int(message.text)
        else:
            await message.answer('Вы выиграли!!')
    else:
        await message.answer('Неизвестная команда')
    await message.answer(f'На столе осталось {total} конфет')
    if total <= 57:
        bot_move = total % 28
        await message.answer(f'Я возьму {bot_move}')
        if total - bot_move > 0:
            total -= bot_move
        else:
            await message.answer('БОТ выиграли!!')
    else:
        bot_move = randint(1,29)
        await message.answer(f'Я возьму {bot_move}')
        if total - bot_move > 0:
            total -= bot_move
        else:
            await message.answer('БОТ выиграли!!')
    await message.answer(f'На столе осталось {total} конфет')








executor.start_polling(dp, skip_updates=True, on_startup=on_start)