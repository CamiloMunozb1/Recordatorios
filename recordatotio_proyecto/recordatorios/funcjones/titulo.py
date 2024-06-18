import sqlite3

def titulo():
    with sqlite3.connect("C:/Users/POWER/recordatorios_proyecto.db") as  titulo_recordatorio:
        try:
            consulta_cursor = titulo_recordatorio.cursor()
            usuario_titulo = str(input("ingresa el titulo del recordatorio: "))
            consulta_cursor.execute("INSERT INTO Datos_recordatorio (Titulo_recordatorio) VALUES (?)",(usuario_titulo))
            titulo_recordatorio.commit()
            print("titulo agregado correctamente")
        except ValueError as error:
            print(f"error de digitacion {error}")
        except sqlite3.Error as error:
            print(f"error en la base de datos {error}")