from mysql.connector import Error
from db_conexion import DatabaseConnection

# Función para listar repartidores
def listar_repartidores():
    """Obtiene y retorna una lista de repartidores desde la base de datos"""
    try:
        # Usamos la clase DatabaseConnection para obtener la conexión
        db_connection = DatabaseConnection()
        conexion = db_connection.get_connection()

        # Usamos 'with' para garantizar el cierre adecuado de la conexión
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM repartidores;")
            repartidores = cursor.fetchall()
            return repartidores

    except Error as e:
        print(f"Error al conectar o consultar la base de datos: {e}")
        return []

    finally:
        if conexion.is_connected():
            conexion.close()

# Función para agregar un repartidor
def agregar_repartidor(nombre, telefono, direccion, activo=True):
    """Agrega un nuevo repartidor a la base de datos"""
    try:
        # Usamos la clase DatabaseConnection para obtener la conexión
        db_connection = DatabaseConnection()
        conexion = db_connection.get_connection()

        # Usamos 'with' para garantizar el cierre adecuado de la conexión
        with conexion.cursor() as cursor:
            sql = "INSERT INTO repartidores (nombre, telefono, direccion, activo) VALUES (%s, %s, %s, %s)"
            valores = (nombre, telefono, direccion, activo)
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Repartidor '{nombre}' agregado correctamente.")

    except Error as e:
        print(f"Error al agregar el repartidor: {e}")

    finally:
        if conexion.is_connected():
            conexion.close()

# Función para actualizar un repartidor
def actualizar_repartidor(id_repartidor, nombre=None, telefono=None, direccion=None, activo=None):
    """Actualiza los datos de un repartidor"""
    try:
        # Usamos la clase DatabaseConnection para obtener la conexión
        db_connection = DatabaseConnection()
        conexion = db_connection.get_connection()

        # Usamos 'with' para garantizar el cierre adecuado de la conexión
        with conexion.cursor() as cursor:
            sql = "UPDATE repartidores SET "
            valores = []

            if nombre:
                sql += "nombre = %s, "
                valores.append(nombre)
            if telefono:
                sql += "telefono = %s, "
                valores.append(telefono)
            if direccion:
                sql += "direccion = %s, "
                valores.append(direccion)
            if activo is not None:
                sql += "activo = %s, "
                valores.append(activo)

            # Eliminamos la última coma y espacio y añadimos la condición WHERE
            sql = sql.rstrip(", ") + " WHERE id = %s"
            valores.append(id_repartidor)

            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Repartidor con ID {id_repartidor} actualizado correctamente.")

    except Error as e:
        print(f"Error al actualizar el repartidor: {e}")

    finally:
        if conexion.is_connected():
            conexion.close()

# Función para eliminar un repartidor
def eliminar_repartidor(id_repartidor):
    """Elimina un repartidor de la base de datos"""
    try:
        # Usamos la clase DatabaseConnection para obtener la conexión
        db_connection = DatabaseConnection()
        conexion = db_connection.get_connection()

        # Usamos 'with' para garantizar el cierre adecuado de la conexión
        with conexion.cursor() as cursor:
            sql = "DELETE FROM repartidores WHERE id = %s"
            cursor.execute(sql, (id_repartidor,))
            conexion.commit()
            print(f"Repartidor con ID {id_repartidor} eliminado correctamente.")

    except Error as e:
        print(f"Error al eliminar el repartidor: {e}")

    finally:
        if conexion.is_connected():
            conexion.close()

