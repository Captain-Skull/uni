# Group: ИКБО-70-25
# Student: Мкртчян Георгий Грантович

def f(a: bool, b: bool, c: bool) -> bool:
	"""Минимизированная функция F = A ∨ (B ∧ C)."""
	return a or (b and c)


def original(a: bool, b: bool, c: bool) -> bool:
	"""Исходное выражение для проверки эквивалентности."""
	return (a or (b or c)) and (a or (b and c))


def verify_and_print():
	print("Упрощение:")
	print("F = (A ∨ (B ∨ C)) ∧ (A ∨ (B ∧ C))")
	print("= (A ∨ B ∨ C) ∧ (A ∨ (B ∧ C))  [ассоц./комм у дизъюнкции]")
	print("= A ∨ ((B ∨ C) ∧ (B ∧ C))       [(X∨Y)∧(X∨Z)=X∨(Y∧Z)]")
	print("= A ∨ (B ∧ C)                   [(B∧C) ⇒ (B∨C)]")
	print("Итог: F = A ∨ (B ∧ C)")
	print()

	print("Проверка эквивалентности (таблица истинности):")
	print("A B C | оригинальное упрощенное")
	all_equal = True
	for A in (False, True):
		for B in (False, True):
			for C in (False, True):
				o = original(A, B, C)
				s = f(A, B, C)
				print(f"{int(A)} {int(B)} {int(C)} |    {int(o)}        {int(s)}")
				if o != s:
					all_equal = False

	print()
	if all_equal:
		print("Результат: исходное выражение эквивалентно упрощённому для всех комбинаций.")


if __name__ == '__main__':
	verify_and_print()

## ОТВЕТ:

# Упрощение:
# F = (A ∨ (B ∨ C)) ∧ (A ∨ (B ∧ C))
# = (A ∨ B ∨ C) ∧ (A ∨ (B ∧ C))  [ассоц./комм у дизъюнкции]
# = A ∨ ((B ∨ C) ∧ (B ∧ C))       [(X∨Y)∧(X∨Z)=X∨(Y∧Z)]
# = A ∨ (B ∧ C)                   [(B∧C) ⇒ (B∨C)]
# Итог: F = A ∨ (B ∧ C)

# Проверка эквивалентности (таблица истинности):
# A B C | оригинальное упрощенное
# 0 0 0 |    0        0
# 0 0 1 |    0        0
# 0 1 0 |    0        0
# 0 1 1 |    1        1
# 1 0 0 |    1        1
# 1 0 1 |    1        1
# 1 1 0 |    1        1
# 1 1 1 |    1        1

# Результат: исходное выражение эквивалентно упрощённому для всех комбинаций.
