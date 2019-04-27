from almacen import Almacen


def opciones():
    print("Bienvenido a almacenes Alex, Digita el numero asociado a las operaciones qupe deseas hacer")
    print("1 para listar todos los productos ")
    print("2 para buscar por id un producto")
    print("3 para buscar y actualizar un producto")
    print("4 para insertar nuevo producto")
    print("5 para eliminar")

    print("0 para salir")

def guia_actualizacion():
    print("para actualizar ingresa el siguiente formato [id,nombre_nuevo,precio_nuevo,proveedor_nuevo,stock_nuevo]")
    print("donde")
    print("id: el id asociado al producto")
    print("nombre_nuevo: es el nombre nuevo si es que se cambia sino digita el actual")
    print("precio_nuevo: es el precio nuevo si es que se cambia sino digita el actual")
    print("proveedor_nuevo: es el proveedor nuevo si es que se cambia sino digita el actual")
    print("stock_nuevo: es la cantidad en stock nueva si es que se cambia sino digita la actual")

if __name__ == '__main__':
    almacen =Almacen("Almacenes Alex")
    opcion = 1

    while(opcion!=0):
        opciones()
        opcion = int(input("Ingresa el numero: "))
        #iterador=int(input('ingresa una opcion'))

        if opcion == 1:
            print("listado de productos \n")
            almacen.listar_productos_en_stock()
            print("\n")
        elif opcion == 2:
            id = input('ingresa un id para buscar: ')
            almacen.buscar_producto_por_id(id)
        elif opcion == 3:
            id = input("ingresa el id del producto que deseas buscar: ")
            resultado = almacen.buscar_producto_por_id(id)
            if resultado:
                guia_actualizacion()
                producto_actualizado = input("Ingresa: \n")[1:-1].split(',')
                #producto_actualizado = producto_actualizado[1:-1].split(',')
                almacen.actualizar_producto_en_stock(producto_actualizado)
        elif opcion==4:
            print("ingresa en el formato [id,nombre,precio_unitario,proveedor,cantidad_stock]")
            print("ejemplo: [1,jabon,12.2,proveedor 1,15]")
            producto = input("ingresa: \n")[1:-1].split(',')
            producto = list(map(str,producto))
            almacen.guardar_producto_en_stock(producto)
        elif opcion==5:
            id = input("ingresa el id del producto que deseas eliminar: ")
            almacen.eliminar_producto_en_stock(id)
