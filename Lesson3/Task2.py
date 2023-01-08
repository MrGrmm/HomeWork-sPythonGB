# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random

# my_list = [2,3,4,5,6]
my_list = []
for _ in range(10):
    index = random.randint(0,2)
    my_list.append(round(random.randint(0,10), index))

middle_i = len(my_list) // 2
new_list = []
j = 0

for i in range(middle_i):
    j -= 1
    new_list.append(my_list[i] * my_list[j])
if len(my_list) % 2 != 0:
    new_list.append(my_list[middle_i] * my_list[middle_i])
print(f'Initial list 👉  {my_list}\nResult 👉  {new_list}')

