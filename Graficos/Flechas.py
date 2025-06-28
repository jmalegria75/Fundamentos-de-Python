import turtle
import time

# Se intentó por posicion pero por tiempo ya no le moví más
x = turtle.xcor
y = turtle.ycor

print(x)

for i in range(10):
    turtle.forward(15)
    turtle.penup()    
    turtle.forward(5)
    turtle.pendown()
    time.sleep(.5)

# Se mueve de posición.
turtle.penup()
turtle.backward(200)
turtle.left(90)
turtle.backward(100)
turtle.right(90)
turtle.pendown()

linea = 10.0
for j in range(10):
    turtle.forward(linea)
    turtle.penup()    
    turtle.forward(5)
    turtle.pendown()
    linea += 3.0
    time.sleep(.5)

time.sleep(5)