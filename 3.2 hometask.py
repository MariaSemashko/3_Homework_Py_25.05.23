# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
# -> 5

import random

n = int(input("Введите число элементов массива: "))
d = int(input("Введите максимальное значение элементов массива: "))
task_2_list = [random.randint(0, d) for i in range(n)]
x = int(input("Введите целое число: "))

min_diff = d
position = 0
for i in range(len(task_2_list)):
    if abs(task_2_list[i] - x) < min_diff:
        min_diff = abs(task_2_list[i] - x)
        position = i


print(task_2_list)
print(f' Самое близкое число к {x} - это {task_2_list[position]}')