# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в 
# массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


n = int(input("Введите кол-во элементов: "))
list_1 = []
for i in range(n):
    digit = int(input("Введите элемент массива: "))
    list_1.append(digit)

x = int(input("Введите x: "))
razn = abs(x - list_1[0])

element = list_1[0]

for i in list_1:
    diff = abs(x-i)
    if diff < razn:
        razn = diff
        element = i
    
print(element)