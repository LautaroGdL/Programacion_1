def contar_animales(cant_total, cant_patas_total):
    # Definir las cantidades de patas por tipo de animal
    patas_2 = 2
    patas_4 = 4
    
    # Resolver el sistema de ecuaciones
    # cant_2 + cant_4 = cant_total
    # patas_2 * cant_2 + patas_4 * cant_4 = cant_patas_total
    cant_4 = (cant_patas_total - patas_2 * cant_total) / (patas_4 - patas_2)
    cant_2 = cant_total - cant_4
    
    return int(cant_2), int(cant_4)

# Datos proporcionados
cant_total = 35
cant_patas_total = 94

# Llamar a la función para obtener los resultados
cant_2, cant_4 = contar_animales(cant_total, cant_patas_total)

# Imprimir los resultados
print("Cantidad de animales con 2 patas:", cant_2)
print("Cantidad de animales con 4 patas:", cant_4)
