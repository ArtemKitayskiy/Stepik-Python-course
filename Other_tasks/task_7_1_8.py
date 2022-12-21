'''
Подвиг 8. Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки.
Будем полагать, что адрес верен, если он обязательно содержит символы '@' и '.',
а все остальные символы могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен, то функция выводит ДА, иначе - НЕТ.

После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.

Sample Input:
sc_lib@list.ru
Sample Output:
ДА
'''


def check_address(email):
    flag = 'ДА'
    if '@' and '.' in email:
        email = email.replace('@', '')
        email = email.replace('.', '')
        for i in email.lower():
            if not ('a' <= i <= 'z' or '0' <= i <= '9' or i == '_'):
                flag = 'НЕТ'
                break
    else:
        flag = 'НЕТ'
    print(flag)


check_address(input())
