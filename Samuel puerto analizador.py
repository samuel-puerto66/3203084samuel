def analizar_texto():
    print("ANALIZADOR DE TEXTO")
    frase = input("Ingrese una frase: ")

    num_caracteres = len(frase)
    palabras = frase.split()
    num_palabras = len(palabras)
    mayusculas = frase.upper()
    minusculas = frase.lower()
    invertida = frase[::-1]

    buscar = input("¿Qué palabra deseas buscar?: ")
    ocurrencias = frase.count(buscar)

    reemplazar = input(f"¿Con qué palabra deseas reemplazar '{buscar}'?: ")
    nueva_frase = frase.replace(buscar, reemplazar)

    print("RESULTADOS:")
    print(f"Cantidad: {num_caracteres}")
    print(f"Palabras: {num_palabras}")
    print(f"En mayúsculas: {mayusculas}")
    print(f"En minúsculas: {minusculas}")
    print(f"Invertida: {invertida}")
    print(f"Ocurrencias de '{buscar}': {ocurrencias}")
    print(f"Frase con reemplazo: {nueva_frase}")

analizar_texto()
