import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    _instance = None  # Atributo para almacenar la instancia única de la conexión

    def __new__(cls):
        # Verificamos si ya existe una instancia de la conexión
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = None  # Inicializamos la conexión en None
        return cls._instance
    
    def connect(self):
        # Si la conexión no está activa, la creamos
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = mysql.connector.connect(
                    host='192.168.56.101',  # IP del servidor MySQL
                    database='delivery2',   # Nombre de la base de datos
                    user='pythonapp',       # Usuario de conexión
                    password='inacap.2024'  # Contraseña
                )
                print("Conexión efectuada correctamente")
            except Error as e:
                print(f"Se ha producido un error: {e}")
                self.connection = None
        return self.connection

    def close(self):
        # Cerrar la conexión si está activa
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            self.connection = None
            print("Conexión cerrada")

    def get_connection(self):
        # Devolvemos la conexión existente o la creamos
        return self.connect()
      
            

        
