print("Ingresa un numero entero: ")
numero=int(input())

numero_invertido = str(abs(numero))[::-1]

if numero < 0:
    numero_invertido = '-' + numero_invertido

print(f"Número invertido: {numero_invertido}")
