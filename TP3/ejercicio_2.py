def matriz_secuencial(n):

  matriz = [[0 for _ in range(n)] for _ in range(n)]
  i = 0
  for fila in matriz:
    for columna in fila:
      if i % 2 == 0:
        fila[columna] = i
      else:
        fila[columna] = 0
      i += 1
  print(matriz)

matriz_secuencial(4)