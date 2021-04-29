miLista=["Antonio", "Fede", "Marta", "Antonio"]

miLista.insert(2,"Flor")

miLista.append("Juan")

miLista.extend(["Sandra", "Ana", "Lucía"])

print(miLista[:])

print(miLista.index("Antonio"))

print("Antonio" in miLista)

miLista2=["María", 5, True, 78.35]

miLista2.append("Ana")

print(miLista2[:])

miLista2.pop()

print(miLista2[:])

miLista.remove("Sandra")

print(miLista[:])

miLista3=miLista+miLista2

print(miLista3[:])

miListaColores=["Azul","Rojo","Verde"] * 3

print(miListaColores[:])