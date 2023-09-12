def eliminar_subcadena_rebanadas(cadena, inicio, cantidad):

  return cadena[:inicio] + cadena[inicio + cantidad:]

cadena = "Hola, mundo!"

# Eliminar la subcadena "mundo" a partir de la posición 6.
resultado_rebanadas = eliminar_subcadena_rebanadas(cadena, 6, 5)
print(resultado_rebanadas)

def eliminar_subcadena_no_rebanadas(cadena, inicio, cantidad):
  nueva_cadena = ""
  for i in range(len(cadena)):
    if i < inicio or i >= inicio + cantidad:
      nueva_cadena += cadena[i]

  return nueva_cadena

resultado_no_rebanadas = eliminar_subcadena_no_rebanadas(cadena, 6, 5)
print(resultado_no_rebanadas)
