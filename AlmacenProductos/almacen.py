from producto import Producto
from file_handler import FileHandler


class Almacen:
    """Implementa las operaciones crud de FileHandler requeridas por el usuario"""
    def __init__(self,nombre):
        self.nombre  = nombre
        self.file_handler = FileHandler('./datos.txt')


    def listar_productos_en_stock(self):
        for registro in self.file_handler.get_data():
            product = Producto(*registro)
            print(product)

    def buscar_producto_por_id(self,id):
        #id = input('ingresa un id para buscar')
        producto = self.file_handler.buscar_registro_por_id(id)
        if producto:
            product = Producto(*producto)
            print("resultado de la busqueda \n :"+product.__str__())
            print("\n")
            return True
        else:
            print("no se encontro ningun producto asociado a ese id \n")
            return False
    def actualizar_producto_en_stock(self,producto_actualizado):
        self.file_handler.actualizar_registro(producto_actualizado)
        print("Actualizacion con exito")

    def guardar_producto_en_stock(self,producto):
        self.file_handler.insertar_pruducto(producto)


    def eliminar_producto_en_stock(self,id):
        if self.file_handler.buscar_registro_por_id(id):
            self.file_handler.eliminar_producto(id)
            print("Se ha eliminado con exito \n")
        else:
            print("No se puede eliminar un producto no registrado \n")
