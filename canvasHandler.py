from projectiveFormulas import *
from Camera import Camera
from tkinter import *
from Object3D import *

width = 500.0
height = 300.0
c = Canvas(width = width, height = height, bg = 'white')
c.pack(expand=YES, fill = BOTH)
testVanishPoint = Point3D()
testVanishPoint.setYValue(100.0)
viewport = Camera()
viewport.setVanishPoint(testVanishPoint)

pointOne = Point3D(-10.0, 10.0, 20.0)
pointTwo = Point3D(10.0, 10.0, 20.0)
pointThree = Point3D(10.0, 10.0, -20.0)
pointFour = Point3D(-10, 10, -20)
testPlane = Plane()
testPlane.setPoints([pointOne, pointTwo, pointThree, pointFour])

# renderObject(c, viewport, testPlane)

def translateToCanvas(point, camera):
    abstractIntersection = Point3D()
    abstractIntersection = getIntersectionWithWindow(camera, point)
    returnPoint = abstractIntersection
    yComparisonValue = camera.window.getPoints()[0].getZVal()
    yComparisonPoint = point
    yComparisonPoint.setZValue(yComparisonValue)
    xComparisonPoint = camera.window.getPoints()[0]
    xComparisonPoint.setZValue(xComparisonPoint.getZVal() - returnPoint.getZVal())
    yDistance = get3dDistance(yComparisonPoint, abstractIntersection)
    xDistance = get3dDistance(xComparisonPoint, abstractIntersection)
    return (xDistance, yDistance)

def renderObject(c, camera, object):
    camera.rotateLeft()
    camera.rotateLeft()
    camera.rotateLeft()
    camera.rotateLeft()
    camera.rotateLeft()

    camera.rotateLeft()
    points = object.getPoints()
    polygonVertices = []
    for i in range(len(points)):
        polygonVertices.append(translateToCanvas(points[i], camera))
    #polygonVertices.append(translateToCanvas(points[0], camera))
    c.create_polygon(polygonVertices, fill = 'green', outline = 'black')
    c.bind("<Button>",camera.rotateLeft())
def testRotation(c, camera, object):
    while(TRUE):
        c.bind("<Button>",camera.rotateLeft())
        renderObject(c, camera, object)
        c.after(1000)
testRotation(c, viewport, testPlane)
