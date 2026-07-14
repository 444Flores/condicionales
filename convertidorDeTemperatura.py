#convertidor de temperatura
celcius = float(input("temperatura en grados Celsius: "))
print("1. farenheit\n2. kelvin\n")
opcion = int(input("elige una opcion: "))
match opcion:
    case 1:
        resultado = (celcius * 9/5) + 32
        unidad = "°F"
    case 2:
        resultado = celcius + 273.15
        unidad = "K"
    case _:
        resultado = None
        print("opcion invalida")
if resultado is not None:
    print("Convertido: ", resultado, unidad)