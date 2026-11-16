import csv
import requests
from bs4 import BeautifulSoup

# URL base del catálogo (usamos una página de práctica segura)
URL_BASE = "https://books.toscrape.com/catalogue/page-{}.html"

def extraer_libros(paginas_a_recorrer=3):
    """Recorre las primeras N páginas del catálogo y extrae título, precio y disponibilidad."""
    lista_libros = []

    for pagina in range(1, paginas_a_recorrer + 1):
        url = URL_BASE.format(pagina)
        print(f"Escaneando página {pagina}: {url}...")

        # 1. Descargar el contenido HTML de la página
        respuesta = requests.get(url)
        
        # Verificar que la página cargó bien (código 200 = OK)
        if respuesta.status_code != 200:
            print(f"Error al acceder a la página {pagina}. Código: {respuesta.status_code}")
            continue

        # 2. Analizar el HTML con BeautifulSoup (forzamos UTF-8 para evitar símbolos raros en la moneda)
        respuesta.encoding = "utf-8"
        sopa = BeautifulSoup(respuesta.text, "html.parser")

        # 3. Buscar todos los bloques de productos en la página (cada libro está en una etiqueta <article class="product_pod">)
        productos = sopa.find_all("article", class_="product_pod")

        for producto in productos:
            # Extraer el título completo desde el atributo 'title' del enlace dentro de <h3>
            titulo = producto.h3.a["title"]

            # Extraer el precio y limpiar el símbolo de libra (£) para dejarlo como número
            precio_texto = producto.find("p", class_="price_color").text
            precio_limpio = float(precio_texto.replace("£", "").strip())

            # Extraer el estado de disponibilidad (ej. "In stock")
            disponibilidad = producto.find("p", class_="instock availability").text.strip()

            # Guardar los datos estructurados en un diccionario
            lista_libros.append({
                "Pagina": pagina,
                "Titulo": titulo,
                "Precio_GBP": precio_limpio,
                "Disponibilidad": disponibilidad
            })

    return lista_libros

def guardar_en_csv(datos, nombre_archivo="reporte_precios.csv"):
    """Guarda la lista de diccionarios en un archivo CSV listo para abrir en Excel."""
    if not datos:
        print("No se encontraron datos para guardar.")
        return

    # Encabezados de las columnas (toman las llaves del primer diccionario)
    columnas = datos[0].keys()

    # utf-8-sig asegura que Excel en Windows reconozca bien los acentos y símbolos
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(datos)

    print(f"\n¡Éxito! Se guardaron {len(datos)} productos en '{nombre_archivo}'.")

if __name__ == "__main__":
    print("Iniciando extracción de precios...\n")
    datos_extraidos = extraer_libros(paginas_a_recorrer=3)
    guardar_en_csv(datos_extraidos)