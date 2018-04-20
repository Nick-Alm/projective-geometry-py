########################################################################
# 3d object consisting of number of interconnected planes
# plane points defined as (x,y,z) where x and y are horizontal (ground-level)
# axes and z is height
########################################################################
class Point3D:
    values = [0,0,0]
    def __init__(self, values = [0,0,0]):
        self.values = values
    def getValues():
        return this.values

class Plane:
    points = [Point3D,Point3D,Point3D]
    def __init__(self, points = [Point3D(),Point3D(),Point3D()]):
        self.points = points
    def getPoints():
        return this.points
    
class Object3D:
    planes = [Plane()]
    def __init__(self, planes=[Plane()]):
        self.planes = planes
    def getPlanes():
        return this.planes
