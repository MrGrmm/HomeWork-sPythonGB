from random import randint
from handlers import dp
from create import executor


async def on_start(_):
    print('Бот запущен')

total = 0
first_move = 0
bot_move = False
user_move = True
begin = False


executor.start_polling(dp, skip_updates=True, on_startup=on_start)