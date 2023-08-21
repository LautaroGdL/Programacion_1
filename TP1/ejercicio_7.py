def diassiguientes():
    lista = []
    for i in range(3):
        fecha = int(input("Ingrese una fecha válida: "))
        while fecha <= 0:
            print("El número debe ser mayor a 0")
            fecha = int(input("Ingrese una fecha válida: "))
        lista.append(fecha)
    
    print("Fechas ingresadas:", lista)
    
    for i in range(len(lista)):
        lista[i] += 1
    
    return lista

fecha_siguiente = diassiguientes()

print("Fechas siguientes:", fecha_siguiente)

