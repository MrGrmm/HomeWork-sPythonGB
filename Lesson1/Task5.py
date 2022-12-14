# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

xa = float(input('Enter xa coordinate: '))
ya = float(input('Enter ya coordinate: '))
xb = float(input('Enter xb coordinate: '))
yb = float(input('Enter yb coordinate: '))

import math

rangeAB = math.sqrt((xb - xa)**2 + (yb - ya)**2)
print(round(rangeAB,2))

# Здесь ещё возник вопрос возник, я использовал "round" чтобы удалить цифры после запятой,
# но в первой проверке где A(3,6); B(2,1) round округляет до 5.1 вместо необходимого результата в 5.09
# как сделать чтобы просто удалить цифры после запятой не огругляя? 

