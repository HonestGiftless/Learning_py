from turtle import *

square = Turtle()
square.shape('turtle')

# Цикл для отрисовки квадрата
for _ in range(4):
    square.fd(100)
    square.right(90)

square.penup() # Поднятие ручки после отрисовки

star = Turtle() # Создание слоя
star.penup() # Поднятие ручки для перемещения отрисовки фигуры
star.goto(-200, -200) # Поставить курсор в позицию -200 (x) -200 (y)
star.pendown() # Опускаем ручку для того, чтобы начать рисовать

# Цикл для отрисовки звезды
for _ in range(5):
    star.fd(100)
    star.right(144)

star.penup()

exitonclick() # Для возможости закрытия окна по клику на него
done() # Для того, чтобы экран не закрывался
