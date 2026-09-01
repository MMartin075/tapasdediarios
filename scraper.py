import json
import re
import requests

# Fuentes de imágenes directas libres de bloqueo
DIARIOS = [
    {
        "nombre": "Clarín",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.clarin.com/",
        "img": "https://images.clarin.com/tapa/300/tapa.jpg",
    },
    {
        "nombre": "La Nación",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.lanacion.com.ar/",
        "img": "https://bucket1.glanacion.com/anexos/fotos/96/1234596.jpg",
    },
    {
        "nombre": "Página/12",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.pagina12.com.ar/",
        "img": "https://www.pagina12.com.ar/assets/media/logos/logo-p12.png",
    },
    {
        "nombre": "Perfil",
        "provincia": "Buenos Aires",
        "categoria": "General",
        "url": "https://www.perfil.com/",
        "img": "https://www.perfil.com/assets/img/logo-perfil.png",
    },
    {
        "nombre": "El Cronista",
        "provincia": "Buenos Aires",
        "categoria": "Economía",
        "url": "https://www.cronista.com/",
        "img": "https://www.cronista.com/files/image/414/414781/5ff46f882193b.png",
    },
    {
        "nombre": "Ámbito",
        "provincia": "Buenos Aires",
        "categoria": "Economía",
        "url": "https://www.ambito.com/",
        "img": "https://www.ambito.com/css/img/logo-ambito.png",
    },
    {
        "nombre": "Olé",
        "provincia": "Buenos Aires",
        "categoria": "Deportes",
        "url": "https://www.ole.com.ar/",
        "img": "https://www.ole.com.ar/images/ole-logo.png",
    },
]


def extraer_tapa_clarin():
  """Intenta obtener la URL exacta de la portada del día de Clarín."""
  try:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
    }
    res = requests.get("https://www.clarin.com/", headers=headers, timeout=10)
    match = re.search(r'https://images\.clarin\.com/tapa/[^\s"]+\.jpg', res.text)
    if match:
      return match.group(0)
  except Exception:
    pass
  return "https://images.clarin.com/tapa/300/tapa.jpg"


def generar_json():
  resultado = []

  # Actualizar Clarín con la tapa extraída
  tapa_clarin = extraer_tapa_clarin()

  for d in DIARIOS:
    img_final = tapa_clarin if d["nombre"] == "Clarín" else d["img"]
    resultado.append({
        "nombre": d["nombre"],
        "provincia": d["provincia"],
        "categoria": d["categoria"],
        "imagen": img_final,
        "enlace": d["url"],
    })

  with open("tapas.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
  generar_json()
