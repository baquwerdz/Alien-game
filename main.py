import pgzrun
import random

WIDTH = 400
HEIGHT = 400

message = ""

alien = Actor("alien")

#alien.pos = 50,50

def draw():
    screen.clear()
    screen.fill("green")
    alien.draw()
    screen.draw.text(message,center = (400,10),fontsize = 30)

def move_alien():
    alien.x = random.randint(50,WIDTH - 50)
    alien.y = random.randint(50, WIDTH - 50)

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        message = "Good shot!"
        move_alien()
    else:
        message = "You missed."

move_alien()

pgzrun.go()