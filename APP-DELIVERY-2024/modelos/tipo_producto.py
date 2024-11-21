from datetime import datetime 

class TipoProducto:
    def __init__(self,id=None,nombre ="",descripcion ="",fecha_ingreso = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_ingreso = fecha_ingreso if fecha_ingreso else datetime.now()
    def __str__(self):
        return f"TipoProducto(id={self.id},nombre='{self.nombre}',descripcion ='{self.descripcion}',fecha_ingreso ={self.fecha_ingreso})"