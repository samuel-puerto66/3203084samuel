
dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")


print("Tercer día de la semana:", dias_semana[2])


try:
    dias_semana[1] = "Martesito"
except TypeError as error:
    print("Error al modificar la tupla:", error)
