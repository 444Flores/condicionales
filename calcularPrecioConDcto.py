#calcular precio con descuento

#solicitamos el precio original al usuario
precio = float(input("precio original: "))

#segun el precio vamos a dar este descuento
if precio <= 100:
    descuento = 0
elif precio <= 200:
    descuento = 0.1
elif precio <= 500:
    descuento = 0.2
else:
    descuento = 0.25

#calculamos e imprimimos
precio_final = precio - (precio * descuento)
print("El precio con descuento es: ", precio_final)