#estaciones del ano
mes = int(input("numero de mes (1-12): "))
match mes:
    case 1 | 2 | 12:
        estacion = "invierno"
    case 3 | 4 | 5:
        estacion = "primavera"
    case 6 | 7 | 8:
        estacion = "verano"
    case 9 | 10 | 11:
        estacion = "otoño"
    case _:
        estacion = "mes invalido"
print("estacion: ", estacion)