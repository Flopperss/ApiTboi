@echo off
REM Navegar a la carpeta Poblacion
cd Poblacion

echo Tablas Borrandose..

REM Ejecutar el script para borrar las tablas
python borrar_tablas.py


echo Tablas Creandose..

REM Ejecutar el script para crear las tablas
python crear_tablas.py


echo Tablas Poblandose..

REM Ejecutar el script para poblar las tablas
python poblar_tablas.py

echo Creando procedimientos..

REM Ejecutar el script para crear procedimientos
python crear_procedimientos.py

REM Navegar a la carpeta base
cd..

echo Scripts ejecutados correctamente.
pause
