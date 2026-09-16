import time
import random

def task1():
    def sum_n(n):
        s = 0
        for i in range(1, n+1):
            s += i
        return s

    print(sum_n(10))
    print("Сложность: O(n), определяется циклом")
    # 55
    # Сложность: O(n), определяется циклом

def task2():
    def find_min(arr):
        mn = arr[0]
        for x in arr:
            if x < mn:
                mn = x
        return mn

    print(find_min([3,1,4,2]))
    print("Сложность: O(n)")
    # 1
    # Сложность: O(n)

def task3():
    print("Сортировка выбором: O(n^2), число сравнений всегда одинаково")
    # Сортировка выбором: O(n^2), число сравнений всегда одинаково

def task4():
    def f(n):
        count = 0
        for i in range(n):
            for j in range(i):
                count += 1
        return count

    print(f(5))
    print("Сложность: O(n^2)")
    # 10
    # Сложность: O(n^2)

def task5():
    def linear_search(arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

    sizes = [1000, 5000, 10000]
    for n in sizes:
        arr = list(range(n))
        start = time.perf_counter()
        linear_search(arr, n-1)
        end = time.perf_counter()
        print(n, end-start)
    print("Линейный рост времени → O(n)")
    # вывод зависит от времени выполнения

def task6():
    def bubble(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    arr = [5,3,2,4,1]
    print(bubble(arr))
    print("Сложность: O(n^2)")
    # [1, 2, 3, 4, 5]
    # Сложность: O(n^2)

def task7():
    print("Теория: O(n)")
    print("Практика: зависит от железа, интерпретатора")
    # Теория: O(n)
    # Практика: зависит от железа, интерпретатора

def task8():
    sizes = [1000, 5000, 10000]
    for n in sizes:
        arr = list(range(n))
        start = time.perf_counter()
        sum(arr)
        end = time.perf_counter()
        print(n, end-start)
    print("Рост примерно линейный")
    # вывод зависит от времени выполнения

def task9():
    def slow(arr):
        count = 0
        for i in arr:
            for j in arr:
                if i == j:
                    count += 1
        return count

    def fast(arr):
        d = {}
        for x in arr:
            d[x] = d.get(x,0)+1
        return sum(v*v for v in d.values())

    sizes = [100, 300, 500]
    for n in sizes:
        arr = [random.randint(1,50) for _ in range(n)]

        t1 = time.perf_counter()
        slow(arr)
        t2 = time.perf_counter()

        t3 = time.perf_counter()
        fast(arr)
        t4 = time.perf_counter()

        print(n, "slow:", t2-t1, "fast:", t4-t3)

    print("slow O(n^2), fast O(n)")
    print("При росте n разница резко увеличивается")
    # вывод зависит от времени выполнения
    # slow O(n^2), fast O(n)
    # При росте n разница резко увеличивается

def task10():
    def bubble(arr):
        a = arr[:]
        n = len(a)
        for i in range(n):
            for j in range(0, n-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a

    def builtin(arr):
        return sorted(arr)

    datasets = {
        "random": [random.randint(1,100) for _ in range(200)],
        "sorted": list(range(200)),
        "reverse": list(range(200,0,-1))
    }

    for name, data in datasets.items():
        t1 = time.perf_counter()
        bubble(data)
        t2 = time.perf_counter()

        t3 = time.perf_counter()
        builtin(data)
        t4 = time.perf_counter()

        print(name, "bubble:", t2-t1, "sorted:", t4-t3)

    print("Пузырек O(n^2), встроенный O(n log n)")
    print("На больших данных встроенный быстрее")
    print("Структура данных влияет на время")
    # вывод зависит от времени выполнения
    # Пузырек O(n^2), встроенный O(n log n)
    # На больших данных встроенный быстрее
    # Структура данных влияет на время