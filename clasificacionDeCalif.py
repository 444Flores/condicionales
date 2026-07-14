#clasificacion de calificaciones
#pedimos la calificacion al usuario
nota = float(input("Ingrese la calificacion: "))

#hacemos una serie de condicionales if anidados
#asi clasificamos la calificacion en letras
if nota >= 90:
    letra = "A"
elif nota >= 80:
        letra = "B"
elif nota >= 70:
            letra = "C"
elif nota >= 60:
                letra = "D"
else:
                    letra = "F"

#imprimimos el resiltado de la nota
print("la calificacion es: ", letra)