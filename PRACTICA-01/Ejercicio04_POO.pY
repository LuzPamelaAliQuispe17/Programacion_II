import math

class Estadistica:

    def __init__(self, n):
        self.__n = n
        self.__datos = []

    def promedio(self):
        sum = 0
        for i in range(len(self.__datos)):
            sum += self.__datos[i]
        return sum / len(self.__datos)

    def desviacion(self):
        prom = self.promedio()
        sumCuadrado = 0
        for i in range(len(self.__datos)):
            sumCuadrado += (self.__datos[i] - prom) ** 2
        return math.sqrt(sumCuadrado / (len(self.__datos) - 1))

    def __str__(self):
        return "Estadistica[{}, {}]".format(
            self.promedio(), self.desviacion()
        )


class Main():

    e = Estadistica(10)

    for i in range(10):
        e._Estadistica__datos.append(float(input()))

    print("El promedio es {:.2f}".format(e.promedio()))
    print("La desviación estandar es {:.5f}".format(e.desviacion()))