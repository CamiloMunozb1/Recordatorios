
# IMPORTAR SQLITE3 PARA MANEJAR LA BASE DE DATOS

import sqlite3


# DEFINIR UNA FUNCION PARA USAR LA CPMSULTA EN EL CODIGO ORIGINAL

def eliminarcion():

    # CONCECTAMOS CON LA BASE DE DATOS

    with sqlite3.connect("C:/Users/POWER/recordatorios_proyecto.db") as eliminar_recordatorio:
        try:
            
            # AÑADIR UN CURSOR PARA MANEJAR LA BASE DE DATOS

            consulta_cursor =  eliminar_recordatorio.cursor()

            # ENTRADA DE USUARIO PARA INGRESAR EL TITULO DEL RECORDATORIO

            usuario_eliminar = str(input("ingresa el titulo del recordatorio que desees eliminar:  "))

            # ENTRADA DE USUARIO PARA INGRESAR EL ID DEL RECORDATORIO

            eliminar_contenido = int(input("ingresa el ID del recordatorio: "))

            # SE SELECCIONA LA TABLA "Datos_recoradatorio" Y EL CAMPO "Titulo_recordatorio" PARA ELIMINAR EL ID
            # SE SELECCIONA LA TABLA "Recordatorio" Y EL CAMPO "RecordatorioID" PARA Eliminar EL RECORDATORIO

            consulta_cursor.execute("DELETE FROM Datos_recordatorio wHERE Titulo_recordatorio = ?",(usuario_eliminar,))
            consulta_cursor.execute("DELETE FROM Recordatorio wHERE RecordatorioID = ? ", (eliminar_contenido,))

            # SE SUBEN LOS CAMBIOS A LA BASE DE DATOS

            eliminar_recordatorio.commit()

            print("Recordatorio eliminado correctamente")

        # MANEJO DE ERRORES

        except ValueError as error:

            print(f"Error de digitacion: {error}")
    