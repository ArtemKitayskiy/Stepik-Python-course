'''
Подвиг 4. Вводятся две строки из слов (слова записаны через пробел).
Объявите функцию, которая преобразовывает эти две строки в два списка слов и возвращает эти списки.

Определите декоратор для этой функции, который из двух списков формирует словарь,
в котором ключами являются слова из первого списка, а значениями - соответствующие элементы из второго списка.
Полученный словарь должен возвращаться при вызове декоратора.

Примените декоратор к первой функции и вызовите ее для введенных строк. Результат (словарь d) отобразите на экране командой:

print(*sorted(d.items()))

Sample Input:
house river tree car
дом река дерево машина
Sample Output:
('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')
'''

s1 = input()
s2 = input()

def get_tuple(func):
    def wrapper(*args):
        s1, s2 = func(*args)
        return {s1[i]:s2[i] for i in range(min(len(s1), len(s2)))}
    return wrapper

@get_tuple
def get_lst(s1, s2):
    return (s1.split(), s2.split())

d = get_lst(s1, s2)
print(*sorted(d.items()))