#1.3

# x = 5 >= 2
# A = {1, 3, 7, 8}
# B = { 2, 4, 5, 10, 'apple' }
# C = A & B
# df = 'Антонова Антонина', 34, 'ж'
# z = 'type'
# D = [1, 'title', 2, 'content']
#
# print(x, '|', type(x), '\n',
#       A, '|', type(A), '\n',
#       B, '|', type(B), '\n',
#       C, '|', type(C), '\n',
#       df, '|', type(df), '\n',
#       z, '|', type(z), '\n',
#       D, '|', type(D), '\n')

#2.3

# x = int(input('Enter a number: '))
#
# if x < -5:
#     print('x принадлежит (-infinity, -5)')
# elif x >= -5 and x <= 5:
#     print('x принадлежит [-5, 5]')
# elif x > 5:
#     print('x принадлежит (5, +infinity)')

# 3.3.1
# x = 10
#
# while x >= 1:
#     print(x)
#     x -= 3

# 3.3.2

# propertyList = ['intelligence', 'compassion', 'heart', 'head', 'arms', 'legs', 'chest', 'back']
#
# for property in propertyList:
#     print(property)


# 3.3.3

# x = [i for i in range(2, 16)]
#
# print(x)

# 3.3.4

# for i in range(106, 5, -25):
#     print(i)

# 3.3.5

# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# x[::2] = x[::2][::-1]
# print(x)

# 4.3.1
# import random as rnd
# import matplotlib.pyplot as plt
#
# rnd_array = [int(rnd.random()*10)/10 for _ in range(int(rnd.random()*10+3))]
# rnd_array.sort()
# print(rnd_array)
#
# mean = sum(rnd_array)/len(rnd_array)
# print(mean)
#
# median = 0
# if (len(rnd_array) % 2 != 0):
#     print('odd length')
#     median = rnd_array[len(rnd_array)//2]
# else:
#     print('even length')
#     median = sum(rnd_array[(len(rnd_array)//2-1):(len(rnd_array)//2)])/2
# print(median)
# plt.grid()
# plt.scatter([i for i in range(len(rnd_array))], rnd_array)
# plt.xlabel('index')
# plt.ylabel('value')
# plt.show()

# 4.3.2

# import math
#
# from matplotlib import pyplot as plt
#
# def function(x):
#     return math.sqrt(1 + math.pow(math.e, math.sqrt(x)) + math.cos(x*x))/abs(1 - math.pow(math.sin(x), 3)) + math.log(abs(2*x), math.e)
#
# valArr = [function(x) for x in range(1, 11)]
# halfValArr = valArr[0:5]
#
# plt.grid()
# plt.plot(valArr)
# plt.scatter([i for i in range(0, 5)], halfValArr)
# plt.show()

# 4.3.3
# import math
# import matplotlib.pyplot as plt
# from scipy.integrate import simps
# import  numpy as np
#
# def function(x):
#     return abs(math.cos(x * math.pow(math.e, math.cos(x) + math.log(x+1, math.e))))
#
# argArr = [x for x in range(11)]
# valArr = [function(x) for x in range(11)]
# plt.grid()
# plt.plot(valArr)
# plt.fill_between(argArr, valArr)
# plt.show()
#
# area = np.trapezoid(valArr, argArr)
# print(area)

# 4.3.4
# import matplotlib.pyplot as plt
#
# AAPL = [133.52, 133.75, 123.75, 123.66, 132.04, 125.08, 136.60, 146.36, 152.83, 141.90, 148.99, 167.48]
# GOOGL = [88.00, 92.23, 102.40, 104.61, 118.25, 118.72, 121.72, 135.12, 145.00, 134.45, 148.05, 144.00]
# MSFT = [222.53, 235.05, 235.90, 238.47, 253.40, 251.23, 269.61, 286.36, 302.78, 282.12, 331.36, 335.13]
#
# months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн',
#           'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
#
# plt.grid()
# plt.plot(months, AAPL,label='AAPL', color='blue')
# plt.plot(months, GOOGL,label='GOOGL', color='red')
# plt.plot(months, MSFT,label='MSFT', color='green')
# plt.legend()
# plt.show()
# print("Все акции показали рост. Акции Alphabet показли самый большой рост в процентах. Акции Microsoft показали наибольший рост в долларах. Apple первые полгода стагнировали")

# 4.3.5
# import math
#
# x = int(input("first number: "))
# operation = input("input opertaion (`+`, `-`, `*`, `/`, `exp`, `sin`, `cos`, `pow`): ")
# y = int(input("second number: "))
#
# if operation == "+":
#     print(x + y)
# if operation == "-":
#     print(x - y)
# if operation == "*":
#     print(x * y)
# if operation == "/":
#     print(x / y)
# if operation == "exp":
#     print(math.pow(math.e, x+y))
# if operation == "sin":
#     print(math.sin(x+y))
# if operation == "cos":
#     print(math.cos(x+y))
# if operation == "pow":
#     print(math.pow(x, y))
