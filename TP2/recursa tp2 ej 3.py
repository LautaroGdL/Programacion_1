cantidad=int(input("ingrese la cantidad de elementos: "))

mi_lista=[]
for i in range(1,cantidad+1):
    mi_lista.append(i**2)


ultimos_10_valores = mi_lista[-10:]

for valor in ultimos_10_valores:
    print(valor)
    
