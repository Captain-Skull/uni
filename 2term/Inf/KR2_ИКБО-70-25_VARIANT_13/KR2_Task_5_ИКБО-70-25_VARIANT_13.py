# Group: ИКБО-70-25
# Student: Мкртчян Георгий Грантович

def conveyor_on(e_stop: int, guard_closed: int, jam: int) -> int:
    """Вычисляет выход ConveyorOn по входам 0/1. Возвращает 0 или 1.

    Формула: ConveyorOn = ¬EStop ∧ GuardClosed ∧ ¬Jam
    """
    e = bool(e_stop)
    g = bool(guard_closed)
    j = bool(jam)
    result = (not e) and g and (not j)
    return int(result)


def print_truth_table():
    rows_with_one = []
    for EStop in (0, 1):
        for GuardClosed in (0, 1):
            for Jam in (0, 1):
                not_e = int(not EStop)
                not_j = int(not Jam)
                out = conveyor_on(EStop, GuardClosed, Jam)
                mark = "*" if out == 1 else ""
                print(f"  {EStop}       {GuardClosed}     {Jam}  |    {not_e}     {not_j}   |    {out} {mark}")
                if out == 1:
                    rows_with_one.append((EStop, GuardClosed, Jam))

    print()
    print("Строки, где ConveyorOn = 1:")
    for t in rows_with_one:
        print(f"  EStop={t[0]}, GuardClosed={t[1]}, Jam={t[2]}")
    print(f"Количество строк, где ConveyorOn = 1: {len(rows_with_one)}")
    print()


def minimization_explanation():
    print("Минимизация:")
    print("Исходное выражение задано в форме: ConveyorOn = ¬EStop ∧ GuardClosed ∧ ¬Jam")
    print("Это произведение литералов (конъюнкция переменных и/или их отрицаний) — уже минимальная (нет избыточных литералов).")
    print("Поэтому минимальная форма то же выражение: ConveyorOn = ¬EStop ∧ GuardClosed ∧ ¬Jam")
    print()


def example_io():
    print("Пример:")
    sample = (0, 1, 0) 
    out = conveyor_on(*sample)
    print(f"Ввод: {sample[0]} {sample[1]} {sample[2]}")
    print(f"Вывод: {out}  (ConveyorOn)")
    print()


if __name__ == '__main__':
    print_truth_table()
    minimization_explanation()
    example_io()

## ОТВЕТ:

#  0       0     0  |    1     1   |    0 
#   0       0     1  |    1     0   |    0 
#   0       1     0  |    1     1   |    1 *
#   0       1     1  |    1     0   |    0 
#   1       0     0  |    0     1   |    0 
#   1       0     1  |    0     0   |    0 
#   1       1     0  |    0     1   |    0 
#   1       1     1  |    0     0   |    0 

# Строки, где ConveyorOn = 1:
#   EStop=0, GuardClosed=1, Jam=0
# Количество строк, где ConveyorOn = 1: 1

# Минимизация:
# Исходное выражение задано в форме: ConveyorOn = ¬EStop ∧ GuardClosed ∧ ¬Jam
# Это произведение литералов (конъюнкция переменных и/или их отрицаний) — уже минимальная (нет избыточных литералов).
# Поэтому минимальная форма то же выражение: ConveyorOn = ¬EStop ∧ GuardClosed ∧ ¬Jam

# Пример:
# Ввод: 0 1 0
# Вывод: 1  (ConveyorOn)