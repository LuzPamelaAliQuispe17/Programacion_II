import time
import random

class Cronometro:

    def __init__(self):
        self.__inicia = int(time.time()*1000)
        self.__finaliza = None

    def getInicia(self):
        return self.__inicia

    def getFinaliza(self):
        return self.__finaliza

    def inicia(self):
        self.__inicia = int(time.time()*1000)
        self.__finaliza = None

    def detener(self):
        self.__finaliza = int(time.time()*1000)

    def lapsoDeTiempo(self):
        if self.__finaliza is None:
            return None
        return self.__finaliza - self.__inicia


class Main:

    def burbuja(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista


    vect = []

    for i in range(100000):
        vect.append(random.randint(1,100000))

    cron = Cronometro()
    cron.inicia()
    burbuja(vect)
    cron.detener()

    print(cron.lapsoDeTiempo())