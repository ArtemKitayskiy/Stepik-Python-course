'''
Подвиг 3. Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n, то есть,
в диапазоне [2; n). Результат вывести на экран в строчку через пробел.

Sample Input:
11
Sample Output:
2 3 5 7
'''

n = int(input())
count = 0
for i in range(2, n):
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, end = ' ')
    count = 0
