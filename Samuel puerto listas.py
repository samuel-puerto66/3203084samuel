# Crear una lista con los números del 1 al 10
numeros = list(range(1, 11))
print("Lista inicial:", numeros)

# Añadir el número 11 al final de la lista
numeros.append(11)
print("Después de añadir 11:", numeros)

# Ordenar la lista de menor a mayor
numeros.sort()
print("Lista ordenada:", numeros)

# Eliminar el primer número de la lista
numeros.pop(0)
print("Después de eliminar el primer número:", numeros)
