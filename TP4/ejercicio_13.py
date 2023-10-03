def numero_a_letras(numero):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

    if 0 <= numero < 10:
        return unidades[numero]
    elif 10 <= numero < 16:
        return especiales[numero - 10]
    elif 16 <= numero < 20:
        return "dieci" + unidades[numero - 10]
    elif 20 <= numero < 100:
        decena = numero // 10
        unidad = numero % 10
        if unidad == 0:
            return decenas[decena]
        else:
            return decenas[decena] + " y " + unidades[unidad]
    elif 100 <= numero < 1000:
        centena = numero // 100
        resto = numero % 100
        if resto == 0:
            return centenas[centena]
        else:
            return centenas[centena] + " " + numero_a_letras(resto)
    elif 1000 <= numero < 1000000:
        millar = numero // 1000
        resto = numero % 1000
        if resto == 0:
            return numero_a_letras(millar) + " mil"
        else:
            return numero_a_letras(millar) + " mil " + numero_a_letras(resto)
    elif 1000000 <= numero < 1000000000:
        millon = numero // 1000000
        resto = numero % 1000000
        if resto == 0:
            return numero_a_letras(millon) + " millones"
        else:
            return numero_a_letras(millon) + " millones " + numero_a_letras(resto)
    else:
        return "Número fuera de rango"

# Ejemplo de uso:
numero = int(input("Ingrese un número entre 0 y 1 billón: "))
if 0 <= numero <= 1000000000:
    resultado = numero_a_letras(numero)
    print(resultado)
else:
    print("Número fuera de rango")
