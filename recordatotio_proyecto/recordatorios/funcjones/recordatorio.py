
# IMPORTAR SQLITE3 PARA MANEJAR LA BASE DE DATOS

import sqlite3


# DEFINIR UNA FUNCION PARA USAR LA CONSULTA EN EL CODIGO PRINCIPAL

def recordatorio():

    #CONECTAR CON LA BASE DE DATOS 

    with sqlite3.connect("C:/Users/POWER/recordatorios_proyecto.db") as ingreso_recordatorio:
        try:

            # AÑADIR UN CURSOR PARA MANEJAR LA BASE DE DATOS

            consulta_cursor = ingreso_recordatorio.cursor()

            # ENTRADA DE USUARIO PARA INGRESAR EL RECORDATORIO

            usuario_recordatorio = str(input("ingreso de recordatorio: "))

            # ENTRADA DE USUARIO QUE PREGUNTA EL TITULO DEL RECORDATORIO

            titulo_recordatorio = str(input("Ingresa el titulo del recordatorio: "))

            # SE SELECCIONA LA TABLA "Datos_recoradatorio" Y EL CAMPO "TituloID" PARA ESTABLECER LA CLAVE FORANEA "Titulo_recordatorio"

            consulta_cursor.execute("SELECT TituloID fROM Datos_recordatorio WHERE Titulo_recordatorio = ?", (titulo_recordatorio,))

            # ACCEDEMOS A UNA FILA QUE ES "Titulo_recordatorio"

            titulo = consulta_cursor.fetchone()

            if titulo:

                # ALMACENAMOS EL "TituloID"

                titulo_id = titulo[0]

                # INSERTAMOS LOS DATOS A LA TABA  "Recordatorio"

                consulta_cursor.execute("INSERT INTO Recordatorio (Contenido_recordatorio,TituloID) VALUES (?,?)",(usuario_recordatorio,titulo_id))

                # AGREGAMOS LOS CAMBIOS A LA BASE DE DATOS

                ingreso_recordatorio.commit()
                print("recordatorio ingresado con exito")

            # MANEJO DE ERRORES
            else:

                print("Titulo no encontrado")

        except ValueError as value:
            
            print(f"no es una entrada valida : {value}")


