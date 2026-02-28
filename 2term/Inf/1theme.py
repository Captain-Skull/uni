import math
import random

#1
I1 = math.log(64, 2)
print(I1, 'Количество информации при равновероятных сообщениях вычисляется по формуле I = log(2, n), где n - количество сообщений')

#2
I2 = math.log(10, 2)
print(I2, 'Количество информации при равновероятных сообщениях вычисляется по формуле I = log(2, n), где n - количество сообщений')

#3
p3 = [0.4, 0.3, 0.2, 0.1]
H3 = 0
for pi in p3:
    H3 -= pi * math.log(pi, 2)
print(H3, 'Энтропия меньше максимального значения для четырёх сообщений, что указывает на наличие предсказуемости в источнике информации.')

#4
p4 = [0.2, 0.2, 0.2, 0.2, 0.2]
H4 = 0
I4 = math.log(5, 2)
for pi in p4:
    H4 -= pi * math.log(pi, 2)
print(H4, ' ', I4, 'Для равновероятных исходов энтропия Шеннона в точности равна хартлиевскому количеству информации, поскольку последнее является частным случаем первой.')

#5
p5 = [0.6, 0.3, 0.1]
H5 = 0
for pi in p5:
    H5 -= pi * math.log(pi, 2)
print(H5, 'Неравномерность вероятностей уменьшает энтропию. Высокая вероятность одного сообщения снижает неопределённость, так как оно будет появляться чаще, а редкие события вносят малый вклад в среднюю информативность.')

#6
random.seed(21)
n = 8

raw = [random.random() for _ in range(n)]
total = sum(raw)

p6 = [x/total for x in raw]

H = -sum(pi * math.log(pi, 2) for pi in p6)
print("Случайное распределение вероятностей:", [round(pi, 4) for pi in p6])
print(f"Энтропия: {H:.4f} бит")
print(f"Максимальная энтропия (log2({n})): {math.log2(n):.4f} бит")
print(f"Энтропия полученного распределения {H:.4f} меньше максимально возможной (3 бита), что отражает неравномерность сгенерированных вероятностей. Чем ближе распределение к равномерному, тем выше энтропия.")

#7
n7 = 5
p_uniform = [1/n7] * n7
H_uniform = -sum(pi * math.log2(pi) for pi in p_uniform)
print(f"Равномерное распределение: p = {[round(p,2) for p in p_uniform]}, энтропия = {H_uniform:.4f} бит")

print("Постепенное увеличение неравномерности:")
for k in range(1, 6):
    p1 = k / (k + (n7-1))
    p_other = (1 - p1) / (n7-1)
    p = [p1] + [p_other] * (n7-1)
    H = -sum(pi * math.log2(pi) for pi in p)
    print(f"  p1 = {p1:.3f}, остальные = {p_other:.3f}, энтропия = {H:.4f} бит")

print("Вывод: по мере увеличения неравномерности (роста вероятности одного сообщения) энтропия уменьшается, так как неопределенность источника снижается.")


#8
N = 6
p8_uniform = [1/N] * N
H8_uniform = -sum(pi * math.log2(pi) for pi in p8_uniform)

p8_nonuniform = [0.5, 0.2, 0.1, 0.1, 0.05, 0.05]
H8_nonuniform = -sum(pi * math.log2(pi) for pi in p8_nonuniform)

print(f"Хартли (log2({N})): {math.log2(N):.4f} бит")
print(f"Энтропия Шеннона (равномерное): {H8_uniform:.4f} бит")
print(f"Энтропия Шеннона (неравномерное): {H8_nonuniform:.4f} бит")


#9
n9 = 4
max_entropy = math.log2(n9)

p9_1 = [0.25, 0.25, 0.25, 0.25]
H9_1 = -sum(pi * math.log2(pi) for pi in p9_1)

p9_2 = [0.4, 0.3, 0.2, 0.1]
H9_2 = -sum(pi * math.log2(pi) for pi in p9_2)

p9_3 = [0.7, 0.1, 0.1, 0.1]
H9_3 = -sum(pi * math.log2(pi) for pi in p9_3)

print(f"Распределение 1 (равномерное): {p9_1}, энтропия = {H9_1:.4f} бит")
print(f"Распределение 2 (умеренно неравномерное): {p9_2}, энтропия = {H9_2:.4f} бит")
print(f"Распределение 3 (сильно неравномерное): {p9_3}, энтропия = {H9_3:.4f} бит")
print(f"Максимальная энтропия для N={n9} (равномерное распределение): {max_entropy:.4f} бит")
print("Вывод: равномерное распределение даёт максимальную энтропию. Чем сильнее неравномерность, тем меньше энтропия, т.е. источник становится более предсказуемым.")


#10
frequencies = [5, 15, 25, 35, 20]
total = sum(frequencies)
probabilities = [f/total for f in frequencies]
print(f"Исходные частоты: {frequencies}")
print(f"Вероятности (преобразованы из частот): {[round(p,4) for p in probabilities]}")
print(f"Сумма вероятностей: {sum(probabilities):.2f} (условие нормировки выполнено)")

H_freq = -sum(p * math.log2(p) for p in probabilities)
print(f"Энтропия по Шеннону: {H_freq:.4f} бит")

frequencies2 = [90, 2, 2, 3, 3]
total2 = sum(frequencies2)
probabilities2 = [f/total2 for f in frequencies2]
H_freq2 = -sum(p * math.log2(p) for p in probabilities2)
print("\nИзменённые частоты (с доминирующим сообщением):", frequencies2)
print(f"Вероятности: {[round(p,4) for p in probabilities2]}")
print(f"Энтропия: {H_freq2:.4f} бит")

print("Вывод: при равномерном распределении частот (близких друг к другу) энтропия выше. При резком доминировании одного сообщения энтропия снижается, что указывает на высокую предсказуемость источника.")


# 2 тетрадка

import math
import random
from collections import Counter

# Вторая тетрадка: задачи по кодированию

# 1. Фиксированный двоичный код для алфавита {A, B, C, D}
print("\n1. Фиксированное кодирование")
alphabet = ['A', 'B', 'C', 'D']
fixed_code = {'A': '00', 'B': '01', 'C': '10', 'D': '11'}
message = "ABACABAD"
encoded_fixed = ''.join(fixed_code[ch] for ch in message)
print(f"Исходное сообщение: {message}")
print(f"Фиксированный код: {fixed_code}")
print(f"Закодированная последовательность: {encoded_fixed}")
print(f"Длина кода: {len(encoded_fixed)} бит")

# 2. Переменный код (Хаффмана) для того же сообщения
freq = Counter(message)
print(f"Частоты символов: {dict(freq)}")
var_code = {'A': '0', 'B': '10', 'C': '110', 'D': '111'}
encoded_var = ''.join(var_code[ch] for ch in message)
print(f"Переменный код: {var_code}")
print(f"Закодированная последовательность: {encoded_var}")
total_bits = len(encoded_var)
avg_len = total_bits / len(message)
print(f"Длина кода: {total_bits} бит")
print(f"Средняя длина кодового слова: {avg_len:.2f} бит/символ")

# 3. Байтовое кодирование (ASCII)
byte_encoded = message.encode('ascii')
print(f"Байтовое представление: {byte_encoded}")
print(f"Объём: {len(byte_encoded)} байт = {len(byte_encoded)*8} бит")

# 4. Декодирование сообщения, закодированного фиксированным кодом
reverse_fixed = {v: k for k, v in fixed_code.items()}
decoded_fixed = ''
bits = encoded_fixed
for i in range(0, len(bits), 2):
    chunk = bits[i:i+2]
    decoded_fixed += reverse_fixed[chunk]
print(f"Закодированная строка: {encoded_fixed}")
print(f"Декодированное сообщение: {decoded_fixed}")
print(f"Совпадение с исходным: {decoded_fixed == message}")

# 5. Сравнение объёмов
print(f"Фиксированный код: {len(encoded_fixed)} бит")
print(f"Переменный код: {len(encoded_var)} бит")
print(f"Байтовое кодирование: {len(byte_encoded)*8} бит")
print("Вывод: байтовое кодирование даёт избыточность 8 бит на символ; переменный код эффективнее фиксированного при неравномерных частотах.")

# 6. Влияние длины кодового слова на объём (для фиксированного кода)
for n_symbols in [2, 3, 4]:
    if n_symbols == 2:
        msg2 = "ABABABAB"
        code_len = 1
        vol = len(msg2) * code_len
        print(f"Алфавит из 2 символов, длина кодового слова = {code_len} бит, объём для 8 символов: {vol} бит")
    elif n_symbols == 3:
        msg3 = "ABACABAD"
        msg3 = "ABACABAB"
        code_len = 2
        vol = len(msg3) * code_len
        print(f"Алфавит из 3 символов, длина кодового слова = {code_len} бит, объём для 8 символов: {vol} бит")
    else: # n=4
        vol = len(message) * 2  # наш исходный код
        print(f"Алфавит из 4 символов, длина кодового слова = 2 бит, объём для 8 символов: {vol} бит")
print("Чем больше алфавит, тем больше бит требуется на символ при фиксированном коде, что увеличивает объём сообщения.")

# 7. Сравнение кодирования текстовой и числовой информации одинаковой длины
text = "1234"
number = 1234
text_bytes = text.encode('ascii')
print(f"Текст '{text}': {text_bytes}, объём = {len(text_bytes)*8} бит")
num_bits = number.bit_length()
print(f"Число {number}: битовая длина = {num_bits} бит (двоичное представление: {bin(number)})")
print(f"Если хранить как 4-байтовый int: 32 бита")
print("Вывод: текст фиксированной длины занимает больше места, чем число, если число мало, но при больших числах разница может сокращаться.")

# 8. Анализ избыточности
print("\n8. Избыточность кодирования")
probs = [freq[ch] / len(message) for ch in alphabet]
entropy = -sum(p * math.log2(p) for p in probs if p > 0)
print(f"Энтропия источника: {entropy:.3f} бит/символ")
print(f"Средняя длина фиксированного кода: {len(encoded_fixed)/len(message):.3f} бит/символ")
print(f"Средняя длина переменного кода: {avg_len:.3f} бит/символ")
print(f"Избыточность фиксированного кода: {len(encoded_fixed)/len(message) - entropy:.3f} бит/символ")
print(f"Избыточность переменного кода: {avg_len - entropy:.3f} бит/символ")
print("Переменный код ближе к энтропии, значит, избыточность меньше.")

# 9. Исследование устойчивости эффективности при случайных сообщениях
random.seed(42)
prob_dist = [0.4, 0.3, 0.2, 0.1]
symbols = ['A','B','C','D']
n_trials = 100
msg_len = 20
fixed_len_per_sym = 2  # бита
total_fixed = 0
total_var = 0
for _ in range(n_trials):
    msg = ''.join(random.choices(symbols, weights=prob_dist, k=msg_len))
    fixed_bits = len(msg) * fixed_len_per_sym
    total_fixed += fixed_bits
    var_bits = sum(len(var_code[ch]) for ch in msg)
    total_var += var_bits

avg_fixed = total_fixed / n_trials / msg_len
avg_var = total_var / n_trials / msg_len
print(f"Средняя длина на символ для {n_trials} случайных сообщений:")
print(f"Фиксированный код: {avg_fixed:.3f} бит")
print(f"Переменный код: {avg_var:.3f} бит")
print("Переменный код стабильно эффективнее, независимо от конкретного сообщения, так как использует статистические свойства.")

# 10. Влияние ограничений среды на выбор способа кодирования
max_len = 3

print(f"Ограничение: длина любого кодового слова <= {max_len} бит")
fixed_ok = all(len(v) <= max_len for v in fixed_code.values())
var_ok = all(len(v) <= max_len for v in var_code.values())
print(f"Фиксированный код соответствует: {fixed_ok} (макс. длина = {max(len(v) for v in fixed_code.values())})")
print(f"Переменный код соответствует: {var_ok} (макс. длина = {max(len(v) for v in var_code.values())})")
print("Если бы ограничение было 2 бита, переменный код пришлось бы модифицировать (использовать равномерный код или другой префиксный, укладывающийся в 2 бита).")
print("Вывод: при жёстких ограничениях на длину слова может потребоваться фиксированный код, даже если он менее эффективен.")


#3 тетрадка

# 1. Вычисление бита чётности и формирование кодового слова
message = "101011"
count_ones = message.count('1')
parity_bit = '0' if count_ones % 2 == 0 else '1'
codeword = message + parity_bit
print(f"Исходное сообщение: {message}")
print(f"Бит чётности (чётный контроль): {parity_bit}")
print(f"Кодовое слово: {codeword}")

# 2. Обнаружение ошибки при искажении двух битов (бит чётности)
print("\n2. Проверка обнаружения двух ошибок")
test_word = "1010111"
test_word = "1010110"
print(f"Исходное кодовое слово: {test_word}")
err_word = list(test_word)
err_word[0] = '1' if err_word[0]=='0' else '0'
err_word[2] = '1' if err_word[2]=='0' else '0'
err_word = ''.join(err_word)
print(f"Слово с двумя ошибками: {err_word}")
ones_err = err_word.count('1')
if ones_err % 2 == 0:
    print("Ошибка не обнаружена (чётность сохранилась)")
else:
    print("Ошибка обнаружена")
print("Вывод: при двух ошибках чётность может не измениться, поэтому ошибка не обнаруживается.")

# 3. Расстояние Хэмминга для двух двоичных слов
word1 = "101010"
word2 = "111010"
hamming_dist = sum(b1 != b2 for b1, b2 in zip(word1, word2))
print(f"Слово 1: {word1}")
print(f"Слово 2: {word2}")
print(f"Расстояние Хэмминга: {hamming_dist}")
print("Интерпретация: это количество позиций, в которых биты различаются, т.е. минимальное число ошибок, превращающих одно слово в другое.")

# 4. Кодирование методом троирования
msg4 = "101"
triple_code = ''.join(bit * 3 for bit in msg4)
print(f"Исходное сообщение: {msg4}")
print(f"Троированный код: {triple_code}")
print(f"Объём закодированной информации: {len(triple_code)} бит (исходный объём {len(msg4)} бит)")

# 5. Моделирование одиночной ошибки и восстановление по правилу большинства
triple = triple_code
print(f"Троированный код: {triple}")
err_triple = list(triple)
err_triple[2] = '1' if err_triple[2]=='0' else '0'
err_triple = ''.join(err_triple)
print(f"Код с ошибкой (индекс 2): {err_triple}")
restored = ''
for i in range(0, len(err_triple), 3):
    group = err_triple[i:i+3]
    ones = group.count('1')
    bit = '1' if ones >= 2 else '0'
    restored += bit
print(f"Восстановленное сообщение: {restored}")
print(f"Совпадение с исходным: {restored == msg4}")

# 6. Кодирование Хэмминга (7,4)
data_bits = [1, 0, 1, 0]  # d1,d2,d3,d4
d1, d2, d3, d4 = data_bits
p1 = d1 ^ d2 ^ d4
p2 = d1 ^ d3 ^ d4
p3 = d2 ^ d3 ^ d4
hamming_code = [p1, p2, d1, p3, d2, d3, d4]
print(f"Информационные биты (d1 d2 d3 d4): {data_bits}")
print(f"Проверочные биты: p1={p1}, p2={p2}, p3={p3}")
print(f"Кодовое слово Хэмминга: {hamming_code}")

# 7. Вычисление синдрома и определение позиции ошибки
received = hamming_code.copy()
received[3] ^= 1
print(f"Принятое слово (с ошибкой в бите p3): {received}")
s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
s3 = received[3] ^ received[4] ^ received[5] ^ received[6]
syndrome = (s3 << 2) | (s2 << 1) | s1
print(f"Синдром (s3 s2 s1): {s3}{s2}{s1} = {syndrome}")
if syndrome == 0:
    print("Ошибок нет")
else:
    error_pos = syndrome - 1
    print(f"Ошибка в позиции {error_pos} (0-индексация), что соответствует биту с индексом {error_pos}")

# 8. Исправление одиночной ошибки в коде Хэмминга
print("\n8. Исправление ошибки и восстановление исходных данных")
if syndrome != 0:
    received[error_pos] ^= 1
    print(f"Исправленное слово: {received}")
    restored_data = [received[2], received[4], received[5], received[6]]
    print(f"Восстановленные информационные биты: {restored_data}")
    print(f"Совпадение с исходными: {restored_data == data_bits}")
else:
    print("Ошибок не было, коррекция не требуется")

# 9. Экспериментальный анализ трёх методов
print("\n9. Экспериментальный анализ обнаружения и исправления ошибок")
import random
random.seed(42)
n_trials = 1000
results = {
    'parity': {'detected': 0, 'corrected': 0},
    'triple': {'detected': 0, 'corrected': 0},
    'hamming': {'detected': 0, 'corrected': 0}
}
for _ in range(n_trials):
    data = [random.randint(0,1) for _ in range(4)]
    ones = sum(data)
    parity = 0 if ones % 2 == 0 else 1
    codeword_par = data + [parity]
    err_pos = random.randint(0, 4)
    received_par = codeword_par.copy()
    received_par[err_pos] ^= 1
    ones_rec = sum(received_par)
    if ones_rec % 2 != 0:
        results['parity']['detected'] += 1
    triple_code = []
    for b in data:
        triple_code.extend([b, b, b])
    err_pos_t = random.randint(0, 11)
    received_triple = triple_code.copy()
    received_triple[err_pos_t] ^= 1
    decoded = []
    for i in range(0, 12, 3):
        group = received_triple[i:i+3]
        ones_g = sum(group)
        decoded.append(1 if ones_g >= 2 else 0)
    if decoded == data:
        results['triple']['detected'] += 1
        results['triple']['corrected'] += 1
    d1,d2,d3,d4 = data
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    h_code = [p1, p2, d1, p3, d2, d3, d4]
    err_pos_h = random.randint(0, 6)
    received_h = h_code.copy()
    received_h[err_pos_h] ^= 1
    s1 = received_h[0] ^ received_h[2] ^ received_h[4] ^ received_h[6]
    s2 = received_h[1] ^ received_h[2] ^ received_h[5] ^ received_h[6]
    s3 = received_h[3] ^ received_h[4] ^ received_h[5] ^ received_h[6]
    syn = (s3<<2)|(s2<<1)|s1
    if syn != 0:
        results['hamming']['detected'] += 1
        corr_pos = syn - 1
        received_h[corr_pos] ^= 1
        recovered = [received_h[2], received_h[4], received_h[5], received_h[6]]
        if recovered == data:
            results['hamming']['corrected'] += 1
    else:
        pass

print(f"Всего испытаний: {n_trials}")
print("Бит чётности:")
print(f"  Обнаружено ошибок: {results['parity']['detected']} ({results['parity']['detected']/n_trials:.2%})")
print(f"  Исправлено ошибок: {results['parity']['corrected']} (0%)")
print("Троирование:")
print(f"  Обнаружено и исправлено: {results['triple']['detected']} ({results['triple']['detected']/n_trials:.2%})")
print("Код Хэмминга (7,4):")
print(f"  Обнаружено ошибок: {results['hamming']['detected']} ({results['hamming']['detected']/n_trials:.2%})")
print(f"  Исправлено ошибок: {results['hamming']['corrected']} ({results['hamming']['corrected']/n_trials:.2%})")
print("Вывод: бит чётности только обнаруживает одиночные ошибки (100% detection), но не исправляет. Троирование и код Хэмминга исправляют все одиночные ошибки (100% correction). Код Хэмминга компактнее (7 бит вместо 12).")

# 10. Модуль моделирования передачи с ошибками
def parity_encode(data):
    ones = sum(data)
    parity = 0 if ones % 2 == 0 else 1
    return data + [parity]

def parity_check(received):
    ones = sum(received)
    return ones % 2 == 0  # True если чётность соблюдена (нет ошибки)

def triple_encode(data):
    code = []
    for b in data:
        code.extend([b, b, b])
    return code

def triple_decode(received):
    decoded = []
    for i in range(0, len(received), 3):
        group = received[i:i+3]
        ones = sum(group)
        decoded.append(1 if ones >= 2 else 0)
    return decoded

def hamming74_encode(data):
    d1,d2,d3,d4 = data
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4
    return [p1, p2, d1, p3, d2, d3, d4]

def hamming74_decode(received):
    s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
    s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
    s3 = received[3] ^ received[4] ^ received[5] ^ received[6]
    syndrome = (s3 << 2) | (s2 << 1) | s1
    if syndrome != 0:
        err_pos = syndrome - 1
        received[err_pos] ^= 1
    return [received[2], received[4], received[5], received[6]]

msg = [1, 0, 1, 1]
print(f"Исходное сообщение: {msg}")

enc_par = parity_encode(msg)
print(f"\n--- Бит чётности ---")
print(f"Закодировано: {enc_par}")
err_par = enc_par.copy()
err_par[2] ^= 1
print(f"Принято с ошибкой (индекс 2): {err_par}")
if not parity_check(err_par):
    print("Ошибка обнаружена!")
else:
    print("Ошибок не обнаружено (но они есть!)")

enc_triple = triple_encode(msg)
print(f"\n--- Троирование ---")
print(f"Закодировано: {enc_triple} (длина {len(enc_triple)})")
err_triple = enc_triple.copy()
err_triple[5] ^= 1
print(f"Принято с ошибкой: {err_triple}")
dec_triple = triple_decode(err_triple)
print(f"Декодировано: {dec_triple}")
print(f"Совпадение с исходным: {dec_triple == msg}")

enc_h = hamming74_encode(msg)
print(f"\n--- Код Хэмминга (7,4) ---")
print(f"Закодировано: {enc_h}")
err_h = enc_h.copy()
err_h[3] ^= 1
print(f"Принято с ошибкой: {err_h}")
dec_h = hamming74_decode(err_h)
print(f"После декодирования (с исправлением) данные: {dec_h}")
print(f"Совпадение с исходным: {dec_h == msg}")

print("\nМодуль демонстрирует этапы кодирования, внесения ошибки, обнаружения/исправления и восстановления исходного сообщения.")