# Mapping cities
import turtle

#A function for scaling NYC coordinates to fit the map:
def scalePoints(lon,lat):
  newLon = (lon+73.964)*6300.00  
  newLat = (lat-40.768)*9750.

  return(newLon,newLat)


screen = turtle.Screen()

# this assures that the size of the screen will match the map image:
screen.setup(950, 900)
# now set the background to our space image
screen.bgpic("nycMap.jpg")

teddy = turtle.Turtle()
teddy.shape('circle')
teddy.penup()


#Go to Hunter: (-73.964,40.768)
teddy.color("purple")
teddy.goto(scalePoints(-73.964,40.768))
teddy.stamp()


#Go to Apollo Theatre
teddy.color("purple")
teddy.goto(scalePoints(-73.950,40.810))
teddy.stamp()

#Go to Lincoln Center


