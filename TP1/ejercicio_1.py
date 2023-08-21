def ingresar_numero():
    numero = 0
    lista=[]
    while len(lista) < 3:
        numero=int(input("Ingrese un numero: "))
        if numero > 0:
            lista.append(numero)
        else:
            print("El numero debe ser mayor a 0")
    print(lista)
    return lista


def encontrar_mayor_estricto(lista):
    mayor_estricto = float('-inf')  # Inicializamos con un valor muy pequeño
    for numero in lista:
        if numero > mayor_estricto:
            mayor_estricto = numero
    
    if mayor_estricto == float('-inf'):
        return -1
    else:
        return mayor_estricto

resultado = encontrar_mayor_estricto(ingresar_numero())

print("El mayor valor estricto en la lista es:", resultado)


# positivo_mayor = max(ingresar_numero())

# print("El numero mayor estricto es: ",positivo_mayor)