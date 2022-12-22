# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

from random import randint


my_list = []

for i in range(randint(1, 10)):
    while True:
        try:
            my_list.append(int(input(f'Position number {i+1}: ')))
            break
        except:
            print('Try again')

print(my_list)

for i in range(len(my_list)):
    j = randint(0, (len(my_list) - 1))
    if i != j:
        my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)
