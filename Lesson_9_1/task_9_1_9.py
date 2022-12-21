'''
Подвиг 9. Имеется график функции f(x) = 0.5x^2 - 2.
Необходимо записать генератор, который бы выдавал значения этой функции для аргумента x в диапазоне [a; b] с шагом 0.01.
Величины a, b вводятся с клавиатуры в одну строчку через пробел как целые числа (a< b).
Вывести на экран первые 20 значений функции с точностью до сотых, взятых из генератора.

P.S. Значения функции вычислять командой:

f(x) = 0.5 * pow(x, 2) - 2.0

Sample Input:
0 10
Sample Output:
-2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -1.99 -1.99 -1.99 -1.99 -1.99 -1.99 -1.99 -1.98 -1.98
'''

a, b = map(int, input().split())

gen = (round(0.5 * pow(x/100, 2) - 2.0, 2) for x in range(a*100, b*100, 1))
print(*[next(gen) for _ in range(20)])   