@echo off
rem Elimina el entorno virtual si existe
if exist venv rmdir /s /q venv

rem Actualiza pip
call python -m pip install --upgrade pip

rem Instala virtualenv
call pip install --upgrade virtualenv

rem Crea el entorno virtual
call python -m venv venv

rem Activa el entorno virtual
call venv\Scripts\activate.bat

rem Actualiza pip dentro del entorno virtual
call python -m pip install --upgrade pip

rem Instala Flask y otras dependencias
call pip install Flask
call pip install flask-restful
call pip install flask_migrate
call pip install flask_wtf
call pip install pyodbc
call pip install requests



rem Desactiva el entorno virtual
call venv\Scripts\deactivate.bat

echo Setup completo.
pause
