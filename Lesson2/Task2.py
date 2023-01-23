# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

while True:
    try:
        n = int(input('Enter the num: '))
        break
    except:
        print('Try again')

# my_list = []

# for i in range(1, n + 1):
#     my_list.append(round((1 + 1 / i) ** i, 2))

my_list = [round((1 + 1 / i) ** i, 2) for i in range(1, n + 1)]         # 

print(my_list)

print(f'Sum of numbers = {sum(my_list)}')           #

# sum = 0

# for item in my_list:
#     sum += item

# print(sum)
