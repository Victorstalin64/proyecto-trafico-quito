import requests
import csv
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": -0.1807,
    "lon": -78.4678,
    "appid": API_KEY,
    "units": "metric",
    "lang": "es"
}

respuesta = requests.get(url, params=params)
data = respuesta.json()

print(data)

fecha = datetime.now().isoformat(timespec="seconds")
temperatura = data["main"]["temp"]
humedad = data["main"]["humidity"]
descripcion = data["weather"][0]["description"]

with open("data/raw/clima_quito.csv", mode="a", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow([fecha, temperatura, humedad, descripcion])

print("Dato guardado en clima_quito.csv")