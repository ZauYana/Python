# Семинар 3-4: примерный список задач

# 11. Сформировать список из N членов последовательности.

# Для N = 5: 1, -3, 9, -27, 81 и т.д.


from random import randint


# list = []
# i = 0
# while i < 5:
#     list.append(randint(0, 999))
#     i +=1
# print(list)


# 12.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# dictionary = {}
# i = 1
# n = 6
# while i <= n:
#     dictionary[i] = (3*i+1)
#     i += 1

# print(dictionary)


# 13.Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# from curses import beep


# str1 = input()
# str2 = input()

# print({str1}.count({str2}))

# from collections import Counter  # верное решение
# my_str1 = input()    # верное решение
# my_str2 = input()    # верное решение
# # counter = Counter(my_str1)
# # for i in my_str1:
# #     print(counter['i'])


# print(my_str1.count(my_str2))    # верное решение

# 14. Подсчитать сумму цифр в вещественном числе.

# number = 4655.76543
# number = str(number)
# number1 = number.replace('.', '')
# number1 = int(number1)
# sum_num = 0
# while number1 > 0:
#     sum_num += number1 % 10
#     number1 //= 10

# print(sum_num)

# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
# n = 4
# massiv = range(1, n+1)
# massiv = list(massiv)
# print(massiv)
# massiv_new = []
# massiv_new.append(1)
# i = 0
# j = 0
# while i < n-1:
#     massiv_new.append(massiv_new[j]*massiv[(i+1)])
#     i += 1
#     j += 1
# print(massiv_new)


# 16. Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

def create_list(n):
    list_second = []
    i = 0
    while i <= n:
        list_second.append((1+1*n)*n)
        i += 1
    return list_second


def find_sum(some_list):
    sum_of_list = None
    for i in some_list:
        sum_of_list += some_list[i]
    return sum_of_list    

my_list = create_list(5)
print(my_list)
print(find_sum(my_list))



# 17. Задать список из N элементов, заполненных числами из [-N, N].
