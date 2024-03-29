# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
from math import floor 


# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# my_list = []
# for _ in range(random.randint(1,10)):
#     index = random.randint(0,2)
#     my_list.append(round(random.uniform(0,10), index))

my_list = [round(random.uniform(0,10), random.randint(0,2)) for _ in range(random.randint(1,10))]           #
    
print(f'Initial list 👉 {my_list}')
new_list = []

# for i in range(len(my_list)):
#     if my_list[i] % 1 != 0:
#         new_list.append((my_list[i] % 1))

new_list = list(map(lambda x: x % 1, [item for item in my_list if item % 1 != 0]))          #
print(new_list)

biggest = max(new_list) * 100
littles = min(new_list) * 100

print(f'The difference between the maximum and minimum value of the fractional part = {floor(biggest - littles)/ 100}')
