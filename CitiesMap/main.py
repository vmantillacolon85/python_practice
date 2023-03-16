# Mapping cities
import turtle

screen = turtle.Screen()

# this assures that the size of the screen will match the map image:
screen.setup(800, 404)
#Set coordinates for latitude and longitude:
screen.setworldcoordinates(-180,-90,180,90)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("mapNASA.jpg")

teddy = turtle.Turtle()
teddy.shape('circle')
teddy.color('red')
teddy.penup()


#Go to NYC:
teddy.goto(-74,41)
teddy.stamp()

#Go to origin:
teddy.goto(0,0)
teddy.stamp()

#Go to Los Angeles:
teddy.goto(-118, 34)
teddy.stamp()

#Go to Paris:
teddy.goto(2, 49)
teddy.stamp()

#Go to Hong Kong:
teddy.goto(114,22)
teddy.stamp

