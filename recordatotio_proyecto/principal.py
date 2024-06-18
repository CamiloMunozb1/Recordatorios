import sqlite3
from recordatorios.funcjones.titulo import titulo



while True:
    print("""
          Bienvenido a su sistema de recordatorios:
          1. Ingresar el titulo del recordatorio
          2 Ingrese el recordatorio
          3. Salir
        """)
    try:
        usuario = int(input("ingresa una opcion: "))
        if usuario == 1:
            titulo()
    except ValueError:
        print("entrada invalida")
    except sqlite3.Error as error:
        print(f"Error en la base de datos {error}")