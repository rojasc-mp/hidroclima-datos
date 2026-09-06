# Diccionario de datos: ejemplo.csv
## Descripcion general
Mediciones horarias de temperatura y humedad relativa de un sensor
ambiental, entre el 1 y el 30 de marzo de 2026. 
## Columnas
| - | Columna | Tipo | Unidad | Descripcion |
|----------------|---------|--------|------------------------------------------------|
| fecha_hora | fecha | Fecha y hora de la medicion, formato AAAA-MM-DD
HH:MM:SS, hora local |
| sensor_id | texto | - | Identificador del sensor |
| temperatura_c | decimal | grados Celsius | Temperatura del aire |
| humedad_pct | decimal | % | Humedad relativa |
## Valores faltantes
Se representan como celda vacia. En humedad_pct hay un 2 % de valores
faltantes por fallas del sensor (en este ejemplo, simuladas).
## Procedencia
Datos generados sinteticamente con src/generar_datos.py (semilla 2026).