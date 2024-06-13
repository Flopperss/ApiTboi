import pyodbc


#Eldiavlo\\SQLEXPRESS
#hola\SQLEXPRESS01
conn_str = 'DRIVER=ODBC Driver 17 for SQL Server; SERVER=hola\\SQLEXPRESS01; DATABASE=base_datos_isaac; UID=user; PWD=123;'

def exec_sql(query):
    with pyodbc.connect(conn_str) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()


def populate_tables():
    # Poblar tabla Personaje
    exec_sql("INSERT INTO Personaje (id_personaje, nombre_personaje, descripcion) VALUES (1, 'Isaac', 'Main character');")
    exec_sql("INSERT INTO Personaje (id_personaje, nombre_personaje, descripcion) VALUES (2, 'Magdalene', 'High health character');")
    exec_sql("INSERT INTO Personaje (id_personaje, nombre_personaje, descripcion) VALUES (3, 'Cain', 'High luck character');")


    # Poblar tabla Capitulo
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (1, 'Capitulo 1');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (2, 'Capitulo 1.5');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (3, 'Capitulo 2');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (4, 'Capitulo 2.5');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (5, 'Capitulo 3');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (6, 'Capitulo 3.5');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (7, 'Capitulo 4');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (8, 'Capitulo 4.5');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (9, 'Capitulo 5');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (10, 'Capitulo 6');")
    exec_sql("INSERT INTO Capitulo (id_capitulo, nombre_capitulo) VALUES (11, 'Endgame');")


    # Poblar tabla Pisos
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (1, 'Sótano', 'El tema del Sótano son las moscas y la caca',1,'S');")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (2, 'Bodega', 'Llena principalmente de arañas y sus telarañas',1);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (3, 'Sótano en Llamas','Es un piso de habitaciones hechas de madera, pero de las cuales todas están quemándose, dándole un aspecto rojizo, leno de humo y chispas de fuego',2);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (4, 'Aguacero', 'El tema de Aguacero son los desagües pluviales inundados y embrujados, con muchos enemigos y elementos sobrenaturales.',2);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (5, 'Desechos', 'Piso alternativo a Aguacero, que se diferencia de éste por tener más caca y aguas residuales.',2);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (6, 'Cuevas', 'Este ambiente presenta Posos y Espinas.',3);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (7, 'Catacumbas', 'Generalmente posee más arañas y enemigos/jefes descompuestos que las cuevas.',3);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (8, 'Cuevas Inundadas', 'El tema de las Cuevas Inundadas es el agua; como tal, la mayoría de los enemigos que la habitan son aéreos',3);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (9, 'Minas', 'Su apariencia es la de unas minas de color gris con piso de tierra, sus paredes tienen tablas de madera clavadas para que no se caiga la estructura y linternas para iluminar.',4);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (10, 'Foso de cenizas', 'La apariencia del piso es la de una fosa cubierta de cenizas de color naranja y gris.',4);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (11, 'Profundidades', 'Toma la forma de una grisácea cueva sucia, llena de huesos, piedras y calaveras.',5);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (12, 'Necropolis', 'Es similar a Profundidades con agujeros, púas y bloques con cerrojo, excepto que las paredes tienen pilares.',5);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (13, 'Profundidades oscuras', 'El tema de la habitacion es el alquitrán, que gotea del techo y burbujea en los pozos.',5);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (14, 'Mausoleo', 'La apariencia es de un Mausoleo común y corriente solo que de color negro y morado',6);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (15, 'Gehenna', 'La apariencia de Gehenna es la de una especie de conjunto de habitaciones de tortura de color rojo y negro',6);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (16, 'The Womb', 'Piso alternativo a Aguacero, que se diferencia de éste por tener más caca y aguas residuales.',7);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (17, 'Útero', 'Las paredes y el suelo tienen un aspecto rojo y carnoso, simulando el interior de un útero.',7);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (18, 'Scarred Womb', 'Similar a The Womb, pero con una apariencia aún más sangrienta y visceral.',7);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (19, '???', 'El diseño de las paredes y del suelo de este piso se parecen a The Womb, pero de color azul, de las cuales se pueden apreciar figuras parecidas a rostros.',8);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (20, 'Corpse', ' Presenta una atmósfera desoladora y lúgubre con enemigos que llevan el tema de la muerte y la putrefacción avanzada',8);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (21, 'Catedral', 'La Catedral tiene una sola planta, en la que la mayoría de los enemigos son muertos vivientes o santos.',9);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (22, 'Sheol', 'Sheol tiene una sola planta, con muertos vivientes y enemigos oscuros/demoníacos.',9);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (23, 'The Chest', 'Tiene una apariencia dorada y lujosa, con cofres y objetos brillantes por todas partes.',10);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (24, 'Dark Room', 'Las habitaciones de la Dark Room suelen estar desprovistas de rocas y otros obstáculos, pero están llenas principalmente de jefes y minijefes.',10);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (25, 'The void', 'Tiene un diseño caótico y surrealista, combinando elementos visuales de varios otros pisos del juego.',11);")
    exec_sql("INSERT INTO Pisos (id_piso, nombre_piso, descripcion_piso, id_capitulo) VALUES (26, 'Home', 'Home posee la habitación de Isaac, dos pasillos, el clóset de Isaac, la sala de estar y la habitación de mamá.',11);")




    # Poblar tabla Objeto
    exec_sql("INSERT INTO Objeto (id_obj, nombre_obj, descripcion_obj, categoria_obj, activable_obj, cooldown_obj) VALUES (1, 'The D6', 'Allows Isaac to reroll his destiny', 4, 1, 6);")
    exec_sql("INSERT INTO Objeto (id_obj, nombre_obj, descripcion_obj, categoria_obj, activable_obj, cooldown_obj) VALUES (2, 'Sacred Heart', 'Greatly increases damage',4,0,0);")
    exec_sql("INSERT INTO Objeto (id_obj, nombre_obj, descripcion_obj, categoria_obj, activable_obj, cooldown_obj) VALUES (3, 'Brimstone', 'Isaac can fire a blood laser beam',4,0,0);")

    # Poblar tabla Jefes
    exec_sql("INSERT INTO Jefes (id_jefe, nombre_jefe, descripcion_jefe, id_capitulo, id_piso) VALUES (1, 'Monstro', 'Common boss enemy',1,1);")
    exec_sql("INSERT INTO Jefes (id_jefe, nombre_jefe, descripcion_jefe, id_capitulo, id_piso) VALUES (2, 'Duke of Flies', 'Boss surrounded by flies',1,1);")
    exec_sql("INSERT INTO Jefes (id_jefe, nombre_jefe, descripcion_jefe, id_capitulo, id_piso) VALUES (3, 'Gurdy', 'Boss that spawns enemies and shoots',1,1);")


    # Poblar tabla Pildora
    exec_sql("INSERT INTO Pildora (id_pildora, nombre_pildora,descripcion_pildora) VALUES (1, N'Monstro', N'Common boss enemy');")
    

if __name__ == "__main__":
    populate_tables()