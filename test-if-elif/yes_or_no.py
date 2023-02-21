num = int(input('Enter the number: '))

if num % 2 != 0:
    print('YES')
elif 2 <= num <= 5 and num % 2 == 0:
    print('NO')
elif 6 <= num <= 20 and num % 2 == 0:
    print('YES')
elif num > 20 and num % 2 == 0:
    print('NO')
