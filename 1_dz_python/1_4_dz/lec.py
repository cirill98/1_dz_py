# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
n = input()
if n == '1 четверть':
    print('x > 0 и y > 0')
elif n == '2 четверть':
    print('x < 0 и y > 0')
elif n == '3 четверть':
    print('x < 0 и y < 0')
elif n == '4 четверть':
    print('x > 0 и y < 0')
