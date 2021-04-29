def suma(num1,num2):
	return num1+num2

def resta(num1,num2):
	return num1-num2

def multiplicacion(num1,num2):
	return num1*num2

def division(num1,num2):
	return num1/num2

op1=(int(input("Introduce el primer numero: ")))
op2=(int(input("Introduce el segundo numero: ")))
operacion=input("Introduce la operacion a realizar (suma, resta, multiplicacion, division: ")

if operacion =="suma":
	print(suma(op1,op2))

elif operacion =="resta" or operacion == "-":
	print(resta(op1,op2))

elif operacion == "multiplicacion":
	print(multiplicacion(op1,op2))

elif operacion == "division":
	print(division(op1,op2))

else:
	print("Operación no contemplada")