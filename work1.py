#Elaborar un programa en Python que permita capturar una cantidad N de números 
#y permita determinar cuántos de estos números se encuentran en el rango de 10 – 
#20. 
datos = int(input('cantidad de numeros que desea ingresar:'))
import os
contador = 1
lista_num =[]
lista_num2 =[]
os.system('cls')
while (contador <= datos):
    os.system('cls')
    num = int(input('escriba un numero'))
    if num>=10 and num <= 20:
        lista_num.append(num)
    else:
        lista_num2.append(num)
    contador += 1               
    print(f'estos numeros estan dentro del rango: {lista_num}\n estos fueron los numeros que no estan en el rango: {lista_num2}')
    # no es necesario imprimir los que no estan en el rango pero lo hice para corroborar que almacena los que almacena correctamente
        
