print("Ingresa tu edad: ")
edad=int(input())

if edad < 12:
    tarifa=50
elif edad <= 17:
    tarifa=80
else:
    tarifa=120
print(f"El costo de entrada es: ${tarifa}")
