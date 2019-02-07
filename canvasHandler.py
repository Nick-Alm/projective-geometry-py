from projectiveFormulas import *
from Camera import Camera
from tkinter import *
from Object3D import *
import copy

width = 500.0
height = 500.0
c = Canvas(width = width, height = height, bg = 'white')
c.pack(expand=YES, fill = BOTH)
testVanishPoint = Point3D()
testVanishPoint.setYValue(10.0)
testFocalPoint = Point3D()
testFocalPoint.setYValue(100.0)
viewport = Camera()
viewport.setVanishPoint(testVanishPoint)
viewport.setWindowDistance(50.0)
viewport.setWindowSize([width, height])
viewport.setFocalPoint(testFocalPoint)

pointOne = Point3D(-20.0, 5.0, 20.0)
pointTwo = Point3D(20.0, 5.0, 20.0)
pointThree = Point3D(20.0, 5.0, -20.0)
pointFour = Point3D(-20.0, 5.0, -20.0)
testPlane = Plane()
testPlane.setPoints([pointOne, pointTwo, pointThree, pointFour])

pointFive = Point3D(-20.0, 40.0, 20.0)
pointSix = Point3D(-20.0, 5.0, 20.0)
pointSeven = Point3D(-20.0, 5.0, -20.0)
pointEight = Point3D(-20.0, 40.0, -20.0)
secondPlane = Plane()
secondPlane.setPoints([pointFive, pointSix, pointSeven, pointEight])

pointNine = Point3D(20.0, 40.0, 20.0)
pointTen = Point3D(20.0, 5.0, 20.0)
pointEleven = Point3D(20.0, 5.0, -20.0)
pointTwelve = Point3D(20.0, 40.0, -20.0)
thirdPlane = Plane()
thirdPlane.setPoints([pointNine, pointTen, pointEleven, pointTwelve])

pointThirteen = Point3D(-20.0, 40.0, 20.0)
pointFourteen = Point3D(20.0, 40.0, 20.0)
pointFifteen = Point3D(20.0, 40.0, -20.0)
pointSixteen = Point3D(-20.0, 40.0, -20.0)
fourthPlane = Plane()
fourthPlane.setPoints([pointThirteen, pointFourteen, pointFifteen, pointSixteen])

def translateToCanvas(point, camera):
    abstractIntersection = Point3D()
    abstractIntersection = getIntersectionWithWindow(camera, point)
    yComparisonValue = copy.deepcopy(camera.window.getPoints()[0].getZVal())
    yComparisonPoint = Point3D()
    yComparisonPoint.setValues(copy.deepcopy(camera.window.getPoints()[0].getValues()))
    yComparisonPoint.setZValue(yComparisonValue)
    xComparisonPoint = copy.deepcopy(camera.window.getPoints()[0])
    xComparisonPoint.setZValue(point.getZVal())
    yDistance = yComparisonValue - copy.deepcopy(abstractIntersection.getZVal())
    xDistance = get3dDistance(xComparisonPoint, abstractIntersection)
    return (xDistance, yDistance)

def renderPlane(c, camera, object):
    points = object.getPoints()
    polygonVertices = []
    for i in range(len(points)):
        polygonVertices.append(translateToCanvas(points[i], camera))
    polygonVertices.append(translateToCanvas(points[0], camera))
    c.create_polygon(polygonVertices,fill = 'green', stipple='gray50',  outline = 'black')


def testRotate(camera):
    for i in range(5):
        camera.rotateLeft()
testRotate(viewport)
testRotate(viewport)
testRotate(viewport)
testRotate(viewport)
testRotate(viewport)
testRotate(viewport)
testRotate(viewport)
renderPlane(c, viewport, testPlane)
renderPlane(c, viewport, secondPlane)
renderPlane(c, viewport, thirdPlane)
renderPlane(c, viewport, fourthPlane)
