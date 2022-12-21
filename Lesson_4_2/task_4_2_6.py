'''
Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число).
По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. Вывести предыдущую дату и следующую дату
(в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

Sample Input:
8 31
Sample Output:
08.30 09.01
'''

m, n = map(int, input().split())
num_days =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 0 < m <= 12:
    if (m == 12 and n == 31) or (m == 1 and n == 1):
        print("m и n не характеризуют 1 января и 31 декабря")
    elif n == num_days[m-1]:
        print(f'{str(m).rjust(2, "0")}.{n - 1} {str(m + 1).rjust(2, "0")}.01')
    elif n == 1:
        print(f'{str(m - 1).rjust(2, "0")}.{num_days[m-1]} {str(m).rjust(2, "0")}.{str(n + 1).rjust(2, "0")}')
    elif 1 < n < num_days[m-1]:
        print(f'{str(m).rjust(2, "0")}.{str(n - 1).rjust(2, "0")} {str(m).rjust(2, "0")}.{str(n + 1).rjust(2, "0")}')
    else:
        print('Введено неверное число')
else:
    print('Введен неверный номер месяца')