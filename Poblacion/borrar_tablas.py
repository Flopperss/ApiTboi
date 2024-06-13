import pyodbc

# Define la cadena de conexión
conn_str = 'DRIVER=ODBC Driver 17 for SQL Server; SERVER=hola\\SQLEXPRESS01; DATABASE=base_datos_isaac; UID=user; PWD=123;'

# Función para ejecutar consultas SQL
def exec_sql(query):
    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()

# Función para eliminar las tablas
def drop_tables():
    exec_sql("DROP TABLE IF EXISTS Jefes;")
    exec_sql("DROP TABLE IF EXISTS Pisos;")
    exec_sql("DROP TABLE IF EXISTS Objeto;")
    exec_sql("DROP TABLE IF EXISTS Capitulo;")
    exec_sql("DROP TABLE IF EXISTS Pildora;")
    exec_sql("DROP TABLE IF EXISTS Personaje;")

# Ejecutar la función para eliminar las tablas
if __name__ == "__main__":
    drop_tables()
