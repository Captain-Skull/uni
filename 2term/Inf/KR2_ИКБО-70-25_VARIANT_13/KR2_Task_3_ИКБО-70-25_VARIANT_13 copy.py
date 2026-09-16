# Group: ИКБО-70-25
# Student: Мкртчян Георгий Грантович

def implication(a: int, b: int) -> int:
	"""Логическая импликация A → B (возвращает 0 или 1)."""
	return 1 if (not a) or b else 0


def build_truth_table():
	"""Строит таблицу истинности для F = (A → B) ⊕ C и печатает шаги."""
	print("F = (A → B) ⊕ C")
	print()
	combos = []
	for A in (0, 1):
		for B in (0, 1):
			for C in (0, 1):
				imp = implication(A, B)
				F = imp ^ C
				combos.append((A, B, C, imp, F))

	print("A B C | F")
	for A, B, C, imp, F in combos:
		print(f"{A} {B} {C} | {F}")

	count_ones = sum(row[4] for row in combos)

	print()
	print(f"Количество строк, где F = 1: {count_ones}")


if __name__ == '__main__':
	build_truth_table()

## ОТВЕТ:

# F = (A → B) ⊕ C

# A B C | F
# 0 0 0 | 1
# 0 0 1 | 0
# 0 1 0 | 1
# 0 1 1 | 0
# 1 0 0 | 0
# 1 0 1 | 1
# 1 1 0 | 1
# 1 1 1 | 0

# Количество строк, где F = 1: 4