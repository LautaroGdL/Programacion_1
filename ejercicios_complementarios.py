##Ejercicio 1
def encuentra_numeros():
    numeros_encontrados = []

    for numero in range(100,1000):
        if numero % 2 == 1 and numero % 3 == 1 and numero % 4 == 1 and numero % 5 == 1 and numero % 6 == 1 and numero % 7 == 1:
            numeros_encontrados.append(numero)
                                
    return numeros_encontrados

numeros = encuentra_numeros()
print(numeros)

##Ejercicio 2
n = int(input("Ingrese un número entero: "))
while n>10:
    # Descomponer número
    suma = 0
    while n!=0:
        suma = suma + n % 10
        n //= 10
    n = suma
print("El crápulo del número ingresado es", n)