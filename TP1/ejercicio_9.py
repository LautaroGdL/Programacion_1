import random

def calcular_reparto(n_camiones):
    carga_total = n_camiones * 0.5  # media tonelada
    naranjas_total = 0
    naranjas_jugo = 0
    
    for i in range(n_camiones):
        peso_camion = random.randint(150, 350)
        naranjas_camion = peso_camion * 2  # cada camión puede llevar 100 naranjas
        naranjas_total += naranjas_camion
        
        for i in range(naranjas_camion):
            peso_naranja = random.randint(200, 300)
            if peso_naranja > 300:
                naranjas_jugo += 1
    
    cajones = naranjas_total // 100
    naranjas_sobrantes = naranjas_total % 100
    
    return cajones, naranjas_jugo, naranjas_sobrantes

n_camiones = int(input("Ingrese la cantidad de camiones: "))
cajones, naranjas_jugo, naranjas_sobrantes = calcular_reparto(n_camiones)

print(f"Cajones a llenar: {cajones}")
print(f"Naranjas para jugo: {naranjas_jugo}")
print(f"Naranjas sobrantes para el próximo reparto: {naranjas_sobrantes}")
