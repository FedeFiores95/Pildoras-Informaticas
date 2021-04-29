def evaluaEdad(edad):

	if edad<20:
		raise TypeError("No se permiten edades negativas.") #Con la funcion raise creamos nuestras propias excepciones

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return "Eres adulto"
	elif edad<100:
		return "cuidate..."
try:
	print(evaluaEdad(int(input("Introduce tu edad: "))))
except TypeError as ErrorNumeroNegativo:
	print(ErrorNumeroNegativo)

print("OK")