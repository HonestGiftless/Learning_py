# Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все числа от m до n включительно.

m = int(input())
n = int(input())

if m <= n:
    for i in range(m, n+1):
        print(i)