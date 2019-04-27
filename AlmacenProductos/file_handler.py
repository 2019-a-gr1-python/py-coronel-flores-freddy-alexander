import numpy as np
class FileHandler:
    """Inplementa las operaciones crud sobre el archivo y guarda los cambios en el txt"""
    def __init__(self,path):
        self.path = path
        self.registros = self.load_data()

    def load_data(self):
        return np.loadtxt(self.path,delimiter=',',dtype='str').tolist()

    def buscar_registro_por_id(self,id):
        # search a product by id and return an product as a list else None
        for registro in self.registros:
            if int(registro[0])==int(id):
                return registro
        return None

    def get_data(self):
        return self.registros

    def _guardar_registros(self):
        np.savetxt('datos.txt',X=np.array(self.registros),delimiter=',',fmt='%s')
        self.registros = self.load_data()

    def actualizar_registro(self,producto_lista): # recibe un producto como una lista
        id = producto_lista[0]
        #producto_lista = np.array(producto_lista)
        for i in range(len(self.registros)):
            if int(self.registros[i][0]) == int(id):
                self.registros[i] = producto_lista
                break
        self._guardar_registros()

    def eliminar_producto(self,producto_id):

        #producto_eliminar = self.buscar_registro_por_id(producto_id)
        for i in range(len(self.registros)):
            if int(self.registros[i][0]) == int(producto_id):
                del self.registros[i]
                self._guardar_registros()
                break

    def insertar_pruducto(self,producto_as_list):
        if self.buscar_registro_por_id(producto_as_list[0]) is None:
            self.registros.append(producto_as_list)
            print("Insercion exitosa \n")
            self._guardar_registros()
        else:
            print("dos productos no pueden tener el mismo id \n")
