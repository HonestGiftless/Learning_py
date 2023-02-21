#Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.

num = int(input('Введите число: '))

first_n = num // 1000 # Первая цифра
last_n = num % 10 # Последняя цифра
num_2 = num // 100 % 10 # Вторая цифра
num_3 = num // 10 % 10 # Третья цифра

if first_n + last_n == num_2 - num_3:
    print("ДА")
else:
    print("НЕТ")