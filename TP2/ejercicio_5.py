import random
def Create_list(x):
    list=[]
    for i in range(x):
        y=(int(input(" Ingrese los valores deseados a la lista: ")))
        list.append(y)
    return list

def Verif_List(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
##probar luego con valores aleatorios##
def list_random(x):
    list1=[]
    for i in range(x):
        list1.append(random.randint(0,100))
    return list1
##main

N_cant_valores=(int(input(" Ingrese la cantidad de elementos que desea en su lista: ")))
list=Create_list(N_cant_valores)
list=Verif_List(list)
print(list)

print()
list1=list_random(N_cant_valores)
print(list1)
list1=Verif_List(list1)
print(list1)
