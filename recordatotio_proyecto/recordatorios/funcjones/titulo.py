
# IMPORTAMOS SQLITE3 PARA TRABAJAR CON LA BASE DE DATOS

import sqlite3


# USAMOS UNA FUNCION PARA LA CONSULTA EN EL CODIGO ORIGINAL

def titulo():

    # CONECTAMOS CON LA BASE DE DATOS Y CON UN WITH  PARA CERRAR LA CONSULTA AUTOMATICAMENTE

    with sqlite3.connect("C:/Users/POWER/recordatorios_proyecto.db") as  titulo_recordatorio:
        try:

            # INICIAR UN CURSOR PARA MANEJAR LA BASE DE DATOS

            consulta_cursor = titulo_recordatorio.cursor()

            # ENTRADA DE USUARIO

            usuario_titulo = str(input("ingresa el titulo del recordatorio: "))

            # USUAMOS UNA CONSULTA QUE INSERTE EL TITULO DEL RECORDATORIO EN LA TABLA "Datos_recordatorio"

            consulta_cursor.execute("INSERT INTO Datos_recordatorio (Titulo_recordatorio) VALUES (?)",(usuario_titulo,))

            # AGREGAMOS LOS CAMBIOS A LA BASE

            titulo_recordatorio.commit()
            print("titulo agregado correctamente")

        #MANEJO DE ERRORES
        except ValueError as error:
            print(f"error de digitacion {error}")