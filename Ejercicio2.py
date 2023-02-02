"""
Escribir una función que calcule el área de un círculo y otra que
calcule el volumen de un cilindro usando la primera función.
"""
import math

def area_circulo(radio):
  return math.pi * radio**2

def volumen_cilindro(radio, altura):
  area = area_circulo(radio)
  return area * altura

radio = float(input("Radio: "))
altura = float(input("Altura: "))
print("El area del circulo es: ", area_circulo(radio))
print("El volumen del cilindro es: ", volumen_cilindro(radio, altura))