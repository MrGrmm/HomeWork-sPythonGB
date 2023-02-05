from create import dp
from aiogram import types
from random import randint

total = 0
first_move = 0
bot_move = False
user_move = True
begin = False


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name} Давай сыграем в конфетки!! Напиши команду /help чтобы узнать подробности')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('/start - запуск бота\n/help - все команды\n/set - установить количество конфет\n/begin - сбросить монету и узнать кто первый делает ход\n/stop - закончить игру')

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    try:
        count = int(message.text.split()[1])
        total = count
        await message.answer(f'Общее количество конфет = {total}\nвоспользуйтесь /begin чтобы узнать чей ход первый')
    except:
        await message.answer('Введите /set 100  где 100 это количество конфет')

@dp.message_handler(commands=['begin'])
async def mes_begin(message: types.Message):
    global first_move
    global total
    global user_move
    global bot_move
    global begin

    if total > 1:
        first_move = randint(1,2)
        if first_move == 1:
            user_move = True
            await message.answer('Ваш ход, введите количество конфет')
        else:
            bot_move = True
            await message.answer('Ходит бот')
            bot_move = randint(1,29)
            await message.answer(f'Я возьму {bot_move}')
            total -= bot_move
            await message.answer(f'На столе осталось {total} конфет\nВаш ход..')
        begin = True
    else:
        await message.answer('Для начала установите количество конфет при помощи команды /set')


@dp.message_handler(commands=['stop'])
async def mes_start(message: types.Message):
    global total
    total = 0
    await message.answer('Игра окончена!')


@dp.message_handler()
async def mes_help(message: types.Message):
    global total
    global user_move
    global bot_move
    global begin

    if total > 0:
        if begin:    
            if message.text.isdigit() and 0 < int(message.text) < 29:
                if user_move:
                    total -= int(message.text)
                    if total < 1:
                        await message.answer('Вы выиграли!!')
                        bot_move = False
                    await message.answer(f'На столе осталось {total} конфет\nХод бота..')
                    bot_move = True
                    user_move = False
                if bot_move:
                    if total <= 57:
                        if total != 29:
                            bot_move = total % 29
                        else:
                            bot_move = 1
                        await message.answer(f'Я возьму {bot_move}')
                        total -= bot_move
                        if total < 1:
                            await message.answer('БОТ выиграл!!')
                    else:
                        bot_move = randint(1,29)
                        await message.answer(f'Я возьму {bot_move}')
                        total -= bot_move
                        if total < 1:
                            await message.answer('БОТ выиграли!!')
                    await message.answer(f'На столе осталось {total} конфет\nВаш ход..')
                    user_move = True
                    bot_move = False
            else:
                await message.answer(f'Введите цифру от 1 до 28\nНа столе осталось {total} конфет\nВаш ход..')
        else:
            await message.answer('Для начала воспользуйтесь /begin чтобы узнать чей ход первый')
    else:
        await message.answer('Для начала воспользуйтесь командой /set чтобы установить начальное количство конфет')


