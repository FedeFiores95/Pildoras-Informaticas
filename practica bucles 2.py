for i in ["Federico","Fiores",4]:
	print("Hola", end = " ") #la instruccion end le indica al programa que entre cada ejecucion del blucle haga algo en este caso imprime un espacio

for i in "Federico": # en el caso de utilizar un string en lugar de una lista el bucle se ejecuta por cada caracter del string
	print(i, end=" ")

email=False
miEmail=input("Introduce tu direccion de email: ")

for i in miEmail:
	
	if(i=="@"):

		email=True

if email == True:
	print("Email es correcto")
else:
	print("El email es incorrecto")		

contador=0

for i in miEmail:

	if(i=="@" or i=="."):

		contador=contador+1

print(contador)

for i in range(5): #el range crea una lista con la cantidad de elementos que se le asigne que van desde el 0
	print(i)