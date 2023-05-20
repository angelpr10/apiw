from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    api_key = '98d826f5837000880cabecb7c8d7df9f'
    ciudad = 'santander'

    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        clima_data = json.loads(response.text)
        temperatura_kelvin = clima_data['main']['temp']
        humedad = clima_data['main']['humidity']
        descripcion = clima_data['weather'][0]['description']
        temperatura_celsius = temperatura_kelvin - 273.15

        return render_template('index.html', temperatura=round(temperatura_celsius), humedad=humedad, descripcion=descripcion)
    else:
        return 'Error al obtener los datos del clima'

if __name__ == '__main__':
    app.run()

