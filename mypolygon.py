from tkinter import N
import turtle, math
bob = turtle.Turtle()
'''print(bob)'''

#Encaspsulation
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
    turtle.mainloop()

square(bob)

#Generalization
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()

square(bob, 160)

def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    turtle.mainloop()

polygon(bob, 50, 5)

#Interface design
def circle(t, r):
    circum = 2 * math.pi* r
    n = int(circum / 3) + 1
    length = circum / n
    polygon(t, length, n)
    turtle.mainloop()

circle(bob, 100)

