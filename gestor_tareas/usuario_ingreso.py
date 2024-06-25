import sqlite3

from base_datos.llamados_funcion.agregar_tarea import agregar_tarea
from base_datos.llamados_funcion.ver_tareas import ver_tareas
from base_datos.llamados_funcion.actualizar_tareas import actualizar_tareas
from base_datos.llamados_funcion.eliminar_tarea import eliminar_tarea


while True:
        print("""
            Bienvenido al gestor de tareas:
            1. Agregar tarea.
            2. Ver tareas
            3. Actualizar tareas.
            4. Eliminar tareas.
            6. Salir
            """)
        try:
            usuario = int(input("Ingrese una opcion: "))
            if usuario == 1:
            
        except ValueError:
             print("Entrada invalida")
        except sqlite3.Error as error:
              print(f"Error en la base de datos: {error}")
