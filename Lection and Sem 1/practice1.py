# 1.По двум заданным числам проверить является ли одно квадратом второго

from random import random
from sys import maxsize


a = 5
b = 7
is_square_a = a**2 == b
is_square_b = b**2 == a
print(is_square_a)
print(is_square_b)


# 2. Найти максимальное из пяти чисел

a = 4
v = 3
g = 9
f = 6
e = 10
max = a
if v > max:
    max = v
if g > max:
    max = g
if f > max:
    max = f
if e > max:
    max = e

print(max)

list = [a, v, g, f, e]
max_number = max(list)
# print(max_number)


# 3. Вывести на экран числа от -N до N
# print('введите число')
# usernumber = int(input())
# count = -usernumber
# while (count <= usernumber):
#     # print({0}.format(count))
