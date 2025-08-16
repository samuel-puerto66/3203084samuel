nombre_cultivo = input("Ingrese el nombre del cultivo: ")
cantidad_plantas = int(input("Ingrese la cantidad de plantas: "))
temperatura_optima = float(input("Ingrese la temperatura óptima (°C): "))
requiere_riego = input("¿Requiere riego hoy? (sí/no): ").lower() == "sí"

print("Cultivo:", nombre_cultivo)
print("Plantas:", cantidad_plantas)
print("Temperatura óptima:", temperatura_optima, "°C")
print("Requiere riego hoy:", requiere_riego)
