import pyodbc

# Define la cadena de conexión
conn_str = 'DRIVER=ODBC Driver 17 for SQL Server; SERVER=hola\\SQLEXPRESS01; DATABASE=base_datos_isaac; UID=user; PWD=123;'

# Función para ejecutar consultas SQL
def exec_sql(query):
    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()

# Función para crear las tablas
def create_tables():
    # Crear tabla Objeto
    exec_sql("""
    CREATE TABLE Objeto (
        id_obj INT PRIMARY KEY,
        nombre_obj NVARCHAR(100) NOT NULL,
        descripcion_obj NVARCHAR(MAX),
        categoria_obj INT,
        activable_obj BIT NOT NULL,
        cooldown_obj INT
    );
    """)

    # Crear tabla Capitulo
    exec_sql("""
    CREATE TABLE Capitulo (
        id_capitulo INT PRIMARY KEY,
        nombre_capitulo NVARCHAR(100) NOT NULL
    );
    """)

    # Crear tabla Pisos
    exec_sql("""
    CREATE TABLE Pisos (
        id_piso INT PRIMARY KEY,
        nombre_piso NVARCHAR(100) NOT NULL,
        descripcion_piso NVARCHAR(MAX),
        id_capitulo INT,
        FOREIGN KEY (id_capitulo) REFERENCES Capitulo(id_capitulo)
    );
    """)

    # Crear tabla Jefes
    exec_sql("""
    CREATE TABLE Jefes (
        id_jefe INT PRIMARY KEY,
        nombre_jefe NVARCHAR(100) NOT NULL,
        descripcion_jefe NVARCHAR(MAX),
        id_capitulo INT,
        id_piso INT,
        FOREIGN KEY (id_capitulo) REFERENCES Capitulo(id_capitulo),
        FOREIGN KEY (id_piso) REFERENCES Pisos(id_piso)
    );
    """)

    # Crear tabla Pildora
    exec_sql("""
    CREATE TABLE Pildora (
        id_pildora INT PRIMARY KEY,
        nombre_pildora NVARCHAR(100) NOT NULL,
        descripcion_pildora NVARCHAR(MAX)
    );
    """)

    # Crear tabla Personaje
    exec_sql("""
    CREATE TABLE Personaje (
        id_personaje INT PRIMARY KEY,
        nombre_personaje NVARCHAR(100) NOT NULL,
        descripcion NVARCHAR(MAX)
    );
    """)

# Ejecutar la función para crear las tablas
if __name__ == "__main__":
    create_tables()
