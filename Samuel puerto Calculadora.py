def calculadora():
    print("CALCULADORA SIMPLE")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Operaciones disponibles: +, -, *, /")
    operacion = input("Seleccione una operación: ")

    try:
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            resultado = num1 / num2
        else:
            print("Operación no válida")
            return

        print(f"Resultado: {resultado:.2f}")

    except ZeroDivisionError:
        print("Error: división por cero")
    except ValueError:
        print("Error: entrada inválida")

calculadora()
