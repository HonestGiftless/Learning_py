# Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.

text = input('Enter ur text: ')

if 'синий' in text:
    print('YES')
else:
    print('NO')