# Тетрадка 1: Перевод систем счисления

# 1. Перевод из произвольной системы в десятичную
num1 = input("Введите число: ")
base1 = int(input("Введите основание исходной системы: "))
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dec = 0
for ch in num1.upper():
    dec = dec * base1 + digits.index(ch)
print(f"Число {num1} в системе {base1} = {dec} в десятичной")

# 2. Перевод из десятичной методом последовательного деления
dec2 = int(input("Введите десятичное число: "))
base2 = int(input("Введите целевое основание: "))
n = dec2
res = ""
while n > 0:
    rem = n % base2
    res = digits[rem] + res
    n //= base2
print(f"{dec2} в системе {base2} = {res}")

# 3. Альтернативный метод (разложение по степеням)
dec3 = 123
base3 = 5
n = dec3
power = 1
while power * base3 <= n:
    power *= base3
res3 = ""
while power > 0:
    digit = n // power
    res3 += digits[digit]
    n %= power
    power //= base3
print(f"{dec3} в системе {base3} (метод разложения) = {res3}")

# 4. Универсальные функции с проверкой
def is_valid(num_str, base):
    for ch in num_str.upper():
        if ch not in digits[:base]:
            return False
    return True

def to_decimal(num_str, base):
    val = 0
    for ch in num_str.upper():
        val = val * base + digits.index(ch)
    return val

def from_decimal(num, base):
    if num == 0:
        return "0"
    n = num
    res = ""
    while n > 0:
        res = digits[n % base] + res
        n //= base
    return res

# 5. Проверка двойным преобразованием
test_num = "2A"
test_base = 11
if is_valid(test_num, test_base):
    dec_val = to_decimal(test_num, test_base)
    back = from_decimal(dec_val, test_base)
    print(f"Двойная проверка: {test_num} -> {dec_val} -> {back}, корректно: {back == test_num.upper()}")
else:
    print("Некорректное число")

# 6. Влияние основания на длину записи
num6 = 1000
print("Длина записи числа 1000 при разных основаниях:")
for b in [2, 3, 4, 5, 8, 10, 16]:
    repr6 = from_decimal(num6, b)
    print(f"Основание {b}: {repr6} (длина {len(repr6)})")

# 7. Серия переводов для одного числа
num7 = 255
print(f"Число {num7} в разных системах:")
for b in [2, 3, 4, 5, 8, 10, 16]:
    print(f"{b:2} : {from_decimal(num7, b)}")

# 8. Программа проверки корректности числа для заданного основания
inp = "10102"
base8 = 3
if is_valid(inp, base8):
    print(f"Число {inp} корректно для основания {base8}")
else:
    print(f"Число {inp} НЕ корректно для основания {base8}")

# 9. Исследование зависимости длины записи от основания
numbers = [10, 100, 1000, 10000]
bases = [2, 3, 4, 5, 8, 10, 16]
print("\nЭкспериментальная и теоретическая длина записи:")
for n in numbers:
    print(f"\nЧисло {n}:")
    for q in bases:
        exp_len = len(from_decimal(n, q))
        theory_len = int(math.log(n, q)) + 1 if n > 0 else 1
        print(f"q={q}: эксп={exp_len}, теор={theory_len}")

# 10. Сравнение методов перевода (последовательное деление и разложение)
def method_division(num, base):
    n = num
    res = ""
    while n > 0:
        res = digits[n % base] + res
        n //= base
    return res

def method_powers(num, base):
    if num == 0:
        return "0"
    n = num
    power = 1
    while power * base <= n:
        power *= base
    res = ""
    while power > 0:
        digit = n // power
        res += digits[digit]
        n %= power
        power //= base
    return res

test_nums = [0, 1, 127, 255, 1024]
base10 = 2
print("\nСравнение методов перевода:")
for n in test_nums:
    d_res = method_division(n, base10)
    p_res = method_powers(n, base10)
    print(f"{n:5} -> деление: {d_res:>10}, разложение: {p_res:>10}")

# Тетрадка 2: Перевод между системами степени двойки

# 1. Двоичное в восьмеричное (ручной и программный)
binary1 = "110101"
oct1 = format(int(binary1, 2), 'o')
print(f"Двоичное {binary1} -> восьмеричное {oct1}")

# 2. Двоичное в шестнадцатеричное группировкой
binary2 = "110101"
hex2 = format(int(binary2, 2), 'X')
print(f"Двоичное {binary2} -> шестнадцатеричное {hex2}")

# 3. Обратный перевод восьмеричное -> двоичное
oct3 = "65"
binary3 = format(int(oct3, 8), 'b')
print(f"Восьмеричное {oct3} -> двоичное {binary3}")

# 4. Обратный перевод шестнадцатеричное -> двоичное
hex4 = "2D"
binary4 = format(int(hex4, 16), 'b')
print(f"Шестнадцатеричное {hex4} -> двоичное {binary4}")

# 5. Прямой перевод восьмеричное <-> шестнадцатеричное через двоичную
oct5 = "65"
hex5 = format(int(oct5, 8), 'X')
print(f"Восьмеричное {oct5} -> шестнадцатеричное {hex5}")
hex5_2 = "2D"
oct5_2 = format(int(hex5_2, 16), 'o')
print(f"Шестнадцатеричное {hex5_2} -> восьмеричное {oct5_2}")

# 6. Проверка корректности обратным преобразованием
orig = "110101"
oct6 = format(int(orig, 2), 'o')
back = format(int(oct6, 8), 'b')
print(f"Двоичное {orig} -> восьмеричное {oct6} -> обратно {back}, совпадает: {back == orig}")

# 7. Влияние ведущих нулей
bin7 = "00110101"
oct7 = format(int(bin7, 2), 'o')
print(f"Двоичное {bin7} (ведущие нули) -> восьмеричное {oct7}")
print(f"Обратно: двоичное {format(int(oct7, 8), 'b')} (ведущие нули не сохраняются)")

# 8. Преимущества прямого метода
print("Перевод через двоичную удобен тем, что не требует десятичной арифметики и использует простую группировку бит.")

# 9. Исследование структуры представления (без десятичного значения)
binaries = ["1010", "110011", "11110000"]
print("\nСтруктурный анализ:")
for b in binaries:
    # группировка для восьмеричной
    while len(b) % 3 != 0:
        b = "0" + b
    oct_groups = [b[i:i+3] for i in range(0, len(b), 3)]
    oct_digits = ''.join(str(int(g,2)) for g in oct_groups)
    print(f"Двоичное: {b}, восьмеричное: {oct_digits}, группы: {oct_groups}")
    # группировка для шестнадцатеричной
    b2 = binaries[-1]  # возьмём другое
    b2_hex = b2
    while len(b2_hex) % 4 != 0:
        b2_hex = "0" + b2_hex
    hex_groups = [b2_hex[i:i+4] for i in range(0, len(b2_hex), 4)]
    hex_digits = ''.join(format(int(g,2), 'X') for g in hex_groups)
    print(f"Двоичное: {b2_hex}, шестнадцатеричное: {hex_digits}, группы: {hex_groups}")

# 10. Потери и сохранение информации
print("\nИнформация сохраняется полностью, так как группировка бит обратима. Ведущие нули в двоичном представлении могут быть утеряны, но само число восстанавливается однозначно.")

# Тетрадка 3: Арифметика в системах счисления

# 1. Поразрядное сложение двоичных чисел с фиксацией переносов
def add_bin(a, b):
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(len(a))
    carry = 0
    res = ""
    carries = []
    for i in range(len(a)-1, -1, -1):
        s = int(a[i]) + int(b[i]) + carry
        carries.append(carry)
        res = str(s % 2) + res
        carry = s // 2
    if carry:
        res = "1" + res
        carries.append(carry)
    return res, carries[::-1]

bin1, bin2 = "1011", "1101"
sum_bin, carries = add_bin(bin1, bin2)
print(f"Сложение {bin1} + {bin2} = {sum_bin}, переносы: {carries}")

# 2. Сложение в системе с основанием 6
def add_base(a, b):
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(len(a))
    carry = 0
    res = ""
    for i in range(len(a)-1, -1, -1):
        s = int(a[i], 6) + int(b[i], 6) + carry
        res = digits[s % 6] + res
        carry = s // 6
    if carry:
        res = digits[carry] + res
    return res

a6, b6 = "45", "23"
sum6 = add_base(a6, b6, 6)
print(f"{a6}(6) + {b6}(6) = {sum6}(6)")

# 3. Вычитание в восьмеричной системе
def sub_base(a, b):
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(len(a))
    borrow = 0
    res = ""
    for i in range(len(a)-1, -1, -1):
        da = int(a[i], 8) - borrow
        db = int(b[i], 8)
        if da < db:
            da += 8
            borrow = 1
        else:
            borrow = 0
        res = digits[da - db] + res
    return res.lstrip('0') or '0'

a8, b8 = "74", "35"
sub8 = sub_base(a8, b8, 8)
print(f"{a8}(8) - {b8}(8) = {sub8}(8)")

# 4. Алгоритм сложения в произвольной системе
def add_base(a, b, base):
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(len(a))
    carry = 0
    res = ""
    for i in range(len(a)-1, -1, -1):
        s = int(a[i], base) + int(b[i], base) + carry
        res = digits[s % base] + res
        carry = s // base
    if carry:
        res = digits[carry] + res
    return res

a6, b6 = "45", "23"
sum6 = add_base(a6, b6, 6)
print(f"{a6}(6) + {b6}(6) = {sum6}(6)")

# 5. Алгоритм вычитания в произвольной системе

def sub_base(a, b, base):
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(len(a))
    borrow = 0
    res = ""
    for i in range(len(a)-1, -1, -1):
        da = int(a[i], base) - borrow
        db = int(b[i], base)
        if da < db:
            da += base
            borrow = 1
        else:
            borrow = 0
        res = digits[da - db] + res
    return res.lstrip('0') or '0'

a8, b8 = "74", "35"
sub8 = sub_base(a8, b8, 8)
print(f"{a8}(8) - {b8}(8) = {sub8}(8)")

# 6. Проверка корректности сложения обратной операцией
sum_check = sum6
a_check, b_check = a6, b6
diff = sub_base(sum_check, b_check, 6)
print(f"Проверка: {sum_check} - {b_check} = {diff}, должно быть {a_check}, совпадает: {diff == a_check}")

# 7. Сравнение переносов при разных основаниях
num_a = "1010"
num_b = "1100"
bases_comp = [2, 3, 4, 5, 8, 10]
for base in bases_comp:
    a_dec = int(num_a, 2)
    b_dec = int(num_b, 2)
    a_str = from_decimal(a_dec, base)
    b_str = from_decimal(b_dec, base)
    def count_carries(a, b, base):
        a = a.zfill(max(len(a), len(b)))
        b = b.zfill(len(a))
        carry = 0
        count = 0
        for i in range(len(a)-1, -1, -1):
            s = int(a[i], base) + int(b[i], base) + carry
            carry = s // base
            if carry > 0:
                count += 1
        return count
    carries_cnt = count_carries(a_str, b_str, base)
    print(f"Основание {base}: {a_str} + {b_str}, переносов = {carries_cnt}")

# 8. Вывод о влиянии основания
print("Чем больше основание, тем меньше переносов, так как сумма цифр реже превышает основание.")

# 9. Подсчёт количества переносов для набора чисел
pairs = [("123", "456"), ("789", "321"), ("111", "222")]
bases_test = [2, 5, 8, 10]
print("\nКоличество переносов для разных пар чисел:")
for a_str, b_str in pairs:
    print(f"\nПара {a_str}, {b_str} (в десятичной):")
    for base in bases_test:
        a_dec = int(a_str)
        b_dec = int(b_str)
        a_rep = from_decimal(a_dec, base)
        b_rep = from_decimal(b_dec, base)
        cnt = count_carries(a_rep, b_rep, base)
        print(f"  base {base}: {a_rep} + {b_rep} -> {cnt} переносов")

# 10. Автоматическое выявление ошибок в алгоритме сложения
def correct_add(a, b, base):
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(len(a))
    carry = 0
    res = ""
    for i in range(len(a)-1, -1, -1):
        s = int(a[i], base) + int(b[i], base) + carry
        res = digits[s % base] + res
        carry = s // base
    if carry:
        res = digits[carry] + res
    return res

def faulty_add(a, b, base):
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(len(a))
    res = ""
    for i in range(len(a)-1, -1, -1):
        s = int(a[i], base) + int(b[i], base)
        res = digits[s % base] + res
    return res

test_pairs = [("12", "34", 5), ("77", "33", 8), ("101", "011", 2)]
for a, b, base in test_pairs:
    corr = correct_add(a, b, base)
    fault = faulty_add(a, b, base)
    print(f"{a} + {b} (base {base}): корректно = {corr}, с ошибкой = {fault}, различаются? {corr != fault}")