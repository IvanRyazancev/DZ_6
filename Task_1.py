# Задача №1. Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с 
# клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a = int(input("Введите первый элемент арифметической последовательности a: "))
k = int(input("Введите шаг приращения последовательности k: "))
n = int(input("Введите кол-во элементов последовательности n: "))
ariphm_array = []

def progress(a, k, n, ariphm_array):
    for i in range(n):
        ariphm_array.append(a)
        a = a + k    
    print(*ariphm_array)

progress(a, k, n, ariphm_array)