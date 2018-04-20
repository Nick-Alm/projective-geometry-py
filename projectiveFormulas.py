################################################################################
# Projective formulas
#
################################################################################
from Object3D import Point3D
import math

class TwoPointsOperation():
    pointOne = Point3D()
    pointTwo = Point3D()
    def __init__(self, pointOne, pointTwo):
        self.pointOne = pointOne
        self.pointTwo = pointTwo
    def getPitch(self, pointOne, pointTwo):
        oppositeSideLength = self.getVerticalDistance(pointOne, pointTwo)
        sideOneLength = self.getYDistance(pointOne, pointTwo)
        sideTwoLength = self.getDirectDistance(pointOne, pointTwo)
        cosine = self.getCosFromSides(oppositeSideLength, sideOneLength, sideTwoLength)
        pitch = math.acos(cosine)
        return pitch
    def getYaw(self, pointOne, pointTwo):
        oppositeSideLength = self.getHorizontalXDistance(pointOne, pointTwo)
        sideOneLength = self.getHorizontalYDistance(pointOne, pointTwo)
        sideTwoLength = self.getDirectDistance(pointOne, pointTwo)
        cosine = self.getCosFromSides(oppositeSideLength, sideOneLength, sideTwoLength)
        pitch = math.acos(cosine)
        return pitch
    def getYDistance(self, pointOne, pointTwo):
        x1 = pointOne.getXVal()
        x2 = pointTwo.getXVal()
        y1 = pointOne.getYVal()
        y2 = pointTwo.getYVal()
        distance = math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
        return distance
    def getHorizontalXDistance(self, pointOne, pointTwo):
        x1 = pointOne.getXVal()
        x2 = pointTwo.getXVal()
        return x2-x1
    def getHorizontalYDistance(self, pointOne, pointTwo):
        y1 = pointOne.getYVal()
        y2 = pointTwo.getYVal()
        return y2-y1
    def getVerticalDistance(self, pointOne, pointTwo):
        z1 = pointOne.getZVal()
        z2 = pointTwo.getZVal()
        return z2-z1
    def getDirectDistance(self, pointOne, pointTwo):
        x1 = pointOne.getXVal()
        x2 = pointTwo.getXVal()
        y1 = pointOne.getYVal()
        y2 = pointTwo.getYVal()
        z1 = pointOne.getZVal()
        z2 = pointTwo.getZVal()
        distance = math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))+((z2-z1)*(z2-z1)))
        return distance
    def getCosFromSides(self, oppositeSide, sideOne, sideTwo):
        cosine = (math.pow(sideOne,2) + math.pow(sideTwo,2) - math.pow(oppositeSide, 2)) / (2 * sideOne * sideTwo)
        return cosine