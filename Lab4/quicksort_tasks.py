import random
from functools import cmp_to_key


# ---------- Быстрая сортировка ----------
def quick_sort(a, left, right):
    i, j = left, right
    pivot = a[(left + right) // 2]
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if left < j:
        quick_sort(a, left, j)
    if i < right:
        quick_sort(a, i, right)


# ---------- Задача 1: 1000 целых чисел по возрастанию ----------
def task1():
    print("Введите 1000 целых чисел (через пробел или по одному в строке):")
    a = []
    while len(a) < 1000:
        a.extend(map(int, input().split()))
    a = a[:1000]
    quick_sort(a, 0, len(a) - 1)
    print(*a)


# ---------- Задача 2: случайный массив из интервала [50, 100] ----------
def task2():
    n = int(input("Размер массива: "))
    a = [random.randint(50, 100) for _ in range(n)]
    print("До сортировки:")
    print(*a)
    quick_sort(a, 0, n - 1)
    print("После сортировки:")
    print(*a)


# ---------- Задача 3: сортировка первого столбца двумерного массива ----------
ROWS = 8
COLS = 5


def task3():
    m = [[random.randint(5, 61) for _ in range(COLS)] for _ in range(ROWS)]

    print("Исходный массив:")
    for row in m:
        print(*(f"{x:3d}" for x in row))

    col = [row[0] for row in m]
    quick_sort(col, 0, ROWS - 1)
    for i in range(ROWS):
        m[i][0] = col[i]

    print("После сортировки первого столбца:")
    for row in m:
        print(*(f"{x:3d}" for x in row))


# ---------- Задача 4: список студентов по алфавиту (аналог qsort с компаратором) ----------
def cmp_names(a, b):
    return (a > b) - (a < b)


def task4():
    n = int(input("Количество студентов: "))
    print("Введите фамилии, по одной в строке:")
    names = [input().strip() for _ in range(n)]
    names.sort(key=cmp_to_key(cmp_names))
    print("Список по алфавиту:")
    for name in names:
        print(name)


def main():
    task = int(input("Номер задачи (1-4): "))
    if task == 1:
        task1()
    elif task == 2:
        task2()
    elif task == 3:
        task3()
    elif task == 4:
        task4()


main()
