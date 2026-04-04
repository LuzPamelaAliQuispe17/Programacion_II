import math

class MiPunto:

    def __init__(self, x=None, y=None):
        if x is None and y is None:
            self.__x = 0
            self.__y = 0
        else:
            self.__x = x
            self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distancia(self, p, y=None):
        if y is None:
            return math.sqrt((p.__x - self.__x)**2 + (p.__y - self.__y)**2)
        else:
            return math.sqrt((p - self.__x)**2 + (y - self.__y)**2)

    def __str__(self):
        return "({},{})".format(self.__x, self.__y)

class Main():
    p1 = MiPunto()
    p2 = MiPunto(10,30.5)
    
    print("Punto 1:", p1)
    print("Punto 2:", p2)
    print("Distancia:", p1.distancia(p2))