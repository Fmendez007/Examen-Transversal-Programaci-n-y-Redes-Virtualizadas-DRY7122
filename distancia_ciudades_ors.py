import requests

API_KEY = "5b3ce3597851110001cf6248875666606b464625827048f1332a885f"

def calcular_distancia(origen, destino, transporte):
    url_geocode = "https://api.openrouteservice.org/geocode/search"
    headers = {'Authorization': API_KEY}

    # Coordenadas origen
    params_origen = {"api_key": API_KEY, "text": origen}
    r1 = requests.get(url_geocode, params=params_origen)
    coord_origen = r1.json()["features"][0]["geometry"]["coordinates"]

    # Coordenadas destino
    params_destino = {"api_key": API_KEY, "text": destino}
    r2 = requests.get(url_geocode, params=params_destino)
    coord_destino = r2.json()["features"][0]["geometry"]["coordinates"]

    # Tipo de transporte
    modo = {
        "auto": "driving-car",
        "bici": "cycling-regular",
        "caminando": "foot-walking"
    }.get(transporte, "driving-car")

    # Ruta
    url_ruta = f"https://api.openrouteservice.org/v2/directions/{modo}"
    body = {
        "coordinates": [coord_origen, coord_destino]
    }

    r3 = requests.post(url_ruta, json=body, headers=headers)
    data = r3.json()
    distancia_m = data["routes"][0]["summary"]["distance"]
    duracion_s = data["routes"][0]["summary"]["duration"]

    # Conversión
    km = distancia_m / 1000
    millas = km * 0.621371
    horas = duracion_s / 3600

    return km, millas, horas, modo.replace("-", " ")

# Programa principal
while True:
    print("\n🧭 Calculadora de Distancia entre Ciudades (Chile ↔ Argentina)")
    origen = input("Ingrese ciudad de origen (o 's' para salir): ").strip()
    if origen.lower() == 's':
        break

    destino = input("Ingrese ciudad de destino: ").strip()
    transporte = input("Seleccione transporte (auto, bici, caminando): ").strip()

    try:
        km, mi, hrs, modo = calcular_distancia(origen, destino, transporte)
        print(f"\n📍 De {origen} a {destino} en {transporte}:")
        print(f"📏 Distancia: {round(km, 2)} km / {round(mi, 2)} millas")
        print(f"⏱️  Duración estimada: {round(hrs, 2)} horas")
        
        # 📝 Narrativa del viaje
        print("\n📝 Narrativa del Viaje:")
        print(f"Desde la ciudad de {origen}, ubicada en Chile, emprenderás un viaje hacia {destino}, en Argentina, utilizando el medio de transporte seleccionado: {transporte}.")
        print(f"El recorrido tiene una distancia aproximada de {round(km, 2)} kilómetros, lo que equivale a {round(mi, 2)} millas.")
        print(f"La duración estimada del viaje es de alrededor de {round(hrs, 2)} horas considerando condiciones normales en la ruta.")
        print("Disfruta del trayecto y ten un buen viaje.\n")
        
    except Exception as e:
        print(f"❌ Error al calcular: {e}")
