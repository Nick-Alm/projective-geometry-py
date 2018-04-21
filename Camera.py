from Object3D import Point3D
from projectiveFormulas import *

class Camera():
    focalPoint = Point3D()
    vanishPoint = Point3D()
    viewField = 0.0
    windowSize = (500,300)
    windowDistance = 10.0
    cartesianAngle = 0.0
    def __init__(self, focalPoint = Point3D(), vanishPoint = Point3D(), windowSize = (500,300) , windowDistance = 10.0):
        self.focalPoint = focalPoint
        self.vanishPoint = vanishPoint
        self.windowSize = windowSize
        self.windowDistance = windowDistance
        vanishPoint.setYValue(100.0)
        self.setVanishPoint(vanishPoint)
        self.setViewField()
    def setViewField(self):
        formulaInstance = TwoPointsOperation(self.getFocalPoint(), self.getVanishPoint())
        newViewField = formulaInstance.getDirectDistance(self.getFocalPoint(), self.getVanishPoint())
        self.viewField = newViewField
    def setFocalPoint(self, point):
        self.focalPoint = point
    def setVanishPoint(self, point):
        self.vanishPoint = point
    def getFocalPoint(self):
        return self.focalPoint
    def getVanishPoint(self):
        return self.vanishPoint    
    def findWindowPoints(self):
        return [Point3D]
    def getCartesianAngle(self):
        return self.cartesianAngle
    def getWindowCenter(self):
        twoPointsOp = TwoPointsOperation(self.focalPoint, self.vanishPoint)
        pitch = twoPointsOp.getPitch(self.focalPoint, self.vanishPoint)
        yaw = twoPointsOp.getYaw(self.focalPoint, self.vanishPoint)
        zValue = self.getZValue(pitch, self.windowDistance)
        xValue = self.getXValue(yaw, self.windowDistance)
        yValue = self.getYValue(yaw, self.windowDistance)
        returnPoint3D = Point3D()
        returnPoint3D.setXValue(xValue)
        returnPoint3D.setYValue(yValue)
        returnPoint3D.setZValue(zValue)
        return returnPoint3D
    def getZValue(self, angle, distance):
        sine = math.sin(angle)
        value = (distance * sine) + self.focalPoint.getZVal()
        return value
    def getXValue(self, angle, distance):
        sine = math.sin(angle)
        value = (distance * sine) + self.focalPoint.getXVal()
        return value
    def getViewField(self):
        return self.viewField
    def getYValue(self, angle, distance):
        cosine = math.cos(angle)
        value = (distance * cosine) + self.focalPoint.getYVal()
        return value
    def changeCartesianAngle(self, angleChange):
        self.cartesianAngle += angleChange
    def rotateLeft(self): # rotate camera left by 1 degree
        degree = math.radians(-1.0)
        self.changeCartesianAngle(degree)
        newVanishPoint = Point3D()
        newVanishPoint.setXValue(self.viewField * math.sin(self.getCartesianAngle()))
        newVanishPoint.setYValue(self.viewField * math.cos(self.getCartesianAngle()))
        self.setVanishPoint(newVanishPoint)
    def rotateRight(self): # rotate camera right by 1 degree
        degree = math.radians(1.0)
        self.changeCartesianAngle(degree)
        newVanishPoint = Point3D()
        newVanishPoint.setXValue(self.viewField * math.sin(self.getCartesianAngle()))
        newVanishPoint.setYValue(self.viewField * math.cos(self.getCartesianAngle()))
        self.setVanishPoint(newVanishPoint)        