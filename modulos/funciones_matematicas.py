def suma(num1,num2):
	return num1+num2

def resta(num1,num2):
	return num1-num2

def multiplicar(num1,num2):
	return num1*num2

def dividir(num1,num2):
	try:
		return num1/num2
								#El bloque try except sirve para que se siga ejecutando el programa a pesar de que se produzca un error
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "Operación errónea"

while True:
	try:

		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))
		break;

	except ValueError:
		print("Los valores no son correctos. Intentalo de nuevo.")

operacion=input("Introduce la operacion a realizar (suma, resta, multiplicar, dividir: ")

if operacion =="suma" or operacion =="+":
	print(suma(op1,op2))

elif operacion =="resta" or operacion =="-":
	print(resta(op1,op2))

elif operacion == "multiplicar" or operacion =="*":
	print(multiplicar(op1,op2))

elif operacion == "dividir" or operacion =="/":
	print(dividir(op1,op2))

else:
	print("Operación no contemplada")

print("Final de ejecución")