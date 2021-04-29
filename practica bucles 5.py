nombre=input("introduce tu nombre: ")

contador=0

for i in nombre:

	if i ==" ":
		continue		#Ignora el resto del bucle y salta a la siguiente iteración
	contador +=1

print(contador)

 # la instruccion pass mantiene el codigo ejecutandose sin que el bucle se vea afectado
