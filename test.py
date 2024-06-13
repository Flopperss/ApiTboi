import requests
import os

os.system('cls')

def execute_http_method(method, url, data=None):
    try:
        if data:
            response = requests.request(method, url, json=data)
        else:
            response = requests.request(method, url)
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        return 500, {'error': 'Error de conexión'}
    

# URL para piso aleatorio
url_piso_aleatorio = "http://127.0.0.1:5000/OBTENER_PISO_ALEATORIO"

print(f'Obtener un piso aleatorio')

status_code, response_json = execute_http_method('GET', url_piso_aleatorio)

print(f'    Status code: {status_code}')
print(f'    Respuesta  : {response_json}')


