# 1.По двум заданным числам проверить является ли одно квадратом второго

from calendar import c
from locale import DAY_1, DAY_2, DAY_3, DAY_4, DAY_5, DAY_6, DAY_7
from random import random
from re import A
from sys import maxsize


# a = 5
# b = 7
# is_square_a = a**2 == b
# is_square_b = b**2 == a
# print(is_square_a)
# print(is_square_b)


# 2. Найти максимальное из пяти чисел

# a = 4
# v = 3
# g = 9
# f = 6
# e = 10
# max1 = a
# if v > max1:
#     max1 = v
# if g > max1:
#     max1 = g
# if f > max1:
#     max1 = f
# if e > max1:
#     max1 = e

# print(max1)

# mass = [4, 3, 6, 7, 8]
# print(max(mass))

# 3. Вывести на экран числа от -N до N

# for i in range(-7,8):
#     print(i)


# 4. Показать первую цифру дробной части числа

# a = 3.8768765
# b = a // 1
# c = ((a - b)*10)//1
# print(c)


# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

# nums = 65
# is_true = nums % 5 == 0 and nums % 10 == 0 or nums % 15 == 0 and not nums % 30 == 0
# print(is_true)


# 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
# days_of_the_week = ['Monday', 'Tuesday', 'Wensday',
#                     'Thursday', 'Friday', 'Saturday', 'Sunday']
# print('Введите номер дня недели')
# i = int(input()) - 1
# if i == 5 or i == 6:
#     print(f'{days_of_the_week[i]} - "Выходной день"')
# else:
#     print(days_of_the_week[i])


# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# x = 3
# y = 5
# z = 4
# math1 = -(x, y, z)
# math2 = -x, -y, -z
# math1 == math2

# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
# x = 0
# y = 0
# point_a = (x, y)
# if x > 0 and y > 0:
#     print(
#         f'точка с координатами {point_a} находится в первой четверти оси координат')
# elif x < 0 and y > 0:
#     print(
#         f'точка с координатами {point_a} находится во второй четверти оси координат')
# elif x < 0 and y < 0:
#     print(
#         f'точка с координатами {point_a} находится в третий четверти оси координат')
# elif x > 0 and y < 0:
#     print(
#         f'точка с координатами {point_a} находится в четвертой четверти оси координат')
# elif x == 0 and y == 0:
#     print(
#         f'точка с коррдинатами {point_a} находится в нулевой точке оси координат')
# else:
#     print(f'точка с координатами {point_a} выходит за пределы оси координат')

# 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

# print("Введите номер системы координат")
# number_of_sys = int(input())
# x1 = range(999)
# x2 = range(-999)
# y1 = range(999)
# y2 = range(-999)

# part1 = (x1, y1)
# part2 = (x2, y1)
# part3 = (x2, y2)
# part4 = (x1, y2)

# if number_of_sys == 1:
#     print(part1)
# elif number_of_sys == 2:
#     print(part2)
# elif number_of_sys == 3:
#     print(part3)
# elif number_of_sys == 4:
#     print(part4)
# else: 
#     print ('указанной системы координат не существует')

# 10. Найти расстояние между двумя точками пространства
# import math
# d = None
# x1 = 2
# y1 = 4
# x2 = 5
# y2 = 1
# d = int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
# print(d)


