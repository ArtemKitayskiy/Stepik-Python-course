'''
Подвиг 5. Вводится список email-адресов в одну строчку через пробел. Среди них нужно оставить только корректно записанные адреса.
Будем полагать, что к таким относятся те, что используют латинские буквы, цифры и символ подчеркивания.
А также в адресе должен быть символ "@", а после него символ точки "." (между ними, конечно же, могут быть и другие символы).

Результат отобразить в виде строки email-адресов, записанных через пробел.

Sample Input:

abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
Sample Output:

abc@it.ru biba123@list.ru sc_lib@list.ru
'''

from string import ascii_lowercase, ascii_uppercase, digits

symbols = ascii_lowercase + ascii_uppercase + digits + '_.@'
addresses = input().split()

def check_email(s):
    if s.count('@') != 1:
        return False

    before, after = s.split('@')
    if '.' in before or after.count('.') != 1:
        return False

    for i in s:
        if i != '@' and i != '.':
            if i not in symbols:
                return False

    return True

print(*filter(check_email, addresses))