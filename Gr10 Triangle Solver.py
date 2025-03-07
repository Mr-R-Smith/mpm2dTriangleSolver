from fractions import Fraction
import math
import turtle as T

def slopeFinder(x1,y1,x2,y2, segment):
  deltaY = y2 - y1
  deltaX = x2 - x1
  if deltaX < 0 and deltaY < 0:
    deltaX = abs(deltaX)
    deltaY = abs(deltaY)
  overallSlope = Fraction(deltaY, deltaX)
  print(f"The slope of segment {segment} is {overallSlope}")
  return overallSlope

def negRecip(x1,y1,x2,y2):
  deltaY = y2 - y1
  deltaX = x2 - x1
  if deltaX < 0 and deltaY < 0:
    deltaX = abs(deltaX)
    deltaY = abs(deltaY)
  overallSlope = -1*Fraction(deltaX,deltaY)
  return overallSlope

def lenOfSeg(x1,y1,x2,y2, segment):
  squareDiffY = (y2 - y1)**2
  squareDiffX = (x2 - x1)**2
  length = math.sqrt(squareDiffX+squareDiffY)
  print(f"The length of the segment {segment} is: {length} OR √{squareDiffX+squareDiffY}")

def midPoint(x1,y1,x2,y2):
  xcoord = Fraction(x1 + x2,2)
  ycoord = Fraction(y1 + y2,2)
  return xcoord, ycoord

def yIntSolver(slope, x1, y1):
  yInt = y1 - (slope*x1)
  return yInt

def medianSolver(x1, y1, x2, y2, segment, point):
  mOfMedian = slopeFinder(x1, y1, x2, y2, "median")
  bOfMedian = yIntSolver(mOfMedian, x1, y1)
  print(f"The equation of the median from point {point} to the midpoint of {segment} is:")
  print(f"y = {mOfMedian}x +{bOfMedian}")

def altitudeSolver(x1, y1, negrecip, segment, point):
  bOfMedian = yIntSolver(negrecip, x1, y1)
  print(f"The equation of the altitude from point {point} to the segment {segment} is:")
  print(f"y = {negrecip}x + {bOfMedian}")
  

def findIntersection(x1,y1,y2,x3,y3,y4):
  x2= 0
  x4 = 0
  
  PTA = (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4)
  PTB =  (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
  PTC = (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4)
  PTD =  (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
  px= Fraction(PTA, PTB) 
  py= Fraction(PTC, PTD)
  return [px, py]

def line_intersection(line1, line2):
  xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
  ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

  def det(a, b):
      return a[0] * b[1] - a[1] * b[0]

  div = det(xdiff, ydiff)
  if div == 0:
     raise Exception('lines do not intersect')

  d = (det(*line1), det(*line2))
  x = det(d, xdiff) / div
  y = det(d, ydiff) / div
  return x, y

#inital set-up
T.hideturtle()
T.setup(800, 800)
 
#Define size of drawing screen/canvas and colour
T.screensize(400, 400, bg='lightblue')
 
T.setworldcoordinates(-15, -15, 15, 15)  # Custom coordinate system

#draw the cartesian grid - do this in the main.py 
T.forward (18)
T.back (36)
T.home()
T.left (90)
T.forward (8)
T.back (16)
T.home()
T.penup()

T.pensize(2)



def turtleMovementPart(x, y):
  T.goto(x,y)
  T.color("red")
  T.dot()
  T.write(f"({x}, {y})")
  T.color('blue')
  T.pendown()


pointAX = -3
pointAY = 5
pointBX = 4
pointBY = 2
pointCX = -2
pointCY = -5

turtleMovementPart(pointAX, pointAY)
turtleMovementPart(pointBX, pointBY)
turtleMovementPart(pointCX, pointCY)
turtleMovementPart(pointAX, pointAY)

print(f"The points are A({pointAX},{pointAY}), B({pointBX},{pointBY}) and C({pointCX},{pointCY})!")
print(" ")

print("SLOPES!")
mAB = slopeFinder(pointAX, pointAY, pointBX, pointBY, "AB")
mBC = slopeFinder(pointBX, pointBY, pointCX, pointCY, "BC")
mAC = slopeFinder(pointAX, pointAY, pointCX, pointCY, "AC")
print(" ")



perpAB = negRecip(pointAX, pointAY, pointBX, pointBY)
perpBC = negRecip(pointBX, pointBY, pointCX, pointCY)
perpAC = negRecip(pointAX, pointAY, pointCX, pointCY)

print("NEGATIVE RECIPROCALS")
print(f"The negative reciprocal of AB is {perpAB}")
print(f"The negative reciprocal of BC is {perpBC}")
print(f"The negative reciprocal of AC is {perpAC}")
print(" ")
print("Length of line segments")
lenAB = lenOfSeg(pointAX, pointAY, pointBX, pointBY, "AB")
lenBC = lenOfSeg(pointBX, pointBY, pointCX, pointCY, "BC")
lenAC = lenOfSeg(pointAX, pointAY, pointCX, pointCY, "AC")
print(" ")
print("Midpoints of line Segement:")
midABX , midABY  = midPoint(pointAX, pointAY, pointBX, pointBY)
midBCX , midBCY = midPoint(pointBX, pointBY, pointCX, pointCY)
midACX , midACY = midPoint(pointAX, pointAY, pointCX, pointCY)

print(f"The mid point of AB is: ({midABX} , {midABY})")
print(f"The mid point of BC is: ({midBCX} , {midBCY})")
print(f"The mid point of AC is: ({midACX} , {midACY})")



print(" ")
print("Equations of perpendicular bisectors:")

yIntPerpBisectAB = yIntSolver(perpAB,midABX, midABY)
print(f"The equation of the perpendicular bisector of AB is y={perpAB}x+{yIntPerpBisectAB}")

yIntPerpBisectBC = yIntSolver(perpBC,midBCX, midBCY)
print(f"The equation of the perpendicular bisector of BC is y={perpBC}x+{yIntPerpBisectBC}")

yIntPerpBisectAC = yIntSolver(perpAC,midACX, midACY)
print(f"The equation of the perpendicular bisector of AC is y={perpAC}x+{yIntPerpBisectAC}")


print(" ")
print("POI:")
POIX, POIY = findIntersection(midABX, midABY, yIntPerpBisectAB, midBCX, midBCY, yIntPerpBisectBC)

print(f"The POI is ({POIX},{POIY})")

T.penup()

for x in range(-20,15,5):
  y = perpAB * x + yIntPerpBisectAB
  T.goto(x,y)
  T.color("green")
  T.pd()
  
T.penup()

for x in range(-20,15,5):
  y = perpBC * x + yIntPerpBisectBC
  T.goto(x,y)
  T.color("orange")
  T.pd()

print(f"The POI is ({POIX},{POIY})")
T.penup()
T.goto(POIX,POIY)
T.color("red")
T.dot()
T.write(f"({POIX}, {POIY})")
T.color('blue')
T.pendown()

print(" ")
print("Equation of the median")
medianSolver(pointAX, pointAY, midBCX, midBCY, "BC", "A")
medianSolver(pointBX, pointBY, midACX, midACY, "AC", "B")
medianSolver(pointCX, pointCY, midABX, midABY, "AB", "C")

print(" ")
print("Equation of altitude")
altitudeSolver(pointAX, pointAY, perpBC, "BC", "A")
altitudeSolver(pointBX, pointBY, perpAC, "AC", "B")
altitudeSolver(pointCX, pointCY, perpAB, "AB", "C")


T.mainloop()  #keeps the drawing visible on the screen