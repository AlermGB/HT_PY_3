# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1


main_list = []
count = 0
n = int(input('Задайте количество элементов списка: '))
print(f'Последовательно введите элементы списка, всего {n}: ')
for i in range(n):
    main_list.append(int(input()))
print(main_list)
number = int(input('Какое число вас интересует? '))
for i in main_list:
    if i == number:
        count += 1
print(f'Количество повторений числа {number} в вашем списке: {count}')
