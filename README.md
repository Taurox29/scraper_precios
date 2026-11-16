# scraper_precios
Script en Python que extrae títulos, precios y disponibilidad de catálogos web mediante BeautifulSoup y exporta los datos limpios a CSV/Excel.
# Monitor de Precios con Web Scraping en Python

Script automatizado en Python que recorre múltiples páginas de un catálogo web de comercio electrónico, extrae información clave de los productos (título, precio y disponibilidad) y exporta los resultados limpios a un archivo CSV listo para abrir en Excel.

## Características principales

* **Paginación automática:** Recorre de forma secuencial las páginas configuradas del catálogo sin intervención manual.
* **Limpieza de datos en tiempo real:** Extrae el texto del HTML y convierte los precios de cadena de texto a valores numéricos decimales (`float`), eliminando símbolos de moneda y espacios extra.
* **Exportación compatible con Excel:** Genera un archivo `.csv` codificado en `utf-8-sig` para garantizar que los caracteres especiales y acentos se visualicen correctamente en hojas de cálculo.

## Tecnologías utilizadas

* **Python 3**
* **Requests:** Para realizar las peticiones HTTP al servidor.
* **BeautifulSoup4:** Para analizar y navegar la estructura HTML de las páginas.
* **CSV (Módulo nativo):** Para la estructuración y guardado del reporte final.

## Instalación y uso

1. Clona este repositorio en tu computadora:
   ```bash
   git clone [https://github.com/](https://github.com/)Taurox29/scraper-precios-python.git
   cd scraper-precios-python
