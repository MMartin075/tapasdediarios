import json
import re
from datetime import datetime
import requests

# Mapeo de diarios con fuentes directas
DIARIOS = [
    {
        "nombre": "Clarín",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.clarin.com/",
        "img": "https://estaticos.kiosko.net/ar/750/clarin.jpg",
    },
    {
        "nombre": "La Nación",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.lanacion.com.ar/",
        "img": "https://estaticos.kiosko.net/ar/750/lanacion.jpg",
    },
    {
        "nombre": "Perfil",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.perfil.com/",
        "img": "https://estaticos.kiosko.net/ar/750/perfil.jpg",
    },
    {
        "nombre": "Página/12",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.pagina12.com.ar/",
        "img": "https://estaticos.kiosko.net/ar/750/pagina12.jpg",
    },
    {
        "nombre": "Crónica",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.cronica.com.ar/",
        "img": "https://estaticos.kiosko.net/ar/750/cronica.jpg",
    },
    {
        "nombre": "Diario Popular",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.diariopopular.com.ar/",
        "img": "https://estaticos.kiosko.net/ar/750/diario_popular.jpg",
    },
    {
        "nombre": "Ámbito",
        "provincia": "Buenos Aires",
        "categoria": "Economía",
        "url": "https://www.ambito.com/",
        "img": "https://estaticos.kiosko.net/ar/750/ambito_financiero.jpg",
    },
    {
        "nombre": "El Cronista",
        "provincia": "Buenos Aires",
        "categoria": "Economía",
        "url": "https://www.cronista.com/",
        "img": "https://estaticos.kiosko.net/ar/750/cronista_comercial.jpg",
    },
    {
        "nombre": "Olé",
        "provincia": "Buenos Aires",
        "categoria": "Deportes",
        "url": "https://www.ole.com.ar/",
        "img": "https://estaticos.kiosko.net/ar/750/ole.jpg",
    },
]


def generar_json():
  resultado = []
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
      )
  }

  for d in DIARIOS:
    resultado.append({
        "nombre": d["nombre"],
        "provincia": d["provincia"],
        "categoria": d["categoria"],
        "imagen": d["img"],
        "enlace": d["url"],
    })

  with open("tapas.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
  generar_json()
