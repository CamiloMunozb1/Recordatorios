
# IMPORTAR SQLITE3 PARA MANEJAR LA BASE DE DATOS
import sqlite3

# IMPORTAR PANDAS PARA VER LA BASE DE DATOS DE FORMA CLARA 

import pandas as pd


# DEFINIR UNA FUNCION PARA USAR LA CONSULTA EN EL CODIGO ORIGINAL 

def completos():

    # CONECTAMOS CON LA BASE DE DATOS 

    with sqlite3.connect("C:/Users/POWER/recordatorios_proyecto.db") as mostrar_recordatorios:

        # DEFINIR UN CURSOR PARA MANEJAR LA BASE DE DATOS

        consulta_cursor = mostrar_recordatorios.cursor()

        # SELECCIONAR LA BASE DE DATOS A MOSTAR

        consulta_cursor.execute("SELECT * FROM Recordatorio")

        # SE USA "FETCHALL" UN METODO DE LECTURA

        resultado = consulta_cursor.fetchall()

    # SE UTILIZA EL MODULO "DataFrame" PARA MOSTAR LA TABLA

    resultado_df = pd.DataFrame(resultado)

    # MOSTRAMOS LA TABLA DE LA BASE DE DATOS
    
    print(resultado_df)