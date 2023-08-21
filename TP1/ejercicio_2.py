def ingresar_fecha():
    fecha = 0
    lista=[]
    for i in range(3):
        fecha=int(input("Ingrese una fecha valida: "))
        if fecha > 0:
            lista.append(fecha)
        else:
            print("El numero debe ser mayor a 0")
    print(lista)
    return lista

def validar_fecha(lista):
    fecha_valida = True
    if lista[0] > 31:
        fecha_valida = False
    elif lista[1] > 12:
        fecha_valida = False
    elif lista[2] < 0:
        fecha_valida = False

    if fecha_valida == True:
        print("La fecha es valida")
    else: 
        print("La fecha no es valida")



resultado_fecha = validar_fecha(ingresar_fecha())