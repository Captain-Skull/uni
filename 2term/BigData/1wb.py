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

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x[::2] = x[::2][::-1]
print(x)