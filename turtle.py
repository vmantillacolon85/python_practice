#A program that demonstrates turtles stamping

import turtle

taylor = turtle.Turtle()
taylor.color("blue")
taylor.shape("turtle")

for i in range(8):
  taylor.forward(100)
  taylor.stamp()
  taylor.left(90)