# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 

coordinateX = float(input('Enter X coordinate: '))
coordinateY = float(input('Enter Y coordinate: '))

if coordinateX > 0 and coordinateY > 0:
    print('1')
elif coordinateX < 0 and coordinateY > 0:
    print('2')
elif coordinateX < 0 and coordinateY < 0:
    print('3')
elif coordinateX > 0 and coordinateY < 0:
    print('4')
else:
    print('ERROR: X ≠ 0 and Y ≠ 0')