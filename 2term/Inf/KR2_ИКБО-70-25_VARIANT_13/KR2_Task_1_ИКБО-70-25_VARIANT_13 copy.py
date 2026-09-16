# Group: ИКБО-70-25
# Student: Мкртчян Георгий Грантович

import math


def info_volume(m_states: int, n_messages: int) -> dict:
	"""Вычисляет информационный объём в битах и байтах.

	Возвращает словарь с полями: bits, bytes, bits_per_message.
	"""
	bits_per_message = math.log2(m_states)
	total_bits = n_messages * bits_per_message
	total_bytes = total_bits / 8
	return {
		"bits_per_message": bits_per_message,
		"total_bits": total_bits,
		"total_bytes": total_bytes,
	}


def main():
	M = 9
	N = 100
	res = info_volume(M, N)

	print("Формулы:")
	print("I1 = log2(M) бит")
	print("I = N * I1 бит")
	print()
	print(f"Дано: M = {M} состояний, N = {N} сообщений")
	print()
	print("Расчёт:")
	print(f"I1 = log2({M}) = {res['bits_per_message']:.6f} бит (информация одного сообщения)")
	print(f"I = {N} * {res['bits_per_message']:.6f} = {res['total_bits']:.3f} бит")
	print(f"Перевод в байты: B = I / 8 = {res['total_bytes']:.3f} байт")


if __name__ == '__main__':
	main()

## ОТВЕТ:

# Формулы:
# I1 = log2(M) бит
# I = N * I1 бит

# Дано: M = 9 состояний, N = 100 сообщений

# Расчёт:
# I1 = log2(9) = 3.169925 бит (информация одного сообщения)
# I = 100 * 3.169925 = 316.993 бит
# Перевод в байты: B = I / 8 = 39.624 байт