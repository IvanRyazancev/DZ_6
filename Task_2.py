# Задача №2. Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не 
# больше заданного максимума) Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 
# 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 
# Диапазон от 6 до 12
# 
# Вывод: [1, 9, 13, 14, 19]
from random import randint
import random

n = int(input("Введите кол-во элементов массива: "))
n1 = int(input("Введите первый элемент диапазона: "))
n2 = int(input("Введите последний элемент диапазона: "))
array_2 = []
array_1 = []

def first_array(n, array_1):
    for i in range(n):
        x = random.randint(-100, 100)
        array_1.append(x)
    print(*array_1)

def index_array(array_1, n1, n2, array_2):
    for i in range(len(array_1)):
        if array_1[i] > n1 and array_1[i] < n2:
            array_2.append(i)
    print(*array_2)

first_array(n, array_1)
index_array(array_1, n1, n2, array_2)