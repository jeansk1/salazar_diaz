from mysql.connector import Error
from modelos import TipoProducto
from db_conexion import DatabaseConnection

class TipoProductoOperaciones:
    def __init__(self):
        self.db_conexion = DatabaseConnection()

    def agregar(self, tipo_producto):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor()
            query = "insert into TipoProducto(nombre,descripcion) values(%s,%s)"
            valores = (tipo_producto.nombre, tipo_producto.descripcion)
            cursor.execute(query, valores)
            conexion.commit()
            tipo_producto.id = cursor.lastrowid
            print("Tipo de producto se ha ingresado correctamente")
            return tipo_producto
        except Error as e:
            print(f"Error al insertar registro : {e} ")
        finally:
            if cursor:
                cursor.close()

    def obtener_datos(self):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor(dictionary = True)
            query = "select * from TipoProducto"
            cursor.execute(query)
            resultados = cursor.fetchall()
            return [TipoProducto(**resultado) for resultado in resultados]
        except Error as e:
            print(f"Error al consultar datos : {e}")
        finally:
            if cursor:
                cursor.close()

    def actualizar(self, tipo_producto):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor()
            query = "update TipoProducto set nombre = %s, descripcion = %s where id = %s"
            valores = (tipo_producto.nombre, tipo_producto.descripcion, tipo_producto.id)
            cursor.execute(query, valores)
            conexion.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al actualizar registro : {e}")
            return False
        finally:
            if cursor:
                cursor.close()

    def eliminar(self, id):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor()
            query = "delete from TipoProducto where id = %s"
            cursor.execute(query, (id,))
            conexion.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error al eliminar registro : {e}")
            return False
        finally:
            if cursor:
                cursor.close()
        

