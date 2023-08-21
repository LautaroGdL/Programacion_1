def viajes_tren():
    tarifa = 70
    viajes = int(input("Ingrese la cantidad de viajes: "))
    if viajes >=1 and viajes <=20:
        total= viajes*tarifa
    if viajes >=21 and viajes <=30:
        total= viajes*tarifa*0.8
    if viajes >=31 and viajes <=40:
        total= viajes*tarifa*0.7
    elif viajes > 40:
        total= viajes*tarifa*0.6
    return total

print("El total gastado en el mes de viajes es:","$",viajes_tren())
