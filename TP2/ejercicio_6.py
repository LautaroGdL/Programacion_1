def normalizar_lista(lista):
    suma_total = sum(lista)
    lista_normalizada = [num / suma_total for num in lista]
    return lista_normalizada

numeros = []
num = 0
while num != -1:
    num = int(input("Ingrese números a la lista (-1 para terminar): "))
    if num != -1:
        numeros.append(num)

numeros_normalizados = normalizar_lista(numeros)
print(numeros_normalizados)
