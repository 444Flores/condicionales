#Brindar Info

consulta = input("ingrese el nombre del artista, pelicula o serie: ").lower()

match consulta:
    case "inception":
        info = "pelicula de ciencia ficcion dirigida por Christopher Nolan."
    case "beatles":
        info = "banda de rock britanica formada en Liverpool en 1960."
    case "rick and morty":
        info = "serie animada de comedia y ciencia ficcion."
    case "stranger things":
        info = "serie de ciencia ficcion y terror de Netflix."
    case "avengers":
        info = "pelicula de superhéroes del MCU."
    case "-":
        info = "no se encontro informacion sobre el artista, pelicula o serie."

print("Informacion: ", info)