# Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.

text = input('Enter ur text: ')

if 'суббота' in text or 'воскресенье' in text:
    print('YES')
else:
    print('NO')
