import math

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar, self.z * escalar)

    def ObtenerLongitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def ObtenerNormal(self):
        longitud = self.ObtenerLongitud()
        if longitud == 0:
            return Vector(0,0,0)
        return Vector(self.x / longitud, self.y / longitud, self.z / longitud)

    def ProductoEscalar(self, otro):
        return (self.x * otro.x) + (self.y * otro.y) + (self.z * otro.z)

    def ProductoVectorial(self, otro):
        nueva_x = self.y * otro.z - self.z * otro.y
        nueva_y = self.z * otro.x - self.x * otro.z
        nueva_z = self.x * otro.y - self.y * otro.x
        return Vector(nueva_x, nueva_y, nueva_z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

class Main():
    a = Vector(3, -2, 5)
    b = Vector(1, 4, -1)
    
    print(f"Vector a: {a}")
    print(f"Vector b: {b}")
    
    suma = a + b
    escalar = a * 3
    largo = a.ObtenerLongitud()
    unitario = a.ObtenerNormal()
    p_escalar = a.ProductoEscalar(b)
    p_vectorial = a.ProductoVectorial(b)
    
    print("Resultados:")
    print(f"Suma a + b: {suma}")
    print(f"Escalar a * 3: {escalar}")
    print(f"Longitud |a|: {largo:.2f}")
    print(f"Vector Normal de a: {unitario}")
    print(f"Producto Escalar a · b: {p_escalar}")
    print(f"Producto Vectorial a x b: {p_vectorial}")