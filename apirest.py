from flask import Flask, jsonify, request
import pyodbc
import os

#Eldiavlo\\SQLEXPRESS
#hola\SQLEXPRESS01
conn_str = 'DRIVER=ODBC Driver 17 for SQL Server; SERVER=hola\\SQLEXPRESS01; DATABASE=base_datos_isaac; UID=user; PWD=123;'

app = Flask(__name__)


def OBTENER_PISO_ALEATORIO():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute('EXEC dbo.SP_OBTENER_PISO_ALEATORIO')
        rows = cursor.fetchall()
        conn.close()

        # Convertir los resultados en una lista de diccionarios
        piso = []
        for row in rows:
            piso.append({
                'id_piso': row.id_piso,
                'nombre_piso': row.nombre_piso,
                'descripcion_piso': row.descripcion_piso,
            })

        return piso
    except Exception as e:
        raise e

@app.route('/OBTENER_PISO_ALEATORIO', methods=['GET'])
def get_piso_aleatorio():
    try:
        piso = OBTENER_PISO_ALEATORIO()
        return jsonify(piso), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500