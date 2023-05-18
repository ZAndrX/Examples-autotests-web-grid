def generate_fibonacci_number(n: int) -> int:
    """
    Генерация числа Фибоначчи
    :param n: Номер числа в последовательности
    :return: Число Фибоначчи с заданным номером в последовательности
    """
    tmp = [0, 1]
    while len(tmp) <= n:
        tmp.append(tmp[-1]+tmp[-2])
    return tmp[n]
