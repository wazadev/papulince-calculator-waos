import turtle
import math

# Función z(θ)
def z(theta):
    return math.e**(theta*1j) + math.e**(1.618033988749895*theta*1j)

# Función para dibujar el fractal
def draw_fractal(t, scale=100, theta_range=1000, step_size=0.01):
    t.penup()
    t.goto(z(0).real*scale, z(0).imag*scale)
    t.pendown()
    for i in range(int(theta_range/step_size)):
        theta = i * step_size
        next_point = z(theta)
        t.goto(next_point.real*scale, next_point.imag*scale)

# Configuración de la ventana
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Fractal con z(θ)")

# Configuración de la tortuga
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.color('blue')

# Dibujo del fractal
draw_fractal(t, scale=100, theta_range=500, step_size=0.01)

# Cierre de la ventana al hacer clic en ella
screen.exitonclick()
