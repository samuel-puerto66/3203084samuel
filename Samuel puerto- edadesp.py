Edad=int(input("Ingresa tu edad:"))
if Edad < 12:
    print("Eres un niño.")
if Edad >= 12 and Edad < 18:
    print("Eres un adolescente.")
elif Edad >= 18:
    print("Eres un adulto.")