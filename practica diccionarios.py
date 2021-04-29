miDiccionario={"Alemania":"Berlín","Francia":"París","Argentina":"Buenos Aires","España":"Madrid"} #	clave:valor

print(miDiccionario)

print(miDiccionario["Francia"])	#imprime valor de la clave

miDiccionario["Italia"]="Lisboa" #agregar elemento

print(miDiccionario)

miDiccionario["Italia"]="Roma" #modificar elemento

print(miDiccionario)

del	miDiccionario["Alemania"] #eliminar elemento

print(miDiccionario)

miTupla=("Brasil", "Portugal","Chile")

miDiccionario2={miTupla[0]:"Rio", miTupla[1]:"Lisboa", miTupla[2]:"Santiago"} #Crear a partir de una tupla o lista

print(miDiccionario2)

diccionarioJordan={"Número":23, "Apellido":"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Campeonatos":[1991,1992,1993,1996,1997,1998]} #crear una tupla DENTRO

print(diccionarioJordan["Equipo"])

print(miDiccionario.keys()) #Imprime las claves de un diccionario

print(diccionarioJordan.values()) #Imprime los valores de un diccionario

print(len(diccionarioJordan)) #imprime longitud dedl diccionario