'''
Подвиг 3. Вводится слово. Переменной msg присвоить строку "палиндром",
если введенное слово является палиндромом (одинаково читается и вперед и назад),
а иначе присвоить строку "не палиндром". Проверку проводить без учета регистра.
Программу реализовать с помощью тернарного условного оператора. Значение переменной msg отобразить на экране.

Sample Input:
Казак
Sample Output:
палиндром
'''

word = input()
msg = "палиндром" if word[::].lower() == word[::-1].lower() else "не палиндром"
print(msg)