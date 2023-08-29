def esta_ordenada_ascendente(lista):
    for i in range(1, len(lista)):
        if lista[i] < lista[i - 1]:
            return False
    return True

# Función para verificar el comportamiento de la función
def verificar_funcion():
    lista_1 = [1, 2, 3, 4, 5]
    lista_2 = [5, 4, 3, 2, 1]
    lista_3 = [1, 3, 2, 4, 5]

    print("Lista 1:", esta_ordenada_ascendente(lista_1))  # Debería imprimir True
    print("Lista 2:", esta_ordenada_ascendente(lista_2))  # Debería imprimir False
    print("Lista 3:", esta_ordenada_ascendente(lista_3))  # Debería imprimir False

verificar_funcion()
