# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
print ('Это программа, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
list = []
len_list = int(input('Ввыедите число, длину списка. '))
print ('введите "1" если хотите ввести список вручную или "0"заполнитть случайными числами')
hav = int(input())

if hav == 1:
    for i in range (len_list):
        list.append(int(input(f'Введите {i} число списка: ')))
else :
    range_random = int(input('Введите число  диапазон чисел от - до + '))
    for i in range (len_list):
        list.append(random.randint(-range_random, range_random))


sum_list = []
len_sum_list = 0 
if len_list % 2 == 0:
    len_sum_list = len_list // 2
    for i in range(1,len_sum_list+1):
        sum_list.append(list[i - 1] * list[-i])
else :
    len_sum_list = (len_list // 2) + 1
    for i in range (1,len_sum_list+1):
        if i == len_sum_list+1:
            sum_list.append(list[i] ** 2 )
        else:
            sum_list.append(list[i - 1] * list[-i])

print(f'Это список чисел: {list}')
print(f'Это сумма чисел: {sum_list}')