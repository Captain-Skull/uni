def task1():
    def total(price, delivery):
        return price + delivery

    print(total(100, 20))
    # 120

def task2():
    def in_range(x, a, b):
        return a <= x <= b

    print(in_range(5, 1, 10))
    print(in_range(15, 1, 10))
    # True
    # False

def task3():
    def count_div(arr, k):
        count = 0
        for x in arr:
            if x % k == 0:
                count += 1
        return count

    print(count_div([2,3,4,6,9], 3))
    # 3

def task4():
    def second_max(arr):
        arr = sorted(set(arr))
        return arr[-2] if len(arr) > 1 else None

    print(second_max([1,5,3,9,7]))
    # 7

def task5():
    def count_range(arr, a, b):
        count = 0
        for x in arr:
            if a <= x <= b:
                count += 1
        return count

    print(count_range([1,5,10,15,20], 5, 15))
    # 3

def task6():
    print("Тесты: обычные, граничные и некорректные")
    print("Пример:")
    print(5 <= 5 <= 10)
    print(0 <= 5 <= 10)
    print(-1 <= 5 <= 10)
    # Тесты: обычные, граничные и некорректные
    # Пример:
    # True
    # True
    # True

def task7():
    print("Ввод: input()")
    print("Вычисления: операции +, -, *, /")
    print("Ветвление: if")
    print("Цикл: for/while")
    # Ввод: input()
    # Вычисления: операции +, -, *, /
    # Ветвление: if
    # Цикл: for/while

def task8():
    def old(arr):
        return sum(arr)

    def new(arr):
        return sum(arr) * 0.9

    print(old([10,10]))
    print(new([10,10]))
    # 20
    # 18.0

def task9():
    def changes(arr):
        count = 0
        prev = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                cur = 1
            elif arr[i] < arr[i-1]:
                cur = -1
            else:
                continue
            if prev != 0 and cur != prev:
                count += 1
            prev = cur
        return count

    print("Переменные: prev (предыдущее направление)")
    print(changes([1,2,3,2,1,2]))
    print(changes([1,1,1]))
    # Переменные: prev (предыдущее направление)
    # 2
    # 0

def task10():
    def process(matrix):
        sums = []
        has_neg = False

        for row in matrix:
            s = sum(row)
            sums.append(s)
            for x in row:
                if x < 0:
                    has_neg = True

        max_row = sums.index(max(sums)) + 1
        return sums, max_row, has_neg

    print("Внешний цикл: по строкам")
    print("Внутренний цикл: по элементам строки")

    m = [[1,2,3],[4,5,6],[-1,2,3]]
    print(process(m))
    # Внешний цикл: по строкам
    # Внутренний цикл: по элементам строки
    # ([6, 15, 4], 2, True)