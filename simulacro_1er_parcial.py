import random

 # Ejercicio 1
def repartir_cartas_españolas(num_jugadores):
  """
  Reparte las cartas de una baraja española entre un número de jugadores dado.

  Args:
    num_jugadores: El número de jugadores.

  Returns:
    Una matriz con las cartas repartidas, con una fila por jugador y tres columnas, una por cada palo.
  """

  # Generamos la baraja española
  palos = ["oros", "copas", "espadas", "bastos"]
  rangos = list(range(1, 13))
  baraja = []
  for palo in palos:
    for rango in rangos:
      baraja.append((palo, rango))

  # Mezclamos la baraja
  random.shuffle(baraja)

  # Repartimos las cartas
  cartas_repartidas = []
  for i in range(num_jugadores):
    cartas_jugador = []
    for j in range(3):
      cartas_jugador.append(baraja.pop())
    cartas_repartidas.append(cartas_jugador)

  # Devolvemos las cartas repartidas
  return cartas_repartidas


# Ejemplo de uso
cartas_repartidas = repartir_cartas_españolas(4)
print(cartas_repartidas)

# Ejercicio 2

def copias(hojas, copias):
  """
  Esta función hace copias de una cantidad de hojas especificada.

  Args:
    hojas: La cantidad de hojas que hay que copiar.
    copias: La cantidad de copias que hay que hacer.

  Returns:
    Una lista con las copias de las hojas.
  """

  # Creamos una lista con las hojas originales.
  hojas = list(range(1, hojas + 1))

  # Hacemos las copias intercaladas.
  copias_no_intercaladas = []
  for i in range(len(hojas)):
    for j in range(copias):
      copias_no_intercaladas.append(hojas[i])

  # Devolvemos la lista con las copias.
  return copias_no_intercaladas


copias_intercaladas = copias(3, 2)

print("Copias no intercaladas:", copias_intercaladas)

def copias(hojas, copias):
  """
  Esta función hace copias de una cantidad de hojas especificada.

  Args:
    hojas: La cantidad de hojas que hay que copiar.
    copias: La cantidad de copias que hay que hacer.

  Returns:
    Una lista con las copias de las hojas.
  """

  # Creamos una lista con las hojas originales.
  hojas = list(range(1, hojas + 1))

  # Hacemos las copias no intercaladas.
  copias_intercaladas = []
  for i in range(copias):
    for j in range(len(hojas)):
      copias_intercaladas.append(hojas[j])

  # Devolvemos la lista con las copias.
  return copias_intercaladas


copias_intercaladas = copias(3, 2)

print("Copias intercaladas:", copias_intercaladas)
