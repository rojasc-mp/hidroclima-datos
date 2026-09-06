# Mediciones horarias de temperatura y humedad de un sensor ambiental
Conjunto de datos de ejemplo y programa minimo de lectura, preparados
como actividad del curso Topicos Avanzados del Analisis de Datos
(Doctorado en Ingenieria Aplicada). Este registro sera actualizado al
final del curso con los datos y el codigo del trabajo final.
## Contenido
- `data/ejemplo.csv`: 720 mediciones horarias (1 al 30 de marzo de 2026).
- `data/diccionario_de_datos.md`: descripcion de cada columna, unidades y valores
faltantes.
- `src/generar_datos.py`: programa que genera los datos de ejemplo (semilla fija).
- `src/leer_datos.py`: lee los datos, calcula un resumen diario y produce una figura.
- `resultados/`: archivos producidos por `leer_datos.py`.
## Procedencia de los datos
(Describa como se obtuvieron: instrumento, lugar, periodo, procesamiento
previo. Si son sinteticos, digalo explicitamente.)
## Como ejecutar
Requisitos: Python 3.9 o superior.
1. Descargar o clonar este repositorio.
2. Instalar las dependencias: `python3 -m pip install -r requirements.txt`
3. Desde la carpeta raiz del proyecto, ejecutar: `python3 src/leer_datos.py`
El programa imprime un resumen en pantalla y guarda `resultados/resumen.csv`
y `resultados/figura_1.png`.
## Licencia
- Codigo (`src/`): licencia MIT (ver archivo `LICENSE`).
- Datos y documentacion (`data/`, este archivo): Creative Commons Atribucion 4.0
Internacional (CC BY 4.0), https://creativecommons.org/licenses/by/4.0/
## Como citar
Rojas, María-Paz (2026). Mediciones horarias de temperatura y humedad de un
sensor ambiental (datos de ejemplo) (Version 1.0.0) [Conjunto de datos].
Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX
(El DOI se completara despues de publicar en Zenodo.)
## Contacto
María-Paz Rojas Castillo, m.rojasc@udd.cl.cl, ORCID: https://orcid.org/0009-0007-0671-7941