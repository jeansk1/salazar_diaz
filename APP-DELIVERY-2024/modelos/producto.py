from datetime import datetime 

class Producto:
    def __init__(self,id=None,nombre ="",descripcion ="",precio=0.0, tipo_producto=None,fecha_ingreso = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.tipo_producto = tipo_producto
        self.fecha_ingreso = fecha_ingreso if fecha_ingreso else datetime.now()
    def __str__(self):
        return f"Producto(id={self.id},nombre='{self.nombre}',descripcion ='{self.descripcion}',precio = {self.precio},tipo_producto = {self.tipo_producto},fecha_ingreso ={self.fecha_ingreso})"