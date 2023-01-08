# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
from math import floor

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_list = []
for _ in range(10):
    index = random.randint(0,2)
    my_list.append(round(random.uniform(0,10), index))
    
print(my_list)
new_list = []

for i in range(len(my_list)):
    new_list.append((my_list[i] % 1))

biggest = max(new_list) * 100
littles = min(new_list) * 100

# print(biggest)
# print(littles)
print(f'The difference between the maximum and minimum value of the fractional part = {floor(biggest - littles)/ 100}')
