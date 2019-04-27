

class Producto:

    def __init__(self,id,nombre,precio_unitario,proveedor,cantidad_stock):
        self.id = id
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.proveedor = proveedor
        self.cantidad_stock = cantidad_stock


    def get_producto_string_separado_comas(self):
        return str(self.id)+','+self.nombre+','+str(self.precio_unitario)+','+self.proveedor+','+str(self.cantidad_stock)+'\n'

    def __str__(self):
        return "id: {} nombre: {}| precio unitario: {}| proveedor: {}| cantidad stock: {}".format(self.id,
                                                                                                       self.nombre,
                                                                                                       self.precio_unitario,
                                                                                                       self.proveedor,
                                                                                                       self.cantidad_stock)
