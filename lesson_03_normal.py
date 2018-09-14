import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# Простое решение
# def fibonacci(n, m):
#
#     fnumber1 = 0
#     fnumber2 = 1
#
#     i = 0
#     while i < m:
#
#         if i >= n:
#             print(fnumber1)
#         fnumber1 = fnumber1 + fnumber2
#         i += 1
#
#         if i >= n:
#              print(fnumber2)
#         fnumber2 = fnumber1 + fnumber2
#         i += 1

#Решение при помощи формулы Бене
def fibonacci(n, m):

    list_f = []
    i = n
    while i <= m:
        number_f = (((1+math.sqrt(5))/2)**i-((1-math.sqrt(5))/2)**i)/math.sqrt(5)
        list_f.append(int(number_f))

        i += 1

    return list_f

list_f = fibonacci(10, 20)
print(list_f)



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):

    n = 1

    while n < len(origin_list):
        for i in range(len(origin_list) - 1):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
        n += 1

origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(origin_list)
print(origin_list)

# # Задача-3:
# # Напишите собственную реализацию стандартной функции filter.
# # Разумеется, внутри нельзя использовать саму функцию filter.
#
def even(number):

    if number % 2 == 0:
        return 1
    else:
        return 0


def origin_filter(func, origin_list):

    i = 1
    while i < len(origin_list):
        if func(origin_list[i]):
           i += 1
        else:
            origin_list.pop(i)


origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
origin_filter(even, origin_list)
print(origin_list)

# # Задача-4:
# # Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# # Определить, будут ли они вершинами параллелограмма.
#
def parallelogram(a1, a2, a3, a4):

    i = 0

    if math.fabs(a1[0] - a2[0]) == math.fabs(a3[0] - a4[0]) and math.fabs(a1[1] - a2[1]) == math.fabs(a3[1] - a4[1]):
        i += 1

    if math.fabs(a1[0] - a3[0]) == math.fabs(a2[0] - a4[0]) and math.fabs(a1[1] - a3[1]) == math.fabs(a2[1] - a4[1]):
        i += 1

    if math.fabs(a1[0] - a4[0]) == math.fabs(a2[0] - a3[0]) and math.fabs(a1[1] - a4[1]) == math.fabs(a2[1] - a3[1]):
        i += 1

    if i == 2:
        return 1
    else:
        return 0

a1 = [1,3]
a2 = [3,6]
#a2 = [7,6]
# это интересный вариант для проверки
a3 = [5,4]
a4 = [3,1]

if parallelogram(a1, a2, a3, a4):
    print('Это параллелограмм')
else:
    print('Это не параллелограмм')