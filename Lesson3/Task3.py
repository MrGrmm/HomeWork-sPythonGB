import random


my_list = []

for _ in range(10):
    index = random.randint(0,3)
    my_list.append(round(random.uniform(0,10), index))
    
print(my_list)