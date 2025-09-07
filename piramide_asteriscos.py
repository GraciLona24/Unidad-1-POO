print("Ingresa la altura de la piramide : ")
numero=int(input())

for i in range(1, numero + 1):
    espacios = ' ' * (numero - i)
    asteriscos = '*' * (2 * i - 1)
    print(espacios + asteriscos)
