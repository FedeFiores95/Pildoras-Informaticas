def devuelveCiudades(*ciudades): # el * indica que va a recibir un numero indeterminado de elementos yq ue se guardan en forma de tupla
	for elemento in ciudades:
		for subElemento in elemento: #este bucle anidado nos permite acceder a los sub elementos
			yield subElemento #La sintaxis yield from elemento no ahorraria utilizar el bucle for anidado


ciudadesDevueltas=devuelveCiudades("Madrid", "Barcelona", "Buenos Aires", "Cordoba")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))