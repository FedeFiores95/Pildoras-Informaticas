print("Programa de becas año 2021")

distancia = int(input("Introduzca la distancia en kilometros desde su hogar al instituto: "))
print(distancia)

cant_hermanos = int(input("¿Cuál es la cantidad de hermanos que estudian en el instituto?: "))
print(cant_hermanos)

salario = int(input("Introduzca el salario familiar total: "))
print(salario)

if distancia>40 and cant_hermanos>2 or salario<=20000:

	print("Usted cumple las condiciones para recibir una beca")

else:

	print("Usted no cumple las condiciones para recibir una beca")

#####################

print("Asignaturas opcionales año 2021")
print("Informática - Pruebas de software - Arduino")

opcion = input("Escribe la asignatura en la que quieras ingresar: ")

asignatura =opcion.lower() # .lower() toda la cadena se pasa a minusculas // .upper() mayusculas #

if asignatura in ("informática", "pruebas de software", "arduino"):

	print("Usted se inscribió en " + asignatura)

else: 

	print("La asignatura en la que intenta ingresar no esta contemplada") 