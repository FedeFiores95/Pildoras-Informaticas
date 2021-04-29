def divide():

	while True:
		try:
			op1=float(input("Introduce el primer número: "))

			op2=float(input("Introduce el segundo número: "))

			print("La división es: " + str(op1/op2))

			break;

		except ValueError:

			print("Los valores introducidos no son correctos. Intentalo de nuevo.")

		except	ZeroDivisionError:

			print("No se puede dividir entre 0. Intentalo de nuevo.")

		finally:

			print("OK")

divide()