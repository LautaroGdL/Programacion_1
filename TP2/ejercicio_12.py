# Función para ingresar los números de socios
def ingresar_socios():
  socios = []
  while True:
    numero_socio = input("Ingrese el número de socio (0 para terminar): ")
    if numero_socio == "0":
      break
    if len(numero_socio) != 5:
      print("El número de socio debe tener 5 dígitos.")
      continue
    socios.append(numero_socio)
  return socios

# Función para contar las visitas de cada socio
def contar_visitas(socios):
  visitas = [0] * len(socios)
  for i in range(len(socios)):
    for j in range(i + 1, len(socios)):
      if socios[i] == socios[j]:
        visitas[i] += 1
        break
  return visitas

# Función para eliminar las visitas de un socio
def eliminar_visitas(socios, numero_socio):
  for i in range(len(socios)):
    if socios[i] == numero_socio:
      socios[i] = "Eliminado"
      break
  return socios

# Función para mostrar los registros de entrada al club
def mostrar_registros(socios):
  for numero_socio in socios:
    if numero_socio != "Eliminado":
      print(f"Número de socio: {numero_socio}")
      print(f"Visitas: {visitas[socios.index(numero_socio)]}")

# Programa principal
socios = ingresar_socios()
visitas = contar_visitas(socios)

# Solicitamos el número de socio que se dio de baja
numero_socio_baja = input("Ingrese el número de socio que se dio de baja: ")

# Eliminamos las visitas del socio
socios = eliminar_visitas(socios, numero_socio_baja)

# Mostramos los registros de entrada al club antes y después de eliminar el socio
print("Registros de entrada al club antes de eliminar el socio:")
mostrar_registros(socios)

# Mostramos los registros de entrada al club después de eliminar el socio:
mostrar_registros(socios)

# Informamos cuántos ingresos se eliminaron
print(f"Se eliminaron {visitas[socios.index(numero_socio_baja)] - 1} ingresos del socio {numero_socio_baja}")
