edad=int(input("Introduzca su edad: "))

if 0<edad<100:
	print("Edad es correcta")
	if 30<edad<50:
		print("Mediana edad")
else:
	print("Edad es incorrecta")

salario_presidente=int(input("Introduzca salario del presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduzca salario del director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Introduzca salario del jede de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduzca salario del administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo esta fallando")