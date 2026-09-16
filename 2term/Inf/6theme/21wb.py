def task1():
    def product(n):
        p = 1
        i = 1
        while i <= n:
            p *= i
            i += 1
        return p

    print(product(5))
    # 120

def task2():
    def count_positive(arr):
        count = 0
        i = 0
        while i < len(arr):
            if arr[i] > 0:
                count += 1
            i += 1
        return count

    print(count_positive([1, -2, 3, 0, 5]))
    # 3

def task3():
    def sum_even(a, b):
        s = 0
        i = a
        while i <= b:
            if i % 2 == 0:
                s += i
            i += 1
        return s

    print(sum_even(1, 10))
    # 30

def task4():
    def max_array(arr):
        mx = arr[0]
        i = 1
        while i < len(arr):
            if arr[i] > mx:
                mx = arr[i]
            i += 1
        return mx

    print(max_array([1, 5, 3, 9, 2]))
    # 9

def task5():
    def is_prime(n):
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1
        return n > 1

    print(is_prime(7))
    print(is_prime(8))
    # True
    # False

def task6():
    print("Цикл с параметром (for) используется, когда известно количество повторений заранее")
    print("Цикл с предусловием (while) используется, когда количество повторений заранее неизвестно")
    # Цикл с параметром (for) используется, когда известно количество повторений заранее
    # Цикл с предусловием (while) используется, когда количество повторений заранее неизвестно

def task7():
    print("Алгоритм: ввод числа n, затем суммирование чисел от 1 до n")
    print("Тип цикла: цикл с параметром, так как известно количество повторений")
    # Алгоритм: ввод числа n, затем суммирование чисел от 1 до n
    # Тип цикла: цикл с параметром, так как известно количество повторений

def task8():
    def sum_n(n):
        s = 0
        for i in range(1, n+1):
            s += i
        return s

    print(sum_n(5))
    # 5 15

def task9():
    def count_pairs(arr):
        count = 0
        i = 0
        while i < len(arr):
            j = i + 1
            while j < len(arr):
                if arr[i] == arr[j]:
                    count += 1
                j += 1
            i += 1
        return count

    print(count_pairs([1, 2, 1, 2, 1]))
    # 4

def task10():
    print("Бесконечный цикл возникает, если переменная цикла не изменяется или условие всегда истинно")
    print("Для завершения цикла необходимо изменять управляющую переменную")
    print("Пример ошибки:")
    i = 1
    steps = 0
    while i > 0 and steps < 5:
        print(i)
        steps += 1
    # Бесконечный цикл возникает, если переменная цикла не изменяется или условие всегда истинно
    # Для завершения цикла необходимо изменять управляющую переменную
    # Пример ошибки:
    # 1
    # 1
    # 1
    # 1
    # 1