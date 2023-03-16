# Mapping cities
import turtle

#A function for scaling NYC coordinates to fit the map:
def scalePoints(lat,lon):
  newLat = (lat+73.964)*6300.0
  newLon = (lon-40.768)*9750.0
  return(newLat,newLon)


screen = turtle.Screen()

# this assures that the size of the screen will match the map image:
screen.setup(950, 900)
# now set the background to our space image
screen.bgpic("nycMap.jpg")

teddy = turtle.Turtle()
teddy.shape('circle')
teddy.penup()


#Go to Hunter: 115th Street Library:
teddy.color("purple")
teddy.goto(scalePoints(-73.954, 40.803))
teddy.stamp()

#Go to 125th Street Library
teddy.color("purple")
teddy.goto(scalePoints(-73.935, 40.803))
teddy.stamp()


#Go to 53rd Street Library
teddy.color("purple")
teddy.goto(scalePoints(-73.977, 40.761))
teddy.stamp()

#Go to 58th Street Library
teddy.color("purple")
teddy.goto(scalePoints(-73.969, 40.762))
teddy.stamp()


