# Семинар 3-4: примерный список задач

# 1. Сформировать список из N членов последовательности.

# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# def get_list(first_num, last_num, length):
#     list = []
#     for i in length:
#         i = range(first_num, last_num)


# list_1 = get_list(0, 999, 5)
# print(list_1)


# 12.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# 13.Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# from curses import beep


# str1 = input()
# str2 = input()

# print({str1}.count({str2}))

from collections import Counter  # верное решение 
my_str1 = input()    # верное решение
my_str2 = input()    # верное решение
# counter = Counter(my_str1)
# for i in my_str1:
#     print(counter['i'])


print(my_str1.count(my_str2))    # верное решение
