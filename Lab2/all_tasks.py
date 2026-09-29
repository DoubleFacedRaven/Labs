import random  # модуль для генерации случайных чисел


# Задание 1: сортировка выбором по возрастанию, числа из интервала [2; 103]
def task1():
    n = 15  # размер массива
    # randint включает обе границы, поэтому получаем числа 2..103
    a = [random.randint(2, 103) for _ in range(n)]

    print("Исходный массив:")
    print(*a)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    print("Отсортированный по возрастанию массив:")
    print(*a)


# Задание 2: сортировка по убыванию, числа из интервала [0; 100]
def task2():
    n = 15
    a = [random.randint(0, 100) for _ in range(n)]

    print("Исходный массив:")
    print(*a)

    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if a[j] > a[max_index]:
                max_index = j

        a[i], a[max_index] = a[max_index], a[i]

    print("Отсортированный по убыванию массив:")
    print(*a)


# Задание 3: сортировка выбором списка телефонов по возрастанию
def task3():
    # каждый телефон задан строкой формата XX-XX-XX
    phones = ["23-45-67", "12-34-56", "98-76-54", "23-45-60",
              "45-11-22", "10-20-30", "77-88-99", "23-44-99"]
    n = len(phones)

    print("Исходный список телефонов:")
    for p in phones:
        print(p)


    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if phones[j] < phones[min_index]:
                min_index = j
        phones[i], phones[min_index] = phones[min_index], phones[i]

    print("Отсортированный по возрастанию список:")
    for p in phones:
        print(p)


def main():
    print("=== Задание 1 ===")
    task1()

    print("\n=== Задание 2 ===")
    task2()

    print("\n=== Задание 3 ===")
    task3()


main()
