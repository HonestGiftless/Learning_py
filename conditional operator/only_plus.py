# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

a = int(input())
b = int(input())
c = int(input())
s = 0

if a > 0:
    s = s + a
if b > 0:
    s = s + b
if c > 0:
    s = s + c
print(s)
