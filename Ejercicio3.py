""""
Escribir una función que convierta un número decimal en binario y
otra que convierta un número binario en decimal.
"""

def decimal_a_binario(decimal):
  binario = ""
  while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2
  return binario

def binario_a_decimal(binario):
  decimal = 0
  binario = str(binario)
  for i in range(len(binario)):
    decimal += int(binario[i]) * (2**(len(binario) - i - 1))
  return decimal

decimal = int(input("Ingrese un numero decimal: "))
print("El numero decimal a binario es: ", decimal_a_binario(decimal))
binario = int(input("Ingrese un numero binario: "))
print("El numero binario a decimal es: ", binario_a_decimal(binario))