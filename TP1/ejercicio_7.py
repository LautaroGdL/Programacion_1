# def diassiguientes():
#     lista = []
#     for i in range(3):
#         fecha = int(input("Ingrese una fecha válida: "))
#         while fecha <= 0:
#             print("El número debe ser mayor a 0")
#             fecha = int(input("Ingrese una fecha válida: "))
#         lista.append(fecha)
    
#     print("Fechas ingresadas:", lista)
    
#     for i in range(len(lista)):
#         lista[i] += 1
    
#     return lista

# fecha_siguiente = diassiguientes()

# print("Fechas siguientes:", fecha_siguiente)

def sumardias():
    lista = []
    for i in range(3):
        fecha = int(input("Ingrese una fecha válida: "))
        while fecha <= 0:
            print("El número debe ser mayor a 0")
            fecha = int(input("Ingrese una fecha válida: "))
        lista.append(fecha)
    
    print("Fechas ingresadas:", lista)
    
    dias = int(input("Ingrese la cantidad de días a sumar: "))
    for i in range(len(lista)):
        # Asegurarse de que el número de días sea positivo
        if dias > 0:
            # Sumar los días directamente a la fecha
            lista[i] += dias
            # Verificar si el día se ha pasado de 31
            if lista[i] > 31:
                # Ajustar la fecha y el mes si es necesario
                mes_incremento = (lista[i] - 1) // 31
                lista[i] -= mes_incremento * 31
                lista[i - 1] += mes_incremento
    
    return lista
    

fecha_suma = sumardias()
print("Fecha:", fecha_suma)