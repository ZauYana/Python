# хранение данных-передача данных в клиент-сервисных проектах - хранение конфигов - логирование действий
#  связать файловую переменную с файлом, определив модификатор работы
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+, r+

# colors = ['red', 'green22', 'blue111']
# data = open('file.txt', 'a')
# data.writelines(colors)  # разделителей не будет
# # добавляем еще к тому что есть \n позволяет пробел поставить
# data.write('\nLine 12\n')
# data.close()

# другой способ
# with open('file.txt', 'w') as data:
#     data.write('line1\n')
#     data.write('line1\n')
# не нужно в ручном режиме закрывать

# ЧТЕНИЕ ФАЙЛа

# path = 'file.txt'
# data = open (path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()  # позволяет не выполнять код, который находится ниже
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# ФУНКЦИИ

# import lection1
# print (lection1.f(1))


# def new_string(symbol, count = 3):
#     return symbol*count

# print (new_string('!',5))
# print (new_string('!'))
# print (new_string(5))


# def concatenatio(*params):  # звездочка позволяет вводить неограниченное кол-во аргументов
#     res: str = ""
#     for item in params:
#         res += item
#     return res


# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1'))
# print (concatenatio(1,2,3,4)) # Type error string 52 - str , change to int = 0


# РЕКУРСИЯ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)


#      КОРТЕЖИ


# (a) = (3, 4, 6, 7)
""" a = (3,) """
# print(a)
# print(a[-1])

# a[0] = 12 # не работает кортеж - неизменяемый список

# for item in a:
#     print (item)

#  КОНВЕРТАЦИЯ ИЗ СПИСКА В КОРТЕЖ
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g: {} b: {}'. format(red, green, blue))


# СЛОВАРИ

# dictionary = {}
# dictionary = \
#     {
#         'up': 'навверх',
#         'left': 'налево',
#         'down': 'вниз',
#         'right': 'направо'
#     }

# print(dictionary['up'])
# dictionary['up'] = 'not up'
# print(dictionary['up'])

# print (dictionary)
# print (dictionary['left'])
# типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k)

# for v in dictionary:
#     print(v)

# for b in dictionary.values():
#     print(b)


#  МНОЖЕСТВА

# colors = {'red','green','blue'}
# print(colors)

# colors.add ('red')  # добавления не будет
# colors.add ('gray')  # добавит элемент
# colors.remove('red')
# print(colors)
#    #colors.remove('red')  Key Error
# colors.discard('red')  # delete

# colors.clear()
# print(colors)


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# dl = a.difference(b)
# print(dl)
# dr = b.difference(a)
# print(dr)

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q)


# s = frozenset(a)  # замороженное множество - нельзя менять


# !!!!!!

# list1 = [1, 2, 3, 4]
# list2 = list1

# for i in list1:
#     print(i)
# print()
# for n in list2:
#     print(n)

# print()

# list1[0] = 123
# list2[2] = 54

# for i in list1:
#     print(i)
# print()
# for n in list2:
#     print(n)

"""не стоит просто копировать список, так как меняя элемент в одном из списков, во втором тоже меняется"""

list1 = [1, 2, 3, 4]
print(list1.pop())   # удаление последнего элемента
print(len(list1))

print(list1)


print(list1.insert(2,11))   # добавление элемента в конкретное место
print(list1)

print(list1.append(11))
print(list1)

