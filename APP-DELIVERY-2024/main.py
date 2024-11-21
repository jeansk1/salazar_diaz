# Importar clases y operaciones de productos
from modelos.tipo_producto import TipoProducto
from operaciones.tipo_producto_operaciones import TipoProductoOperaciones

# Importar las operaciones de repartidores
from operaciones.gestion_repartidores import (
    listar_repartidores,
    agregar_repartidor,
    actualizar_repartidor,
    eliminar_repartidor
)

def menu_productos():
    """Menú para gestionar productos"""
    operaciones = TipoProductoOperaciones()

    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Agregar tipo de producto")
        print("2. Listar tipo de producto")
        print("3. Actualizar tipo de producto")
        print("4. Eliminar tipo de producto")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del tipo de producto: ")
            descripcion = input("Descripción: ")
            nuevoTipoProducto = TipoProducto(nombre=nombre, descripcion=descripcion)
            resultado = operaciones.agregar(nuevoTipoProducto)
            if resultado:
                print(f"Tipo de producto ingresado correctamente con ID: {resultado.id}")
        elif opcion == "2":
            tipos_producto = operaciones.obtener_datos()
            if tipos_producto:
                print("\n=== Tipos de Producto ===")
                for tipo in tipos_producto:
                    print(f"ID: {tipo.id}")
                    print(f"Nombre: {tipo.nombre}")
                    print(f"Descripción: {tipo.descripcion}")
                    print(f"Fecha de ingreso: {tipo.fecha_ingreso}")
                    print("-" * 30)
            else:
                print("\nNo hay tipos de producto registrados.")
        elif opcion == "3":
            id = input("ID del tipo de producto a actualizar: ")
            nombre = input("Nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            tipo_producto = TipoProducto(id=int(id), nombre=nombre, descripcion=descripcion)
            if operaciones.actualizar(tipo_producto):
                print("Tipo de producto actualizado correctamente.")
            else:
                print("No se pudo actualizar el tipo de producto.")
        elif opcion == "4":
            id = input("ID del tipo de producto a eliminar: ")
            if operaciones.eliminar(int(id)):
                print("Tipo de producto eliminado correctamente.")
            else:
                print("No se pudo eliminar el tipo de producto.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def menu_repartidores():
    """Menú para gestionar repartidores"""
    while True:
        print("\n--- Gestión de Repartidores ---")
        print("1. Listar repartidores")
        print("2. Agregar repartidor")
        print("3. Actualizar repartidor")
        print("4. Eliminar repartidor")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            repartidores = listar_repartidores()
            print("\n=== Repartidores ===")
            for rep in repartidores:
                print(f"ID: {rep[0]}, Nombre: {rep[1]}, Teléfono: {rep[2]}, Dirección: {rep[3]}, Activo: {rep[4]}, Fecha Registro: {rep[5]}")
        elif opcion == "2":
            nombre = input("Nombre del repartidor: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            activo = input("¿Está activo? (True/False): ").lower() == "true"
            agregar_repartidor(nombre, telefono, direccion, activo)
            print(f"Repartidor '{nombre}' agregado exitosamente.")
        elif opcion == "3":
            id_repartidor = int(input("ID del repartidor a actualizar: "))
            nombre = input("Nuevo nombre (deja vacío para no cambiar): ")
            telefono = input("Nuevo teléfono (deja vacío para no cambiar): ")
            direccion = input("Nueva dirección (deja vacío para no cambiar): ")
            activo = input("¿Está activo? (True/False, deja vacío para no cambiar): ")
            activo = None if activo == "" else activo.lower() == "true"
            actualizar_repartidor(id_repartidor, nombre or None, telefono or None, direccion or None, activo)
            print(f"Repartidor con ID {id_repartidor} actualizado exitosamente.")
        elif opcion == "4":
            id_repartidor = int(input("ID del repartidor a eliminar: "))
            eliminar_repartidor(id_repartidor)
            print(f"Repartidor con ID {id_repartidor} eliminado exitosamente.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def main():
    """Menú principal para seleccionar entre gestionar productos o repartidores"""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Productos")
        print("2. Gestión de Repartidores")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_repartidores()
        elif opcion == "3":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()

