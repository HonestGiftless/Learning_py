n = int(input('Введите трехзначное число: '))

fd = n // 100
sd = n // 10 % 10
ld = n % 10

print('Сумма цифр =', fd + sd + ld)
print('Произведение цифр =', fd * sd * ld)
