'''
Created on 4 nov. 2017
@author: Diego
'''

def mostrarProductos(matriz):
    for a in range(0,len(matriz[0])):
        print(str(a)+"-> "+matriz[0][a]+" - $"+str(matriz[1][a]))


def mostrarTicket(matriz):
    sumaTotalTicket = 0
    for a in range(0,len(matriz[0])):
        print(matriz[0][a]," - ",matriz[1][a]," - $",matriz[2][a])
        sumaTotalTicket = sumaTotalTicket + matriz[2][a]
    print("Total: ",sumaTotalTicket)       


productos = [["Yerba","Azucar","Leche","Pan"],[70,15,25,26]]
ticket = [[],[],[]] 

#debug
termina = 'no'
while termina == 'no':
    mostrarProductos(productos)
    codigo = input("ingresar codigo de articulo")
    cantidad = input("ingresar cantidad de articulo")
    ticket[0].append(int(cantidad))
    ticket[1].append(productos[0][int(codigo)])
    ticket[2].append(int(cantidad)*productos[1][int(codigo)])                                  
    termina = input("termina? si/no")

   
mostrarTicket(ticket)