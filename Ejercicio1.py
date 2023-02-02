""""
Escribir una función que calcule el total de una factura tras aplicarle
el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
IVA a aplicar, y devolver el total de la factura. Si se invoca la función
sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""
def calcularIva(cantidad, iva):
    return cantidad + (cantidad * iva / 100)

cantidad = float(input("Ingrese la cantidad: "))
#Puede recibir un valor vacio
iva = (input("Ingrese el iva: "))
if iva == "":
    iva = 21
    print("No se ha ingresado el iva, se aplicara el iva por defecto (21%)")
else:
    iva = float(iva)

print("El total es: ",calcularIva(cantidad, iva))

