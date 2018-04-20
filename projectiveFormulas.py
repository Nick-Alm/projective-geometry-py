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
        sideOneLength = self.getHorizontalDistance(pointOne, pointTwo)
        sideTwoLength = self.getDirectDistance(pointOne, pointTwo)
        cosine = self.getCosFromSides(oppositeSideLength, sideOneLength, sideTwoLength)
        pitch = math.acos(cosine)
        return pitch
    def calculateYaw(self, pointOne, pointTwo):
        return 0.0
    def getHorizontalDistance(self, pointOne, pointTwo):
        x1 = pointOne.getXVal()
        x2 = pointTwo.getXVal()
        y1 = pointOne.getYVal()
        y2 = pointTwo.getYVal()
        distance = float('%.4f'% math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))))
        return distance
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
        distance = float('%.4f'% math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))+((z2-z1)*(z2-z1))))
        return distance
    def getCosFromSides(self, oppositeSide, sideOne, sideTwo):
        cosine = (math.pow(sideOne,2) + math.pow(sideTwo,2) - math.pow(oppositeSide, 2)) / (2 * sideOne * sideTwo)
        return cosine