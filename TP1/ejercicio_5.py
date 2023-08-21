def asterisco_completa():
    n = int(input("Ingrese cantidad de filas: "))

    # Crea una fila con asteriscos
    for i in range(n):
        fila = '*' * int(n)  # Crea una fila con asteriscos
        print(fila)

completa = asterisco_completa()

def asterisco_incompleta():
    n = int(input("Ingrese cantidad de filas: "))

    # Crea una fila con asteriscos
    for i in range(n):
        fila = '*' * (i + 1)  # Crea una fila con i+1 asteriscos
        print(fila)

incompleta = asterisco_incompleta()