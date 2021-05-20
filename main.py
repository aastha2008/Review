'''
04/12/2021

Review

1. import turtle library
import turtle #Top of page

2. declare turtle instance(one turtle)
variable1 = turtle.Turtle()

3. declare screen (option)
variable2 =. turtle.Screen()

4. movements
  a. forward
  variable1.forward(DISTANCE)
  variable1.fd(DISTANCE)

  b. backward
  variable1.backward(DISTANCE)
  variable1.bk(DISTANCE)

  c. turn right
  variable1.right(ANGLE)

  d. turn left
  variable1.left(ANGLE)

5. pen features
   penup
   variable1.penup()

   pendown
   variable.pendown()

   move to a point(goto)
   variable.goto(x, y)

   move to the origin(home) - home means go to (0,0)
   variable1.home()

   color
   variable1.color(R,G,B) - 0-255 shades of each color

   shape (arrow, turtle, circle, square, classic)
   variable1.shape(SHAPE)

   speed (0,10)
   variable1.speed()

   write
   variable1.write(TEXT,MOVE,ALIGN,FONT)
   FONT = (FONTTYPE,FONTSIZE,FONTSTYLE)

   width (1,10)
   variable1.width()

   circle
   variable1.circle(RADIUS)
   variable1.circle(RADIUS, ANGLE)
   variable1.circle(RADIUS, ANGLE, SIDE)

   fill color
   variable1.fill("COLOR")

   variable1.begin_fill()
     #  SHAPE
   variable1.end_fill()
'''

