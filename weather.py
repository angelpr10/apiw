import requests
import json

# Ingresa tu clave de API de OpenWeatherMap aquí
api_key = '98d826f5837000880cabecb7c8d7df9f'

# Ingresa la ubicación para la cual deseas obtener el clima
ciudad = 'santander'

# Realiza una solicitud GET a la API de OpenWeatherMap
url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'
response = requests.get(url)

# Comprueba si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Convierte la respuesta en formato JSON a un objeto Python
    clima_data = json.loads(response.text)
    
    # Extrae los datos relevantes del objeto de datos
    temperatura_kelvin = clima_data['main']['temp']
    humedad = clima_data['main']['humidity']
    descripcion = clima_data['weather'][0]['description']
    
    # Convierte la temperatura de Kelvin a Celsius
    temperatura_celsius = temperatura_kelvin - 273.15
    
    # Imprime la información del clima
    print(f'Temperatura: {round(temperatura_celsius)} °C')
    print(f'Humedad: {humedad}%')
    print(f'Descripción: {descripcion}')
else:
    print('Error al realizar la solicitud a la API')

