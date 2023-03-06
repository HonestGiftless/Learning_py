# Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.

m = int(input())
n = int(input())

checked_m = m - 1 + m % 2

for i in range(checked_m, n - 1, -2):
    print(i)
