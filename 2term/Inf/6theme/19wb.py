def task1():
    def max2(a, b):
        return a if a > b else b

    tests = [(3, 7), (10, -2), (5, 5)]
    for a, b in tests:
        print(a, b, max2(a, b))
    # 3 7 7
    # 10 -2 10
    # 5 5 5

def task2():
    def my_abs(x):
        return x if x >= 0 else -x

    for x in [-5, -1, 0, 3]:
        print(x, my_abs(x), abs(x))
    # -5 5 5
    # -1 1 1
    # 0 0 0
    # 3 3 3

def task3():
    def is_even(x):
        return x % 2 == 0

    for x in [-2, -1, 0, 3, 4]:
        print(x, is_even(x))
    # -2 True
    # -1 False
    # 0 True
    # 3 False
    # 4 True

def task4():
    def min3(a, b, c):
        return min(a, b, c)

    tests = [(3, 1, 2), (5, 5, 5), (-1, 0, 1)]
    for t in tests:
        print(t, min3(*t))
    # (3, 1, 2) 1
    # (5, 5, 5) 5
    # (-1, 0, 1) -1

def task5():
    def calc(x, y):
        return x*x + y*y

    tests = [(1,2), (3,4), (0,5)]
    for x,y in tests:
        print(x,y,calc(x,y))
    # 1 2 5
    # 3 4 25
    # 0 5 25

def task6():
    def check(has_end, has_def, has_res):
        return has_end and has_def and has_res

    tests = [(True,True,True),(True,False,True),(False,True,True)]
    for t in tests:
        print(t, check(*t))
    # (True, True, True) True
    # (True, False, True) False
    # (False, True, True) False

def task7():
    description = "max of two numbers"
    def impl(a,b): return a if a>b else b

    tests = [(1,2),(5,3)]
    for t in tests:
        print(t, impl(*t))
    print(False)
    # (1, 2) 2
    # (5, 3) 5
    # False

def task8():
    def total(prices):
        return sum(prices)

    tests = [[10,20,30],[5],[100,200]]
    for t in tests:
        print(t, total(t))
    # [10, 20, 30] 60
    # [5] 5
    # [100, 200] 300

def task9():
    def analyze(arr):
        if not arr:
            return None, None, None, False, True
        mn = min(arr)
        mx = max(arr)
        avg = sum(arr)/len(arr)
        has_neg = any(x < 0 for x in arr)
        return mn, mx, avg, has_neg, True

    tests = [[1,2,3], [-1,5,0], []]
    for t in tests:
        print(t, analyze(t))
    # [1, 2, 3] (1, 3, 2.0, False, True)
    # [-1, 5, 0] (-1, 5, 1.3333333333333333, True, True)
    # [] (None, None, None, False, True)

def task10():
    def good():
        return 1

    def no_end():
        while True:
            pass

    def no_result(x):
        if x > 0:
            return x

    def check(func, *args):
        has_end = func != no_end
        try:
            res = func(*args)
            has_res = res is not None
        except:
            has_res = False
        return has_end, has_res, has_end and has_res

    print(check(good))
    print(check(no_end))
    print(check(no_result, -1))
    # (True, True, True)
    # (False, False, False)
    # (True, False, False)