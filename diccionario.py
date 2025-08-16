dic = {"n1": 1, "n2": 2, "n3": 3, "n4": 4, "n5": 5, "n6": 6, "n7": 7, "n8": 8, "n9": 9, "n10": 10}

print("Escoge 2 números entre el 1 y el 10")
print(dic["n1"])
print(dic["n2"])


num1 = int(input("Ingrese el primer número (1-10): "))
num2 = int(input("Ingrese el segundo número (1-10): "))


n1 = dic[f"n{num1}"]
n2 = dic[f"n{num2}"]


print("El resultado de la suma es:", n1 + n2)


print("El resultado de la resta es:", n1 - n2)


print("El resultado de la multiplicación es:", n1 * n2)


if n2 == 0:
    print("Error: No se puede dividir por cero.")
else:
    print("El resultado de la división es:", n1 / n2)