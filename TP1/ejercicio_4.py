def vuelto_billetes():
    billetes_denominaciones = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    billetes_entregados = {}  # Diccionario para almacenar las cantidades de billetes entregados
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero para pagar: "))
    
    if dinero_recibido < total_compra:
        return "El dinero recibido es insuficiente para la compra."
    
    vuelto = dinero_recibido - total_compra

    for denominacion in billetes_denominaciones:
        cantidad_billetes = vuelto // denominacion
        if cantidad_billetes > 0:
            billetes_entregados[denominacion] = cantidad_billetes
            vuelto -= cantidad_billetes * denominacion
            
    return billetes_entregados

vuelto = vuelto_billetes()

if isinstance(vuelto, str):
    print(vuelto)
else:
    print("Vuelto a entregar:")
    for denominacion, cantidad in vuelto.items():
        print(f"{cantidad} billete(s) de {denominacion}")

    