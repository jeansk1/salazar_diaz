from datetime import datetime

class Repartidor:
    def __init__(self, id=None, nombre="", telefono="", direccion="", activo=True, fecha_ingreso=None):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.activo = activo
        self.fecha_ingreso = fecha_ingreso if fecha_ingreso else datetime.now()

    def __str__(self):
        return (
            f"Repartidor(id={self.id}, nombre='{self.nombre}', telefono='{self.telefono}', "
            f"direccion='{self.direccion}', activo={self.activo}, fecha_ingreso={self.fecha_ingreso})"
        )

