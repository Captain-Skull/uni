# Group: ИКБО-70-25
# Student: Мкртчян Георгий Грантович

def hex_digit(n: int) -> str:
	"""Возвращает шестнадцатеричное представление цифры 0..15 в виде символа."""
	if 0 <= n <= 9:
		return str(n)
	return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[n-10]


def int_to_hex(n: int) -> str:
	"""Преобразует неотрицательное целое в шестнадцатеричную строку (заглавные буквы)."""
	if n == 0:
		return "0"
	digits = []
	while n > 0:
		digits.append(hex_digit(n % 16))
		n //= 16
	return "".join(reversed(digits))


def hex_mul_table():
	"""Печать таблицы умножения для системы с основанием 16 (0..F)."""
	header = [hex_digit(i) for i in range(16)]
	# Заголовок
	print("    | " + " ".join(f"{h:>2}" for h in header))
	print("----+" + "---" * 16)
	for i in range(16):
		row = [int_to_hex(i * j) for j in range(16)]
		print(f" {hex_digit(i):>2} | " + " ".join(f"{r:>2}" for r in row))


def solve_task():
	A_hex = 'A'
	B_hex = '5'

	print("Таблица умножения в системе счисления с основанием 16 (0..F):")
	hex_mul_table()
	print()

	print(f"Исходные числа: {A_hex}_16 и {B_hex}_16")

	A_dec = int(A_hex, 16)
	B_dec = int(B_hex, 16)
	print("Шаг 1 — перевод цифр в десятичную систему:")
	print(f"{A_hex}_16 = {A_dec}_10")
	print(f"{B_hex}_16 = {B_dec}_10")
	print()

	product_dec = A_dec * B_dec
	print("Шаг 2 — умножение в десятичной системе:")
	print(f"{A_dec} × {B_dec} = {product_dec} (в десятичной)")
	print()

	print("Шаг 3 — перевод произведения в шестнадцатеричную систему (деление с остатком):")
	n = product_dec
	steps = []
	while n > 0:
		q, r = divmod(n, 16)
		steps.append((n, q, r))
		n = q
	for value, q, r in steps:
		print(f"{value} : 16 = {q} (частное), остаток {r} → цифра {hex_digit(r)}")
	hex_result = int_to_hex(product_dec)
	print()
	print(f"Собираем остатки снизу вверх → {hex_result}_16")
	print()

	print("Итог:")
	print(f"{A_hex}_16 × {B_hex}_16 = {hex_result}_16")
	print()

	back = int(hex_result, 16)
	print("Проверка (обратный перевод):")
	print(f"{hex_result}_16 = {back}_10")
	print(f"Сравнение: {back}_10 {'=' if back == product_dec else '!='} {product_dec}_10")


if __name__ == '__main__':
	solve_task()

## ОТВЕТ:

# Таблица умножения в системе счисления с основанием 16 (0..F):
#     |  0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
# ----+------------------------------------------------
#   0 |  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
#   1 |  0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
#   2 |  0  2  4  6  8  A  C  E 10 12 14 16 18 1A 1C 1E
#   3 |  0  3  6  9  C  F 12 15 18 1B 1E 21 24 27 2A 2D
#   4 |  0  4  8  C 10 14 18 1C 20 24 28 2C 30 34 38 3C
#   5 |  0  5  A  F 14 19 1E 23 28 2D 32 37 3C 41 46 4B
#   6 |  0  6  C 12 18 1E 24 2A 30 36 3C 42 48 4E 54 5A
#   7 |  0  7  E 15 1C 23 2A 31 38 3F 46 4D 54 5B 62 69
#   8 |  0  8 10 18 20 28 30 38 40 48 50 58 60 68 70 78
#   9 |  0  9 12 1B 24 2D 36 3F 48 51 5A 63 6C 75 7E 87
#   A |  0  A 14 1E 28 32 3C 46 50 5A 64 6E 78 82 8C 96
#   B |  0  B 16 21 2C 37 42 4D 58 63 6E 79 84 8F 9A A5
#   C |  0  C 18 24 30 3C 48 54 60 6C 78 84 90 9C A8 B4
#   D |  0  D 1A 27 34 41 4E 5B 68 75 82 8F 9C A9 B6 C3
#   E |  0  E 1C 2A 38 46 54 62 70 7E 8C 9A A8 B6 C4 D2
#   F |  0  F 1E 2D 3C 4B 5A 69 78 87 96 A5 B4 C3 D2 E1

# Исходные числа: A_16 и 5_16
# Шаг 1 — перевод цифр в десятичную систему:
# A_16 = 10_10
# 5_16 = 5_10

# Шаг 2 — умножение в десятичной системе:
# 10 × 5 = 50 (в десятичной)

# Шаг 3 — перевод произведения в шестнадцатеричную систему (деление с остатком):
# 50 : 16 = 3 (частное), остаток 2 → цифра 2
# 3 : 16 = 0 (частное), остаток 3 → цифра 3

# Собираем остатки снизу вверх → 32_16

# Итог:
# A_16 × 5_16 = 32_16

# Проверка (обратный перевод):
# 32_16 = 50_10
# Сравнение: 50_10 = 50_10