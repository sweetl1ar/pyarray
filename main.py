from random import randint
import time


# Функция для метода сортировки пузырьком
def bubble_sort(x):
    for m in range(0, len(x) - 1):
        for j in range(len(x) - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


# Циклический ввод при неверно введенных данных
while True:
    s = input('Введите количество элементов массива: ')
    try:
        n = int(s)
        break
    except:
        print('Введены непонятные символы. Введите количество элементов массива: ')
    else:
        print()
# Заполнение случайными числами
A = [0] * n
for i in range(n):
    A[i] = randint(-100, 100)
print(A)
t0 = time.time()
print(bubble_sort(A))
t1 = time.time()
print(f'Затраченное время: {t1 - t0}')

# Заполнение собственноручно
# a = []
# for i in range(n):
#     row = input('Введите элемент массива: ').split()
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     a.append(row)
# print(a)
# print(list(map(lambda x: x**2, A)))
#
# # Лямбда-функция
# f = lambda x, y: x + y
# print(f(5, 10))
#
# # Лямбда-функция для массива; возведение в квадрат каждого элемента
# L = [1, 2, 3, 4]
# print(list(map(lambda x: x**2, L)))
# Сортировка пузырьком без функции
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if A[j] > A[j + 1]:
#             A[j], A[j + 1] = A[j + 1], A[j]
#
# print(A)
