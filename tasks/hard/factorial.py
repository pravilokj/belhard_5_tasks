"""
Вычисление факториала

Факториалом числа называют произведение всех натуральных
чисел до него включительно.

Например, факториал числа 5 равен произведению 1 * 2 * 3 * 4 * 5 = 120.

Формула нахождения факториала:
n! = 1 * 2 * … * n, где n – это число, а n! – факториал этого числа.
"""


def factorial(n: int) -> int:
    if n < 1:
        raise ValueError("n must be higher than 0")
    current = 1
    for i in range(2, n + 1):
        current *= i
    return current


if __name__ == '__main__':
    assert factorial(5) == 120
    print('Решено!')
