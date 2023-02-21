#Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:

#    «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

name = input('Enter the name ur favorite football team: ')
length = len(name)

print('Football team with name ' + name + ' has length ' + str(length) + ' symbols')
