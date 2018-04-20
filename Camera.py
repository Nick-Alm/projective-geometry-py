from Object3D import Point3D
from projectiveFormulas import *

class Camera():
    focalPoint = Point3D()
    vanishPoint = Point3D()
    windowSize = (500,300)
    windowDistance = 100.0
    def __init__(self, focalPoint, vanishPoint, windowSize, windowDistance):
        self.focalPoint = focalPoint
        self.vanishPoint = vanishPoint
        self.windowSize = windowSize
        self.windowDistance = windowDistance
    
    def findWindowPoints(self):
        return 0