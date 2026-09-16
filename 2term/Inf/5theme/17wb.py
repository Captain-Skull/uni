import random

def task1():
    def NOT(x): return int(not x)
    def AND(x, y): return int(x and y)
    def OR(x, y): return int(x or y)
    def XOR(x, y): return x ^ y
    def NAND(x, y): return int(not (x and y))
    def NOR(x, y): return int(not (x or y))

    print("NOT:", [NOT(x) for x in [0,1]])
    print("AND:", [(x,y,AND(x,y)) for x in [0,1] for y in [0,1]])
    print("OR:", [(x,y,OR(x,y)) for x in [0,1] for y in [0,1]])
    print("XOR:", [(x,y,XOR(x,y)) for x in [0,1] for y in [0,1]])
    print("NAND:", [(x,y,NAND(x,y)) for x in [0,1] for y in [0,1]])
    print("NOR:", [(x,y,NOR(x,y)) for x in [0,1] for y in [0,1]])
    # NOT: [1, 0]
    # AND: [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]
    # OR: [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
    # XOR: [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
    # NAND: [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0)]
    # NOR: [(0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 0)]

def task2():
    for x in [0,1]:
        print("NOT", x, int(not x))
    for x in [0,1]:
        for y in [0,1]:
            print("AND", x, y, int(x and y))
            print("OR", x, y, int(x or y))
            print("XOR", x, y, x ^ y)
            print("NAND", x, y, int(not (x and y)))
            print("NOR", x, y, int(not (x or y)))
    # полный вывод таблиц истинности для всех вентилей

def task3():
    for x in [0,1]:
        for y in [0,1]:
            print(x, y, x ^ y, (x + y) % 2)
    # значения XOR совпадают со сложением по модулю 2

def task4():
    def half_adder(x, y):
        return x ^ y, int(x and y)

    for x in [0,1]:
        for y in [0,1]:
            print(x, y, half_adder(x,y))
    # (0,0)->(0,0); (0,1)->(1,0); (1,0)->(1,0); (1,1)->(0,1)

def task5():
    def full_adder(x, y, cin):
        return x ^ y ^ cin, int((x and y) or (cin and (x ^ y)))

    for x in [0,1]:
        for y in [0,1]:
            for cin in [0,1]:
                print(x, y, cin, full_adder(x,y,cin))
    # корректные значения полного сумматора для всех комбинаций

def task6():
    def full_adder(x, y, cin):
        return x ^ y ^ cin, int((x and y) or (cin and (x ^ y)))

    for x in [0,1]:
        for y in [0,1]:
            for cin in [0,1]:
                S, C = full_adder(x,y,cin)
                print(x, y, cin, S, C)
    # таблица истинности совпадает с теоретической

def task7():
    def AND(x,y): return int(x and y)
    def OR(x,y): return int(x or y)
    def XOR(x,y): return x ^ y

    def half_adder(x,y):
        return XOR(x,y), AND(x,y)

    def full_adder(x,y,cin):
        s1, c1 = half_adder(x,y)
        s2, c2 = half_adder(s1,cin)
        return s2, OR(c1,c2)

    for x in [0,1]:
        for y in [0,1]:
            for cin in [0,1]:
                print(x,y,cin, full_adder(x,y,cin))
    # результаты совпадают с эталонным полным сумматором

def task8():
    def NAND(x,y): return int(not (x and y))
    def NOR(x,y): return int(not (x or y))

    def NOT_nand(x): return NAND(x,x)
    def AND_nand(x,y): return NOT_nand(NAND(x,y))
    def OR_nand(x,y): return NAND(NOT_nand(x), NOT_nand(y))

    def NOT_nor(x): return NOR(x,x)
    def OR_nor(x,y): return NOT_nor(NOR(x,y))
    def AND_nor(x,y): return NOR(NOT_nor(x), NOT_nor(y))

    for x in [0,1]:
        for y in [0,1]:
            print(x,y, AND_nand(x,y), OR_nand(x,y), AND_nor(x,y), OR_nor(x,y))
    # операции через NAND и NOR совпадают с обычными AND и OR

def task9():
    def full_adder(x, y, cin):
        return x ^ y ^ cin, int((x and y) or (cin and (x ^ y)))

    def ripple(a, b):
        n = len(a)
        carry = 0
        res = ""
        carries = 0
        for i in range(n-1, -1, -1):
            s, carry = full_adder(int(a[i]), int(b[i]), carry)
            if carry: carries += 1
            res = str(s) + res
        overflow = int(a[0] == b[0] and res[0] != a[0])
        return res, carry, overflow, carries

    a = "1011"
    b = "0110"
    res = ripple(a,b)
    print(res)

    ref = bin((int(a,2)+int(b,2)) % (2**len(a)))[2:].zfill(len(a))
    print(ref)
    # ('0001', 1, 0, 3)
    # 0001

def task10():
    def full_adder(x, y, cin):
        return x ^ y ^ cin, int((x and y) or (cin and (x ^ y)))

    def ripple(a, b):
        n = len(a)
        carry = 0
        res = ""
        for i in range(n-1, -1, -1):
            s, carry = full_adder(int(a[i]), int(b[i]), carry)
            res = str(s) + res
        return res

    n = 8
    M = 1000
    ok = 0
    fail = 0
    errors = []

    for _ in range(M):
        a = format(random.randint(0, 2**n - 1), f'0{n}b')
        b = format(random.randint(0, 2**n - 1), f'0{n}b')

        r1 = ripple(a,b)
        r2 = format((int(a,2)+int(b,2)) % (2**n), f'0{n}b')

        if r1 == r2:
            ok += 1
        else:
            fail += 1
            if len(errors) < 5:
                errors.append((a,b,r1,r2))

    print(ok, fail, ok/M)
    for e in errors:
        print(e)
    # 1000 0 1.0