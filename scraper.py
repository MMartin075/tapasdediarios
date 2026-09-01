import json
import re
import requests
from bs4 import BeautifulSoup

def obtener_tapa_clarin():
    try:
        url = "https://www.clarin.com/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        res = requests.get(url, headers=headers, timeout=10)
        match = re.search(r'https://images\.clarin\.com/tapa/[^\s"]+\.jpg', res.text)
        if match:
            return match.group(0)
    except Exception:
        pass
    return "https://www.clarin.com/redaccion/deportes/diario-clarin.jpg"

def obtener_tapa_lanacion():
    try:
        url = "https://www.lanacion.com.ar/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        img = soup.find('meta', property='og:image')
        if img and img.get('content'):
            return img['content']
    except Exception:
        pass
    return ""

def obtener_tapa_pagina12():
    try:
        url = "https://www.pagina12.com.ar/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        img = soup.find('meta', property='og:image')
        if img and img.get('content'):
            return img['content']
    except Exception:
        pass
    return ""

def obtener_tapa_perfil():
    try:
        url = "https://www.perfil.com/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        img = soup.find('meta', property='og:image')
        if img and img.get('content'):
            return img['content']
    except Exception:
        pass
    return ""

def obtener_tapa_cronista():
    try:
        url = "https://www.cronista.com/"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        img = soup.find('meta', property='og:image')
        if img and img.get('content'):
            return img['content']
    except Exception:
        pass
    return ""

def generar_json():
    # Scraping directo sitio por sitio
    diarios = [
        {
            "nombre": "Clarín",
            "provincia": "Buenos Aires",
            "categoria": "General",
            "imagen": obtener_tapa_clarin(),
            "enlace": "https://www.clarin.com/"
        },
        {
            "nombre": "La Nación",
            "provincia": "Buenos Aires",
            "categoria": "General",
            "imagen": obtener_tapa_lanacion(),
            "enlace": "https://www.lanacion.com.ar/"
        },
        {
            "nombre": "Perfil",
            "provincia": "Buenos Aires",
            "categoria": "General",
            "imagen": obtener_tapa_perfil(),
            "enlace": "https://www.perfil.com/"
        },
        {
            "nombre": "Página/12",
            "provincia": "Buenos Aires",
            "categoria": "General",
            "imagen": obtener_tapa_pagina12(),
            "enlace": "https://www.pagina12.com.ar/"
        },
        {
            "nombre": "El Cronista",
            "provincia": "Buenos Aires",
            "categoria": "Economía",
            "imagen": obtener_tapa_cronista(),
            "enlace": "https://www.cronista.com/"
        }
    ]

    with open("tapas.json", "w", encoding="utf-8") as f:
        json.dump(diarios, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generar_json()
