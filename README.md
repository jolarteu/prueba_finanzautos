# Proyecto de Análisis y Resumen de Comentarios de Vehículos

## Descripción

Este proyecto realiza scraping de reseñas de vehículos y utiliza técnicas de inteligencia artificial para analizar y resumir los comentarios. Las reseñas se extraen de la web y se procesan para generar resúmenes y análisis de las opiniones de los usuarios.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **pandas**: Librería para la manipulación y análisis de datos.
- **numpy**: Librería para operaciones numéricas.
- **requests**: Librería para hacer solicitudes HTTP.
- **BeautifulSoup**: Librería para el análisis de HTML y scraping.
- **langchain_community**: Librería para procesamiento de lenguaje natural y generación de resúmenes.
- **Ollama**: Modelo de lenguaje para generar resúmenes de texto.

## Requisitos

Asegúrate de tener instalado Python y las siguientes dependencias. También necesitas tener un servidor local de Ollama con el modelo `llama3` en funcionamiento. Puedes instalar todas las dependencias necesarias utilizando el archivo `requirements.txt`.

### Instalación

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/jolarteu/prueba_finanzautos.git
    cd prueba_finanzautos
    ```

2. **Crea un entorno virtual (opcional pero recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura y ejecuta el servidor Ollama con llama3:**

    Asegúrate de que tienes Ollama instalado y ejecutando localmente con el modelo `llama3`. Consulta la [documentación de Ollama](https://ollama.com/docs) para detalles sobre la instalación y configuración.

## Uso

1. **Ejecuta el script para obtener y analizar reseñas:**

    Ejecuta el script de scraping y análisis utilizando el comando de Django `manage.py`:

    ```bash
    python manage.py update_vehicle_data
    ```

   Este comando ejecutará el script ubicado en `myproject/cars/utils/reviews.py`, que se encarga de realizar el scraping de reseñas y generar resúmenes.

2. **Configura las variables necesarias (si es necesario):**
   - Asegúrate de que las URLs y las configuraciones específicas del proyecto estén ajustadas en el código según tus necesidades.

## Estructura del Proyecto

- `myproject/cars/utils/reviews.py`: El script para realizar el scraping y análisis.
- `requirements.txt`: Lista de dependencias del proyecto.
- `media/`: Carpeta para almacenar imágenes (si corresponde).
- `static/`: Carpeta para almacenar archivos estáticos (si corresponde).

## Técnicas de Inteligencia Artificial Utilizadas

- **Generación de Resúmenes**: Utiliza el modelo de lenguaje Ollama para analizar y resumir los comentarios de los usuarios. El modelo genera un resumen coherente de las reseñas, destacando los puntos clave y las opiniones más frecuentes.

