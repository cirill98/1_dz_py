# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
value = int(input('Введите кол-во значений: '))
l = []
total = 0
for i in range(value):
    num = int(input('Введите значение: '))
    l.append(num)
for i in range(len(l)):
    if i != 0 and i % 2 != 0:
        total += l[i]
print(total)