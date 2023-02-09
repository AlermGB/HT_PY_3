# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

def fill_array(volume):
    main_list = []
    print(f'Последовательно введите элементы списка, всего {volume}: ')
    for i in range(volume):
        main_list.append(int(input()))
    return main_list
    

n = int(input('Задайте количество элементов списка: '))
list_1 = fill_array(n)
number = int(input('Близость к какому числу проверить? '))
less_difference = abs(int(list_1[0]) - number)
result_number = list_1[0]
for i in list_1[1:]:
    if abs(int(i) - number) < less_difference:
        less_difference = abs(int(i) - number)
        result_number = i
print(result_number)
    