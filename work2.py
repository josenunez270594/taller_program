#Elaborar un programa en Python el cual tiene los siguientes productos: 1. 
#Televisores y determinar cuantos de cada uno se han comprado, tener en cuenta 
#que el precio de los artículos debe estar establecidos de manera constante, el 
#sistema debe recibir todos los productos de manera infinita y al momento de 
#seleccionar la opción de “FACTURAR” debe mostrar el total de la suma de los 
#artículos, cuantos de cada uno se agregaron, el total a pagar. 
import os
campras = [8000,500,1000,1500,2000]
print('tienda la maquina, bienvenido')
nombre = input('escriba su nombre: ')
contacto = input('escriba su contacto: ')
dirreccion = input('escriba su dirreccion: ')
os.system('cls')
totalG,tablet,televisor,computador_de_escritorio,videobeam,portatil = 0,0,0,0,0,0
while True:
    os.system('cls')
    optionStr = int(input('.......MENU DE OPCIONES........\n que compras deseas hacer marca un numero para elegir una opción:\n 1) computador de escritorio \n 2) portatil \n 3) tablet \n 4) videobeam \n 5) televisor \n 6) facturar \n'))
    if  optionStr == 1:
        cantidad = int(input('cantidad:\n'))
        totalG += (cantidad*campras[optionStr-1])
        computador_de_escritorio = cantidad
    if  optionStr == 2:
        cantidad = int(input('cantidad:\n'))
        totalG += (cantidad*campras[optionStr-1])
        portatil = cantidad
    if  optionStr == 3:
        cantidad = int(input('cantidad:\n'))
        totalG += (cantidad*campras[optionStr-1])
        tablet = cantidad
    if  optionStr == 4:
        cantidad = int(input('cantidad:\n'))
        totalG += (cantidad*campras[optionStr-1])
        videobeam = cantidad
    if  optionStr == 5:
        cantidad = int(input('cantidad:\n'))
        totalG += (cantidad*campras[optionStr-1])
        televisor = cantidad
    if optionStr == 6:
        print (f' \n nombre:{nombre} \n contacto:{contacto} \n  dirección:{dirreccion}\n total a pagar es: {totalG}\n cantidad de computadores de escritorio: { computador_de_escritorio}\n cantidad de portatiles {portatil} \n cantidad de tablets {tablet} \n cantidad de televisores {televisor}')   
        break 
