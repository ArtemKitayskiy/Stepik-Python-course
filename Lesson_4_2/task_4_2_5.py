'''
Подвиг 5. Вводится порядковый номер месяца (1, 2, ..., 12). Вывести на экран количество дней в этом месяце.
Принять, что год не является високосным. Реализовать через условный оператор, в котором следует использовать не более трех ветвей (блоков).

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

Sample Input:
2
Sample Output:
28
'''

month_num = int(input())
num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 0 < month_num <= len(num_days):
    print(num_days[month_num-1])
else:
    print("Введен неверный номер")