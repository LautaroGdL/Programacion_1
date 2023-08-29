import random
def Create_list(x):
    list=[]
    for i in range(x):
        y=(int(input(" Ingrese los valores deseados a la lista: ")))
        list.append(y)
    return list
def Verif_List(list):
    for i in range(len (list)-1):
        if list[i]> list[i+1]:
            return False
        else:
            return True
##probar luego con valores aleatorios##
##main
N_cant_valores=(int(input(" Ingrese la cantidad de elementos: ")))
list=Create_list(N_cant_valores)
list=Verif_List(list)
print(list)