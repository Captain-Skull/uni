def task1():
    def sum2(a, b):
        return a + b

    print(sum2(3, 5))
    # 8

def task2():
    def min2(a, b):
        if a < b:
            return a
        else:
            return b

    print(min2(3, 5))
    print(min2(7, 2))
    # 3
    # 2

def task3():
    def area(a, b):
        return a * b

    print(area(4, 6))
    # 24

def task4():
    def check(n):
        if n > 0:
            return "Положительное"
        elif n < 0:
            return "Отрицательное"
        else:
            return "Ноль"

    print(check(5))
    print(check(-3))
    print(check(0))
    # Положительное
    # Отрицательное
    # Ноль

def task5():
    def my_abs(x):
        if x >= 0:
            return x
        else:
            return -x

    print(my_abs(-7))
    print(my_abs(4))
    # 7
    # 4

def task6():
    print("Линейный алгоритм выполняется последовательно без условий")
    print("Разветвляющийся алгоритм содержит условие и выбор одной из ветвей")
    # Линейный алгоритм выполняется последовательно без условий
    # Разветвляющийся алгоритм содержит условие и выбор одной из ветвей

def task7():
    print("Алгоритм: ввод числа, проверка четности, вывод результата")
    # Алгоритм: ввод числа, проверка четности, вывод результата

def task8():
    def max2(a, b):
        if a > b:
            return a
        else:
            return b

    print(max2(10, 3))
    # 10

def task9():
    def triangle(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                t = "Равносторонний"
            elif a == b or b == c or a == c:
                t = "Равнобедренный"
            else:
                t = "Разносторонний"

            m = max(a, b, c)
            if 10 <= m <= 50:
                interval = "В интервале"
            else:
                interval = "Не в интервале"

            return t, interval
        else:
            return "Не существует"

    print(triangle(3,3,3))
    print(triangle(3,4,5))
    print(triangle(1,2,3))
    # ('Равносторонний', 'Не в интервале')
    # ('Разносторонний', 'Не в интервале')
    # Не существует

def task10():
    def swap(a, b):
        a = a + b
        b = a - b
        a = a - b
        return a, b

    print(swap(3, 5))
    # (5, 3)