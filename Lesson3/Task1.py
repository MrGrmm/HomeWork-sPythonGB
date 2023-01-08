# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
import random


my_list = []

for _ in range(10):
    index = random.randint(0,3)
    my_list.append(round(random.uniform(0,10), index))
    
print(f'Initial list 👇\n{my_list}')
sum_of_item = 0
for i in range(1, len(my_list), 2):

    sum_of_item += my_list[i]

print(f'Sum of elements in odd positions = {round(sum_of_item,2)}')

