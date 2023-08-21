def diadelasemana(dia, mes, año):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((13 * mes - 1) // 5) + año2 + año2 // 4 + siglo // 4 - (2 * siglo)) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def imprimir_calendario(mes, año):
    nombres_dias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    dias_en_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        dias_en_mes[2] = 29
    
    primer_dia = diadelasemana(1, mes, año)
    
    print(f"Calendario para {mes}/{año}")
    print("Domingo   Lunes     Martes    Miércoles Jueves    Viernes   Sábado")
    
    dia_actual = 1
    while dia_actual <= dias_en_mes[mes]:
        semana = ""
        for _ in range(7):
            if dia_actual <= dias_en_mes[mes]:
                espacio = " " * (9 - len(str(dia_actual)))
                semana += f"{espacio}{dia_actual}"
                dia_actual += 1
            else:
                semana += "         "
        print(semana)

mes = int(input("Ingrese el mes (número): "))
año = int(input("Ingrese el año: "))

imprimir_calendario(mes, año)
