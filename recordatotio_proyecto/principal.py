# IMPORTAR SQLITE3 PARA MANEJAR LA BASE DE DATOS

import sqlite3

# LLAMADA A LAS FUNCIONES PARA USARLO EN EL CODIGO PRINCIPAL

from recordatorios.funcjones.titulo import titulo
from recordatorios.funcjones.recordatorio import recordatorio
from recordatorios.funcjones.eliminacion import eliminarcion
from recordatorios.funcjones.completos import completos




while True:

    # MENU DE USUARIO

    print("""
          Bienvenido a su sistema de recordatorios:
          1. Ingresar el titulo del recordatorio
          2  Ingrese el recordatorio
          3. Mostrar recordatorios
          5. Eliminar recordatorios
          4. Salir
        """)
    try:

        # ENTRADA DE USUARIO

        usuario = int(input("ingresa una opcion: "))

        # CONDICIONES DEPENDIENDO DE LA ENTRADA DE USUARIO

        if usuario == 1:
            titulo()
        elif usuario == 2:
            recordatorio()
        elif usuario == 3:
            completos()
        elif usuario == 5:
            eliminarcion()
        elif usuario == 6:
            print("Gracias por gestionar sus recordatorios, hasta luego")
            break

    
    # MANEJO DE PROBLEMAS 
    except ValueError:
        print("entrada invalida")
    except sqlite3.Error as error:
        print(f"Error en la base de datos {error}")