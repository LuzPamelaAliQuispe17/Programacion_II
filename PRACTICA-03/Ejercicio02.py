import random

class Juego():
  def __init__(self,numeroDeVidas):
    self._numeroDeVidas = numeroDeVidas
    self._record = 0

  def reiniciaPartida(self):
    self._vidasActuales = self._numeroDeVidas

  def actualizaRecord(self):
    if self._vidasActuales > self._record:
      self._record = self._vidasActuales
      print(f"Nuevo record: {self._record}")

  def quitaVida(self):
    self._vidasActuales = self._vidasActuales - 1
    if self._vidasActuales > 0:
      print(f"Vidas restantes: {self._vidasActuales}")
      return True
    else:
      print("Te quedaste sin vidas")
      return False

  def __str__(self):
    return f"Numero de Vidas: {self._numeroDeVidas},Record: {self._record}"


class JuegoAdivinaNumero(Juego):
  def __init__(self,numeroDeVidas):
    super().__init__(numeroDeVidas)
    self.__numeroAAdivinar = 0

  def __str__(self):
    return super().__str__() + f",Numero a adivinar: {self.__numeroAAdivinar}"

  def juega(self):
    self.reiniciaPartida()
    self.__numeroAAdivinar = random.randint(0,10)
    while True:
      n = int(input("Adivina el numero entre el 0 y 10: "))
      if self.validaNumero(n):
        if n == self.__numeroAAdivinar:
          print("Acertaste!!")
          self.actualizaRecord()
          break
        else:
          if self.quitaVida():
            if n < self.__numeroAAdivinar:
              print("El numero es mayor")
            else:
              print("El numero es menor")
          else:
            break
      
  def validaNumero(self,n):
    if n >= 0 and n <= 10:
      return True
    else:
      print("El numero debe estar entre 0 y 10")
      return False


class JuegoAdivinaPar(JuegoAdivinaNumero):
  def validaNumero(self,n):
    if super().validaNumero(n):
        if n%2 == 0:
            return True
        else:
            print("El numero debe ser PAR")
            return False
    else:
      return False


class JuegoAdivinaImpar(JuegoAdivinaNumero):
  def validaNumero(self, n):
    if super().validaNumero(n):
        if n%2 != 0:
            return True
        else:
            print("El numero debe ser IMPAR")            
            return False
    else:
      return False


class Aplicacion:
  def main():
    print("_______JUEGO ADIVINA NUMERO_______")
    juego1 = JuegoAdivinaNumero(3)
    juego1.juega()

    print("_______JUEGO ADIVINA PAR_______")
    juego2 = JuegoAdivinaPar(3)
    juego2.juega()

    print("_______JUEGO ADIVINA IMPAR_______")
    juego3 = JuegoAdivinaImpar(3)
    juego3.juega()


if __name__ == "__main__":
  Aplicacion.main()