# Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.

mail = input('Enter ur email adress: ')

if "@" in mail and "." in mail:
    print('YES')
else:
    print('NO')
