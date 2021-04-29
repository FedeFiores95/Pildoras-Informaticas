def generaPares(limite): #esto es una funcion clasica

	num=1

	miLista=[]

	while num<limite:

		miLista.append(num*2)

		num=num+1

	return miLista

print(generaPares(10))

def generaPares2(limite): #esto es un generador, cada vez que se llama a un generador, este crea un objeto y no lo crea si no es llamado

	num=1

	while num<limite:

		yield num*2

		num=num+1

devuelvePares=generaPares2(20) 

print(next(devuelvePares))

print(next(devuelvePares))

print(next(devuelvePares))

print(next(devuelvePares))

for i in devuelvePares:
	print(i)