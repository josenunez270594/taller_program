#Elaborar un programa en Python que permita gestionar el inventario de un 
#supermercado el cual permite registrar compras (suman productos en el inventario), 
#ventas (restan al inventario de productos), el programa debe tener 2 opciones una 
#de compra y otra de ventas, el programa debe validar que no se vendan productos 
#que no tengan existencias es decir si tengo un producto tv y tiene 5 elementos 
#disponibles no permita vender ejemplo 10 porque no posee la cantidad disponible, 
#por otra parte se deben registrar los datos del producto código, nombre, existencias, 
#precio unitario.
inventario = []

while True:
    opcion = input("\nBienvenido al sistema de gestión de inventario. \n 1. Registrar compra \n 2. Registrar venta \n 3. Salir\n")

    if opcion == "1": 
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        existencias = int(input("Ingrese la cantidad de existencias: "))
        precio_unitario = int(input("Ingrese el precio unitario: "))
        producto = {"codigo": codigo, "nombre": nombre, "existencias": existencias, "precio_unitario": precio_unitario}
        inventario.append(producto)
        print("Compra registrada exitosamente")
    elif opcion == "2":  
        codigo = input("Ingrese el código del producto: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))

        producto_encontrado = False
        for producto in inventario:
            if producto["codigo"] == codigo:
                producto_encontrado = True
                if producto["existencias"] >= cantidad:
                    producto["existencias"] -= cantidad
                    print("Venta realizada exitosamente")
                else:
                    print("No hay suficientes existencias para realizar la venta")
                break
        if not producto_encontrado:
            print("El producto no está en el inventario")
    elif opcion == "3": 
        print("\nInventario:")
        for producto in inventario:
            print("Código:", producto["codigo"],"\nNombre:", producto["nombre"],"\nExistencias:", producto["existencias"],"\nPrecio unitario:", producto["precio_unitario"])
        break
    else:
        print("Syntaxis error, seleccione una opción válida")