'''
Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа.
(Простое число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.
'''

def get_simple():
    num = 2
    while True:
        check_num = 1
        count = 0
        while num >= check_num:
            if num % check_num == 0:
                count += 1
            check_num += 1
        if count == 2:
            yield num
        num += 1

gen = get_simple()
for i in range(20):
    print(next(gen), end=' ')