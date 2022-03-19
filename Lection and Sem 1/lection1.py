# # типы данных int, float, boolean, str, list, None
# value = None
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 1234
# print(type(value))

# # слэш n дает переход на другую строку, текст можно обрамлять одинарными или двойными ковычками
# s = 'hello \nworld'
# print(s)
# print(a, ' - ', b, ' - ', s)
# # в скобках можно выставить индексы выводимого текста ( то есть не абс , а например бса)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# логическая переменная
# f = False  # или f = True
# print(f)

# списки

# list = ['1', '2', 'hello', True]
# col = ['1', '2', 'hello', True]
# print(list)
# print(col)

# считывание текста с терминала

# print('введите а')
# a = input()
# print('введите b')
# b = input()
# # работает с текстом? поэтому введя 10 и 20  в сумме получим 1020
# print(a, ' ', b, ' ', a+b)


#  чтобы получить числа надо ввести перед input - int/float

# print('введите а')
# a = int(input())
# print('введите b')
# b = int(input())
# print(a, ' ', b, ' ', a+b)


# арифметчиеские операции
# +,-, *, /, %, //, **

# a = +123
# b = -321
# c = a+b
# print(c)

# a = +123
# b = -321
# c = a/b    # // деление и получение целого числа
# print(c)

# остаток от деления - %
# возведение в степень **

# a = 1.35435678
# b = 3
# c = round(a*b, 5)
# print(c)


# сокращенные операции присваивания

# a = 3
# #a = a+5

# #a +=5
# a *=5

# print (a)


# логические операции
# > >= < <= == !=
# not , and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

#a = 1 < 4 and 5 > 2
#a = 1 == 2
#a = 1 != 2


# a = 'qwe'
# b = 'qwe'

# a = [1, 2]
# b = [1, 2]

# print(a == b)


# a = 1 < 3 < 5 < 10 < 15
# print(a)


# func =1
# T = 4
# x = 123

# print (func<T>(x))


# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# # print(f)
# # print(2 in f)
# # print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)
# #или
# is_odd1 = not f[0] % 2
# print(is_odd1)

# IF AND ELSE

# a = int(input('a ='))
# b = int(input('b='))
# if a > b:
#     print(a)
# else:
#     print(b)


# IF ELIF

# username = input('Введите имя:')
# if username == 'Маша':
#     print('Ура, это же Маша')
# elif username == 'Марина':
#     print('Я так ждала Вас')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# while

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)


# while and else

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print ('пожалуй')
#     print ('хватит')
# print(inverted)


# FOR (for i in )


# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)


# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)


# for i in 'qwe-rty':
#     print(i)


# НЕМНОГО О СТРОКАХ

#text = 'в этом мире усе циклично'
# print(len(text))  # длина текста
# print('все' in text)  # true
# print(text.isdigit())    # false  является ли числами
# print(text.islower()) # true  являются ли все буквы нижнего регистра
# print(text.replace('в','В'))  # замена

# подсказка через контрл пробел или

# help(text.istitle)

# print(text[0])  # first letter

# print(text[len(text)]) # error

# print(text[len(text)-1])

# в тексте первый символ с индексом 0, то тогда начиная с последнего элемента массива нумерация индексов будет -1, -2, и тд
# print(text[-5])


# print(text[:])  # print text
# print(text[:5])  # с нулевого элемента до необходимого
# print(text[2:5])  # с нужного элемента по нужный

# print(text[len(text)-2:])

# print(text[6:-8])

# print(text[0:len(text):6])
# print(text[::6])

# text = text[2:9] + text[-5] + text[:2]

# print(text)


# СПИСКИ

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# print(numbers)

# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)

# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e*2)


# colors.append('gray')  # добавить элемент в конец
# print(colors == ['red', 'green', 'blue', 'gray'])
# colors.remove('red')  # del colors [0]  удалить элемент
# print(colors)


# ФУНКЦИЯ

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# a = 2.3
# print(f(a))
# print(type(f(a)))



 