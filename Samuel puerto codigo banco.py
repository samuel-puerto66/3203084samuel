from decimal import Decimal, getcontext

def conversor_monedas():
    getcontext().prec = 10
    tasas = {
        "USD": Decimal("1.0"),
        "EUR": Decimal("0.85"),
        "COP": Decimal("3900.0"),
        "MXN": Decimal("17.0")
    }

    print("CONVERSOR DE MONEDAS")
    print("Monedas disponibles:", ", ".join(tasas.keys()))
    
    try:
        cantidad = Decimal(input("Ingrese la cantidad: "))
        moneda_origen = input("Moneda de origen: ").upper()
        moneda_destino = input("Moneda destino: ").upper()

        if moneda_origen not in tasas or moneda_destino not in tasas:
            print("Error: Moneda no disponible.")
            return

        cantidad_usd = cantidad / tasas[moneda_origen]
        resultado = cantidad_usd * tasas[moneda_destino]

        print(f"{cantidad} {moneda_origen} = {resultado:.2f} {moneda_destino}")
    except:
        print("Error: Ingrese datos válidos.")

conversor_monedas()
