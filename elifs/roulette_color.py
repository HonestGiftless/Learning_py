n = int(input())

if n == 0:
    print('зеленый')
elif 1 <= n <= 10 and n % 2 == 0:
    print('черный')
elif 1 <= n <= 10 and n % 2 != 0:
    print('красный')
elif 11 <= n <= 18 and n % 2 == 0:
    print('красный')
elif 11 <= n <= 18 and n % 2 != 0:
    print('черный')
elif 19 <= n <= 28 and n % 2 == 0:
    print('черный')
elif 19 <= n <= 28 and n % 2 != 0:
    print('красный')
elif 29 <= n <= 36 and n % 2 == 0:
    print('красный')
elif 29 <= n <= 36 and n % 2 != 0:
    print('черный')
elif n > 36 or n < 0:
    print('ошибка ввода')
