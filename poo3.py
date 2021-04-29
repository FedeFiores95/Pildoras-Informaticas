class Persona():

	def __init__(self, nombre, edad, nacionalidad):

		self.nombre=nombre
		self.edad=edad
		self.nacionalidad=nacionalidad

	def descripcion(self):

		print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nNacionalidad: ", self.nacionalidad)

class Empleado(Persona):
	
	def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, nacEmpleado):

		super().__init__(nombreEmpleado, edadEmpleado, nacEmpleado)

		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):
		
		super().descripcion()

		print("Salario: ",self.salario, "\nAntigüedad:",self.antiguedad)


Federico=Empleado(1500, 15, "Federico", 25,"Argentino")

print(isinstance(Federico, Persona))

Federico.descripcion()



