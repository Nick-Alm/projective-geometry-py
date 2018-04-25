from projectiveFormulas import *
from Camera import Camera
from tkinter import *
from Object3D import *
import copy

width = 500.0
height = 300.0
c = Canvas(width = width, height = height, bg = 'white')
c.pack(expand=YES, fill = BOTH)
testVanishPoint = Point3D()
testVanishPoint.setYValue(10.0)
viewport = Camera()
viewport.setVanishPoint(testVanishPoint)
viewport.setWindowDistance(50.0)

pointOne = Point3D(-10.0, 5.0, 20.0)
pointTwo = Point3D(10.0, 5.0, 20.0)
pointThree = Point3D(10.0, 15.0, -20.0)
pointFour = Point3D(-10.0, 15.0, -20.0)
testPlane = Plane()
testPlane.setPoints([pointOne, pointTwo, pointThree, pointFour])

# renderObject(c, viewport, testPlane)

def translateToCanvas(point, camera):
    abstractIntersection = Point3D()
    abstractIntersection = getIntersectionWithWindow(camera, point)
    yComparisonValue = copy.deepcopy(camera.window.getPoints()[0].getZVal())
    yComparisonPoint = Point3D()
    yComparisonPoint.setValues(copy.deepcopy(camera.window.getPoints()[0].getValues()))
    yComparisonPoint.setZValue(yComparisonValue)
    xComparisonPoint = copy.deepcopy(camera.window.getPoints()[0]) ## Here somewhere
    xComparisonPoint.setZValue(point.getZVal())
    yDistance = yComparisonValue - point.getZVal()
    xDistance = get3dDistance(xComparisonPoint, abstractIntersection)
    return (xDistance, yDistance)

def renderPlane(c, camera, object):
    points = object.getPoints()
    polygonVertices = []
    for i in range(len(points)):
        polygonVertices.append(translateToCanvas(points[i], camera))
    polygonVertices.append(translateToCanvas(points[0], camera))
    c.create_polygon(polygonVertices, fill = 'green', outline = 'black')

renderPlane(c, viewport, testPlane)
