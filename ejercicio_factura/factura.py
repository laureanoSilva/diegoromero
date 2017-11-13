'''
Created on 4 nov. 2017
@author: Diego
'''

def mostrarProductos(diccionario):
    for a in diccionario:
        print(a+"-> "+diccionario[a]["nombre"]+" - $"+str(diccionario[a]["precio"]))


def mostrarTicket(matriz):
    sumaTotalTicket = 0
    for a in range(0,len(matriz[0])):
        print(matriz[0][a]," - ",matriz[1][a]," - $",matriz[2][a])
        sumaTotalTicket = sumaTotalTicket + matriz[2][a]
    print("Total: ",sumaTotalTicket)


productos = {}
productos["A001"]={"nombre":"yerba","precio":75}
productos["A002"]={"nombre":"azucar","precio":25}
productos["A003"]={"nombre":"agua","precio":15}
productos["A004"]={"nombre":"pan","precio":35}

ticket = [[],[],[]]

#debug
termina = 'no'
while termina == 'no':
    mostrarProductos(productos)
    codigo = input("ingresar codigo de articulo")
    cantidad = input("ingresar cantidad de articulo")
    ticket[0].append(int(cantidad))
    ticket[1].append(productos[codigo]["nombre"])
    ticket[2].append(int(cantidad)*productos[codigo]["precio"])
    termina = input("termina? si/no")


mostrarTicket(ticket)
