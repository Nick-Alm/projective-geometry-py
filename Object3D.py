########################################################################
# 3d object consisting of number of interconnected planes
# plane points defined as (x,y,z) where x and y are horizontal (ground-level)
# axes and z is height
########################################################################
class Point3D:
    values = [0.0, 0.0, 0.0]
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.values[0] = x
        self.values[1] = y
        self.values[2] = z
    def getValues(self):
        return self.values
    def getXVal(self):
        return self.values[0]
    def getYVal(self):
        return self.values[1]
    def getZVal(self):
        return self.values[2]
    def setValues(self, values):
        self.values = values
    def setXValue(self, value):
        self.setValues([value, self.values[1], self.values[2]])
    def setYValue(self, value):
        self.setValues([self.values[0], value, self.values[2]])
    def setZValue(self, value):
        self.setValues([self.values[0], self.values[1], value])


class Plane:
    points = [Point3D(),Point3D(),Point3D()]
    def __init__(self, points = [Point3D(),Point3D(),Point3D()]):
        self.points = points
    def getPoints(self):
        return self.points
    def getPointValues(self):
        valueList = []
        for i in range(len(self.points)):
            valueList.append(self.points[i].getValues)
        return valueList       
    def printPointValues(self):
        for i in range(len(self.getPoints())):
            print(self.getPoints()[i].getValues())     
    def setPoints(self, points):
        self.points = points
    def setPointsFromValues(self, values):
        pointList = []
        for i in range(len(values)):
            pointList.append(values[i])
        self.setPoints(pointList)
class Object3D:
    planes = [Plane()]
    def __init__(self, planes=[Plane()]):
        self.planes = planes
    def getPlanes(self):
        return self.planes
    def getPoints(self):
        pointList = []
        for i in range(len(self.planes)):
            for j in range(len(self.planes[i].getPoints())):
                pointList.append(self.planes[i].getPoints()[j])
        return pointList
    def getPointValues(self):
        valueList = []
        pointList = self.getPoints()
        for i in range(len(pointList)):
            valueList.append(pointList[i].getValues())
        return valueList