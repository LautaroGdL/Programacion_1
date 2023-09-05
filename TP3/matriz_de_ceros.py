def matriz_de_ceros(n):
  """
  Crea una matriz de nxn con ceros.

  Argumentos:
    n: El tamaño de la matriz.

  Retorno:
    Una matriz de nxn con ceros.
  """

  matriz = []
  for i in range(n):
    fila = []
    for j in range(n):
      fila.append(0)
    matriz.append(fila)

  return matriz

matriz = matriz_de_ceros(4)

print(matriz)
