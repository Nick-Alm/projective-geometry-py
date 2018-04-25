################################################################################
# Projective formulas
#
################################################################################
from Object3D import Point3D
import math

def getIntersectionWithWindow(camera, pointInSpace):
    points = camera.window.getPoints()
    normalVector = getNormalVector(camera)
    constantD = (points[0].getXVal() * normalVector[0]) + (points[0].getYVal() * normalVector[1]) + (points[0].getZVal() * normalVector[2])
    topOfT = (constantD - (normalVector[0] * camera.focalPoint.getXVal()) - (normalVector[1] * camera.focalPoint.getYVal()) - (normalVector[2] * camera.focalPoint.getZVal()))
    bottomOfT = ((normalVector[0] * pointInSpace.getXVal()) - (normalVector[0] * camera.focalPoint.getXVal()) + (normalVector[1] * pointInSpace.getYVal()) - (normalVector[1] * camera.focalPoint.getYVal()) + (normalVector[2] * pointInSpace.getZVal()) - (normalVector[2] * camera.focalPoint.getZVal()))
    t = topOfT / bottomOfT
    intersectingPoint = Point3D()
    intersectingPoint.setXValue(camera.focalPoint.getXVal() + (t * (pointInSpace.getXVal() - camera.focalPoint.getXVal())))
    intersectingPoint.setYValue(camera.focalPoint.getYVal() + (t * (pointInSpace.getYVal() - camera.focalPoint.getYVal())))
    intersectingPoint.setZValue(camera.focalPoint.getZVal() + (t * (pointInSpace.getZVal() - camera.focalPoint.getZVal())))
    return intersectingPoint
def getTwoVectors(camera):
    points = camera.window.getPoints()
    upperLeft = points[0]
    upperRight = points[1]
    lowerLeft = points[2]
    lowerRight = points[3]
    vectorOne = [upperRight.getXVal() - lowerLeft.getXVal(), upperRight.getYVal() - lowerLeft.getYVal(), upperRight.getZVal() - lowerLeft.getZVal()]
    vectorTwo = [upperLeft.getXVal() - lowerRight.getXVal(), upperLeft.getYVal() - lowerRight.getYVal(), upperLeft.getZVal() - lowerRight.getZVal()]
    return [vectorOne, vectorTwo]
def getNormalVector(camera):
    vectors = getTwoVectors(camera)
    vectorOne = vectors[0]
    vectorTwo = vectors[1]
    normalVectorX = (vectorOne[1] * vectorTwo[2]) - (vectorOne[2] * vectorTwo[1])
    normalVectorY = -((vectorOne[0] * vectorTwo[2]) - (vectorOne[2] * vectorTwo[0]))
    normalVectorZ = (vectorOne[0] * vectorTwo[1]) - (vectorOne[1] * vectorTwo[0])
    normalVector = [normalVectorX, normalVectorY, normalVectorZ]
    return normalVector
def get3dDistance(pointOne, pointTwo):
    x1 = pointOne.getXVal()
    x2 = pointTwo.getXVal()
    y1 = pointOne.getYVal()
    y2 = pointTwo.getYVal()
    z1 = pointOne.getZVal()
    z2 = pointTwo.getZVal()
    distance = math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1))+((z2-z1)*(z2-z1)))
    return distance
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
    def getYaw(self, pointOne, pointTwo): # This will need to be fixed to accomodate negative angles    
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
        if(sideOne==0):
            return 1.0
        elif(sideTwo==0):
            return 0.0
        cosine = (math.pow(sideOne,2) + math.pow(sideTwo,2) - math.pow(oppositeSide, 2)) / (2 * sideOne * sideTwo)
        return cosine
