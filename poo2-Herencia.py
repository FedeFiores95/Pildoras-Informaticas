class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False


	def arrancar(self):
		
		self.enMarcha=True

	def acelerar(self):
		
		self.acelera=True

	def frenar(self):
		
		self.frena=True

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class VElectricos(Vehiculos):
	
	def __init__(self,marca,modelo):
		
		super().__init__(marca,modelo)
		self.autonomia=100

	def estado(self):

		super().estado()

		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

	def cargarEnergia(self):
		
		self.cargando=True
		

class Furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado=cargar

		if(self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"


class Moto (Vehiculos):
	hcaballito=""
	
	def caballito(self):
		self.hcaballito= "Voy haciendo el caballito"

	def estado(self):
		print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class bicicletaElectrica(VElectricos,Vehiculos): #En herencia multiple los argumentos del constructor se heredan de la clase que se menciona primero
	pass

miBici=bicicletaElectrica("Orbea","HC1030")

miBici.estado()

miMoto=Moto("Honda","CBR")

miMoto.caballito()

miMoto.estado()	

miFurgoneta=Furgoneta("Renault","Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))	