class Coche():
	
	def __init__(self):
	
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 ## para encapsular una variable se le incluyen dos guiones bajos
		self.__enMarcha=False

	def arrancar(self,arrancamos):
		self.__enMarcha=arrancamos

		if (self.__enMarcha):
			chequeo =self.__chequeo_interno()
		if(self.__enMarcha and chequeo):
			return "El coche está en marcha"
		if(self.__enMarcha and chequeo==False):
			return "No se puede arrancar"
		else:
			return "El coche esta parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, "cms. y un largo de ",
			self.__largoChasis,"cms.")

	def __chequeo_interno(self):
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if (self.gasolina == "ok" and self.aceite=="ok" and self.puertas == "cerradas"):
			return True

		else:
			return False

miCoche=Coche()

print(miCoche.arrancar(True))
print(miCoche.estado())

print("-------Segundo Objeto-----------")

miCoche2=Coche()

print(miCoche2.arrancar(False))
print(miCoche2.estado())

print("OK")