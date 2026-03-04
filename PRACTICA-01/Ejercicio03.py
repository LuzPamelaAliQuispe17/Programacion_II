import math

class EcuacionCuadratica:

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return self.__b**2 - 4*self.__a*self.__c

    def getRaiz1(self):
        return (-self.__b + math.sqrt(self.getDiscriminante())) / (2*self.__a)

    def getRaiz2(self):
        return (-self.__b - math.sqrt(self.getDiscriminante())) / (2*self.__a)

    def __str__(self):
        return "{},{},{}".format(self.__a, self.__b, self.__c)

class Main():
    a, b, c = map(float, input("Ingrese a, b, c: ").split())
    
    ecuacion = EcuacionCuadratica(a, b, c)
    
    d = ecuacion.getDiscriminante()
    
    if d > 0:
        print("La ecuación tiene dos raíces", ecuacion.getRaiz1(), "y", ecuacion.getRaiz2())
    elif d == 0:
        print("La ecuación tiene una raíz", ecuacion.getRaiz1())
    else:
        print("La ecuación no tiene raíces reales")