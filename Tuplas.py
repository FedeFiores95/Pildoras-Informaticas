miTupla=("Fede", 25, 10, 1995) #las tuplas son listas que no se pueden modificar
miLista=list(miTupla) #convertir tupla en lista
print(miLista)

miLista2=["Flor", 6, 8, 1995]
miTupla2=tuple(miLista2) #convertir lista en tupla

print(miTupla2)

print("Fede" in miTupla) #existe en la tupla?

print("Fede" in miTupla2)

print(miLista2.count("Flor")) #cuenta cuantas veces se repite un elemento en una lista o tupla

print(len(miTupla)) #cantidad de elementos en una tupla o lista

tuplaUnitaria=("Fede",) #tupla con un unico elemento, imprescindible la coma ","

nombre, dia, mes, anio=miTupla #desempaquetado de tupla

print(nombre)
