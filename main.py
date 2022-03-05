from random import randint
#Циклический ввод при неверно введенных данных
while True:
    s = input('Введите количество элементов массива: ')
    try:
        n = int(s)
        break
    except:
        print('Введены непонятные символы. Введите количество элементов массива: ')
    else:
        print()

#Заполнение собственноручно
# a = []
# for i in range(n):
#     row = input('Введите элемент массива: ').split()
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     a.append(row)
# print(a)

#Заполнение случайными числами
A = [0] * n
for i in range(n):
    A[i] = randint(-100, 100)
print(A)
print(list(map(lambda x: x**2, A)))

# Лямбда-функция
f = lambda x, y: x + y
print(f(5, 10))
# Лямбда-функция для массива; возведение в квадрат каждого элемента
L = [1, 2, 3, 4]
print(list(map(lambda x: x**2, L)))
