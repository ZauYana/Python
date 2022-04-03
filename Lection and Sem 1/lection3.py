# ускоренная обработка данных

# def f(x):
#     x**2


# g = f
# print(type(f))
# print(f(1))
# print(g(1))

# def f(x):
#     return x**2


# print(f(2))
# print(type(f))
# g = f
# print(type(g))
# print(g(2))

# def calc(x):
#     return x+10


# # print(calc(10))


# def calc1(x):
#     return x*10


# print(calc1(10))

"""в качестве аргумента передается целая функция"""
# def math(operation, x):
#     print(operation(x))


# math(calc1, 10)
# math(calc, 10)


# def sum(x, y):
#     return x+y


# f = sum

''' тоже самое, что ранее функция sum'''

# sum = lambda x, y: x+y


# def mylt(x, y):
#     return x*y


"""в качестве аргумента передается целая функция"""


# def calc2(op, a, b):
#     print(op(a, b))
#     # return op(a,b)


# calc2(mylt, 4, 5)
# # calc2(f, 4, 5)
# # calc2(sum, 4, 5)

# calc2(lambda x, y: x+y, 4, 5)

'''LIST COMPREHENSION
exp for item in iterable
exp for item in iterable (if conditional)
exp <if conditional> for item in iterable (if conditional)'''

# list = []

# for i in range(1, 101):
#     # if(i%2 == 0):
#     list.append(i)

# print(list)

# list = [i for i in range(1, 21)]
# print(list)
'''условие добавлено'''
# list = [i for i in range(1, 21) if i%2 == 0]
# print(list)
'''кортеж'''
# list = [(i,i) for i in range(1, 21)if i%2 == 0]
# print(list)

# def f(x):
#     return x**3

# list = [(i,f(i)) for i in range(1, 21)if i%2 == 0]
# print(list)

'''в файле хранятся числа, нужно выбрать четные и составить
список пар (число; квадрат числа)
пример: 1 2 3 5 8 15 23 38
получить: [(2,4),(8,64),(38,1444)]'''
# my solutin
# file = [1, 2, 3, 5, 8, 23, 38]
# new_file = [(i,i**2) for i in file if i % 2 == 0]
# print(file)
# print(new_file)

# teacher's solution  - не сработало у меня

# path = '/Users/yanazaulskaya/Desktop/Учеба Разработчик/Python/fileForLec3.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)

# ЕЩЕ ОДИН ВАРИАНТ

# def select(f, col):
#     return [f(x)for x in col]


# def where(f, col):
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x:(x,x**2),res)
# print(res)


'''ФУНКЦИЯ MAP  - применяет указанную функцию к каждому элементу 
итерируемого объекта и возвращает итератор с новыми объектами'''

# li = [x for x in range(1, 20)]

# li = list(map(lambda x: x+10, li))

# print(li)


# data = list(map(int, input().split()))
# print(data)
'''если не делать сразу list или принудительное сохранение 
в какую-нибудь переменную, то с данными типа map можно работать
только один раз (ПРИМЕР НИЖЕ) Добавив в начало перед map 
оператор list можно работать неоднократно'''
# data = map(int, input().split())

# for e in data:
#     print(e)

# print('_______')

# for e in data:
#     print(e)


# __________
'''замена select на map'''
# def select(f, col):
#     return [f(x)for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(map(lambda x:(x,x**2),res))
# print(res)
'''замена where на filter  - это  применяет к указанную 
функцию к каждому элементу итерируемого объекта и возвращает 
итератор с теми объектами, для которых
функция вернула true'''


# data = [x for x in range (10)]
# res = list(filter(lambda x: not x%2, data))
# print(res)


# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x:(x,x**2),res))
# print(res)

'''функция zip применяется к набору итерируемых объектов 
и возвращает итератор с кортежами из элементов входных данных'''

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# data = list(zip(users, ids, salary))
# print(data)

'''функция enumerate'''
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# data = list(enumerate(ids))
# print(data)

