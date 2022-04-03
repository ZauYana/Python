# 17. Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

# from random import randint

# from random import randint


# n = int(input("Введите число"))

# list1 = []

# while n > 0:
#     list1.append(randint(-n, n))
#     n -= 1
# print(list1)


# list_from_text = []
# with open('file.txt', 'r') as data:
#     for i in data:
#         list_from_text.append(i.strip())


# print(list_from_text)
# 20. Определить, присутствует ли в заданном списке строк, некоторое число
# string_list = ["dads", "fhj", "dad2312s", "dadsd21s",
#                "dadsgfgd", "dadsaa", "6543","das", "dds", "123dads"]

# for i in string_list:
#     if i.isdigit():
#         print(f'Все окей, число есть {i}')
#         exit()
# print("ничего не найдено")


# РЕШЕНИЕ ЛУЧШЕ:

# import re
# lst = ['yes', 'hello', '5 раз', '123']
# signal = False
# for i in range(len(lst)):
#     if re.findall('[0-9]', lst[i]) != []:
#         signal = True
# print(signal)


# 21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# list1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# string1 = 'qwe'
# count = None
# if list1.count(string1) < 2:
#     count = -1
# else:
#     for i in range(len.list1):
#         if string1 == i:
#             count += 1
#             if count == 2:
#                 print([i])

#  не сделано!!!


# spisok_1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# stroka_1 = "йцу"
# count = 0
# print(spisok_1.count(stroka_1))
# if spisok_1.count(stroka_1) <2:
#     count = -1
# else:
#     for i in range(len(spisok_1)):
#         if spisok_1[i] == stroka_1:
#             count+=1
#             if count ==2:
#                 count = i
#                 break
# print(f'Искомое {stroka_1}, ответ {count}')


# 22. Найти сумму чисел списка стоящих на нечетной позиции

# def find_sum(list):
#     sum = 0
#     i = 0
#     while i <= len.list:
#         sum += list[i]
#         i += 2


# list_1 = [1, 4, 5, 6, 7]
# print(find_sum(list_1))


# 24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# float_spisok = [1.1, 1.2, 3.1, 5.002, 10.000001, 11.13, 10.11, 122324.52, 0.14]
# # i=0
# # while float_spisok[i]>1:
# max = 0.000
# min = 1.000
# for i in range(len(float_spisok)):
#     float_spisok[i]=round(float_spisok[i]-int(float_spisok[i]),10)
#     if max<float_spisok[i]:
#         max = float_spisok[i]
#     if min>float_spisok[i]:
#         min = float_spisok[i]
# x=max-min
# # print(float_spisok)
# # print(max(float_spisok))
# print(max,min)
# print(type(x))
# print(x)
