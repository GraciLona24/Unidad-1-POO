print("Ingresa el primer numero: ")
numero1=float(input())
print("Ingresa el segundo numero: ")
numero2=float(input())
print("Ingresa el tercer numero: ")
numero3=float(input())

mayor=max(numero1,numero2, numero3)
menor=min(numero1, numero2, numero3)

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")