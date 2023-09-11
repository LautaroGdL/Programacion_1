def es_capicua(palabra):
  """True si la palabra es capicúa, False de lo contrario."""

  palabra_invertida = palabra[::-1]
  return palabra == palabra_invertida


palabra = input("Ingrese una palabra: ")
print(es_capicua(palabra))
