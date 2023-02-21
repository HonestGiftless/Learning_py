n = int(input('Введите трехзначное число: '))

fd = n // 100
sd = n // 10 % 10
td = n % 10

print(fd, sd, td, sep='')
print(fd, td, sd, sep='')
print(sd, fd, td, sep='')
print(sd, td, fd, sep='')
print(td, fd, sd, sep='')
print(td, sd, fd, sep='')
