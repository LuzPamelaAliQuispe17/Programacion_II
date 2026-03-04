import math

def leeVector(A, n):
    for i in range(n):
        A[i] = float(input())

def promedio(lista):
    sum = 0
    for i in range(len(lista)):
        sum += lista[i]
    return sum / len(lista)

def desviacion(lista):
    prom = promedio(lista)
    sumCuadrado = 0
    for i in range(len(lista)):
        sumCuadrado += (lista[i] - prom) ** 2
    return math.sqrt(sumCuadrado / (len(lista) - 1))


A = [0] * 10
leeVector(A, 10)

prom = promedio(A)
desv = desviacion(A)

print("El promedio es {:.2f}".format(prom))
print("La desviación estandar es {:.5f}".format(desv))