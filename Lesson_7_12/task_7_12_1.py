'''
Подвиг 1. Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:

s = input()

Результат отобразите на экране.

Sample Input:
5 6 3 6 -4 6 -1
Sample Output:
26
'''

st = input()

def decor1(start=5):
    def decor2(func):
        def decor3(*args):
            return start + func(*args)
        return decor3
    return decor2

def get_sum(st):
    lst = list(map(int, st.split()))
    return sum(lst)

print(decor1(5)(get_sum)(st))