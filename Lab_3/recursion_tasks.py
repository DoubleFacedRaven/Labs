import sys

sys.setrecursionlimit(10**7)


# Задача 1. Вывести все числа от 1 до n
def print_to(n):
    if n > 0:
        print_to(n - 1)
        print(n)


# Задача 2. Вывести числа от A до B (по возрастанию, если A < B, иначе по убыванию)
def print_range(a, b):
    print(a)
    if a != b:
        print_range(a + 1 if a < b else a - 1, b)


# Задача 3. Сумма цифр числа N
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


# Задача 4. Простые делители числа n > 1 за O(sqrt(n))
def strip(n, d):
    # делит n на d, пока делится
    return strip(n // d, d) if n % d == 0 else n


def prime_divisors(n, d=2):
    if n == 1:
        return
    if d * d > n:  # остаток n - простое число
        print(n)
        return
    if n % d == 0:
        print(d)
        prime_divisors(strip(n, d), d + 1)
    else:
        prime_divisors(n, d + 1)


def main():
    task = int(input("Номер задачи (1-4): "))
    if task == 1:
        print_to(int(input()))
    elif task == 2:
        a = int(input())
        b = int(input())
        print_range(a, b)
    elif task == 3:
        print(digit_sum(int(input())))
    elif task == 4:
        prime_divisors(int(input()))


main()
