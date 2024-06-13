import pyodbc

conn_str = 'DRIVER=ODBC Driver 17 for SQL Server; SERVER=hola\\SQLEXPRESS01; DATABASE=base_datos_isaac; UID=user; PWD=123;'


# La cláusula TOP 1 se usa para seleccionar solo la primera fila del conjunto de resultados
# La función NEWID() genera un identificador único que se puede utilizar para ordenar aleatoriamente las filas de una tabla.
# En resumen primero NEWID ordena aleatoriamente las filas y luego TOP 1 devuelve la primera fila
def create_procedure_SP_OBTENER_PISO_ALEATORIO():
    query = """
    CREATE PROCEDURE SP_OBTENER_PISO_ALEATORIO
    AS
    BEGIN
        SELECT TOP 1 *
        FROM Pisos
        ORDER BY NEWID();
    END;
    """
    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()

if __name__ == "__main__":
    create_procedure_SP_OBTENER_PISO_ALEATORIO()