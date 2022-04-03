# 25. Написать программу преобразования десятичного числа в двоичное

# number = 76
# def find_binary_num(number):

#     binary_number = []
#     while number >= 1:
#         binary_digit = number % 2
#         number = number//2
#         binary_number.append(str(binary_digit))
#     return binary_number


# binary_number1 = find_binary_num(number)
# print(binary_number1)

# binary_number1.reverse()
# print(binary_number1)

# print(''.join(binary_number1))


# 26. Дано число. Составить список чисел Фибоначчи, 
# в том числе для отрицательных индексов. 

#  Т е для k = 8, список будет выглядеть 
#  так: 
#  [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 8):
    list.append(fib(e))
print(list)

