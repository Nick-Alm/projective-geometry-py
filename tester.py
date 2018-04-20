from Object3D import *
from projectiveFormulas import TwoPointsOperation
from Camera import Camera

squarePoints = [[-10,10,0],[10,10,0],[10,-10,0],[-10,-10,0]]

point1 = Point3D()
point2 = Point3D()
point1.setXValue(1.0)
point1.setZValue(1.0)
point1.setYValue(1.0)
viewport = Camera()

square = Object3D()

print(square.getPointValues())
formulaInstance = TwoPointsOperation(point1, point2)
print(point1.getValues())
print(point2.getValues())
print(formulaInstance.getYDistance(point1,point2))
print(formulaInstance.getDirectDistance(point1,point2))
print(formulaInstance.getPitch(point1, point2))
print(formulaInstance.getYaw(point1,point2))
print(viewport.getWindowCenter().getValues())