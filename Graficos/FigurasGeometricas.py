import turtle
import time

#Triangulo
for i in range(3):
    turtle.forward(50)
    turtle.left(120)    
    time.sleep(.5)

# Se mueve de posición.
turtle.penup()
turtle.forward(100)
turtle.pendown()

#Cuadrado
for i in range(4):
    turtle.forward(70)
    turtle.left(90)    
    time.sleep(.5)

# Se mueve de posición.
turtle.penup()
turtle.forward(140)
turtle.pendown()

#Pentagono
for i in range(5):
    turtle.forward(80)
    turtle.left(72)    
    time.sleep(.5)

time.sleep(.5)
