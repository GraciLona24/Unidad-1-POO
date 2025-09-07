print("Ingresa una calificacion de 0-100: ")
calificacion=int(input())

if 0 <= calificacion <= 100:
    if calificacion >= 90:
        letra = "A"
    elif calificacion >= 80:
        letra = "B"
    elif calificacion >= 70:
        letra = "C"
    elif calificacion >= 60:
        letra = "D"
    else:
        letra = "F"
    print(f"Tu calificación en letra es: {letra}")
else:
    print("La calificación debe estar entre 0 y 100.")
