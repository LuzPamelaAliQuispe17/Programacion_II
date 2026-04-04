from multimethod import multimethod
import math

class AlgebraVectorial:

    def __init__(self, ax, ay, az, bx, by, bz):
        self.__ax = ax
        self.__ay = ay
        self.__az = az
        self.__bx = bx
        self.__by = by
        self.__bz = bz

    def __str__(self):
        return "({}, {}, {},{}, {}, {})".format(
            self.__ax, self.__ay, self.__az,
            self.__bx, self.__by, self.__bz
        )

    @multimethod
    def perpendicular(self):
        sx = self.__ax + self.__bx
        sy = self.__ay + self.__by
        sz = self.__az + self.__bz

        rx = self.__ax - self.__bx
        ry = self.__ay - self.__by
        rz = self.__az - self.__bz

        mod1 = math.sqrt(sx*sx + sy*sy + sz*sz)
        mod2 = math.sqrt(rx*rx + ry*ry + rz*rz)

        return mod1 == mod2

    @multimethod
    def perpendicular(self, tipo: int):
        if tipo == 1:
            producto = self.__ax*self.__bx + self.__ay*self.__by + self.__az*self.__bz
            return producto == 0

    @multimethod
    def perpendicular(self, tipo: float):
        sx = self.__ax + self.__bx
        sy = self.__ay + self.__by
        sz = self.__az + self.__bz

        a = sx*sx + sy*sy + sz*sz
        b = (self.__ax*self.__ax + self.__ay*self.__ay + self.__az*self.__az) + (self.__bx*self.__bx + self.__by*self.__by + self.__bz*self.__bz)

        return a == b

    @multimethod
    def paralela(self):
        if self.__bx != 0:
            r = self.__ax / self.__bx
        elif self.__by != 0:
            r = self.__ay / self.__by
        else:
            r = self.__az / self.__bz

        return (self.__ax == r*self.__bx and self.__ay == r*self.__by and self.__az == r*self.__bz)

    @multimethod
    def paralela(self, tipo: int):
        cx = self.__ay*self.__bz - self.__az*self.__by
        cy = self.__az*self.__bx - self.__ax*self.__bz
        cz = self.__ax*self.__by - self.__ay*self.__bx

        return cx == 0 and cy == 0 and cz == 0

    def proyeccion(self):
        producto = self.__ax*self.__bx + self.__ay*self.__by + self.__az*self.__bz
        modb2 = self.__bx*self.__bx + self.__by*self.__by + self.__bz*self.__bz

        escalar = producto / modb2

        px = escalar * self.__bx
        py = escalar * self.__by
        pz = escalar * self.__bz

        return px, py, pz

    def componente(self):
        producto = self.__ax*self.__bx + self.__ay*self.__by + self.__az*self.__bz
        modb = math.sqrt(self.__bx*self.__bx + self.__by*self.__by + self.__bz*self.__bz)

        return producto / modb


class Main():
    av = AlgebraVectorial(1, 2, 3, 2, 4, 6)

    r1 = av.perpendicular()
    print(r1)

    r2 = av.perpendicular(1)
    print(r2)

    r3 = av.perpendicular(1.0)
    print(r3)

    r4 = av.paralela()
    print(r4)

    r5 = av.paralela(1)
    print(r5)

    r6 = av.proyeccion()
    print(r6)

    r7 = av.componente()
    print(r7)