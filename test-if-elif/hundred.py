year = int(input('Enter the year: '))

third_n = year // 10 % 10
last_n = year % 10

if third_n == 0 and last_n == 0:
    print('YES')
else:
    print('NO')
