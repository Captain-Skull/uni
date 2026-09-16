def task1():
    def salary(hours, rate):
        return hours * rate

    print("Вход: часы, ставка")
    print("Выход: зарплата")
    print("Пример:", salary(40, 10))
    # Вход: часы, ставка
    # Выход: зарплата
    # Пример: 400

def task2():
    def check(x, threshold):
        if x > threshold:
            return "Превышает"
        else:
            return "Не превышает"

    print(check(10, 5))
    print(check(3, 5))
    # Превышает
    # Не превышает

def task3():
    def sort3(a, b, c):
        arr = [a, b, c]
        arr.sort()
        return arr

    print(sort3(3,1,2))
    # [1, 2, 3]

def task4():
    def count_if(arr):
        count = 0
        for x in arr:
            if x > 0:
                count += 1
        return count

    print(count_if([-1,2,3,0,5]))
    # 3

def task5():
    def test_result(correct, total):
        percent = correct / total * 100
        return percent

    print(test_result(8,10))
    # 80.0

def task6():
    print("Используются: линейные операции, ветвление и цикл")
    print("Цикл нужен для обработки набора данных")
    print("Ветвление для проверки условий")
    # Используются: линейные операции, ветвление и цикл
    # Цикл нужен для обработки набора данных
    # Ветвление для проверки условий

def task7():
    def check(x, t):
        if x > t:
            return True
        return False

    print(check(7,5))
    # True

def task8():
    print("Ошибки: некорректные данные, деление на ноль, ошибка условий, бесконечный цикл")
    # Ошибки: некорректные данные, деление на ноль, ошибка условий, бесконечный цикл

def task9():
    def process(arr):
        if not arr:
            return None
        mn = min(arr)
        mx = max(arr)
        avg = sum(arr)/len(arr)
        return mn, mx, avg

    data = [1,2,3,4]
    print("Вход: последовательность неизвестной длины")
    print("Выход:", process(data))
    print("Условие завершения: конец ввода")
    print("Переменные цикла: счетчик/элемент")
    print("Ошибки: нет условия выхода, пустой список")
    # Вход: последовательность неизвестной длины
    # Выход: (1, 4, 2.5)
    # Условие завершения: конец ввода
    # Переменные цикла: счетчик/элемент
    # Ошибки: нет условия выхода, пустой список

def task10():
    def shop(prices):
        total = 0
        for p in prices:
            if p > 100:
                total += p * 0.9
            else:
                total += p
        return total

    print("Область: магазин")
    print("Вход: список цен")
    print("Выход:", shop([50,150,200]))
    print("Структура: цикл + ветвление + вычисления")
    print("Ошибки: неверное условие скидки")
    # Область: магазин
    # Вход: список цен
    # Выход: 365.0
    # Структура: цикл + ветвление + вычисления
    # Ошибки: неверное условие скидки