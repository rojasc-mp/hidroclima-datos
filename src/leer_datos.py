"""Lee data/ejemplo.csv, calcula un resumen por dia y genera una figura.
Ejecutar desde la carpeta raiz del proyecto: python3 src/leer_datos.py"""
import pandas as pd
import matplotlib
matplotlib.use("Agg") # permite generar la figura sin abrir ventanas
import matplotlib.pyplot as plt
# Rutas relativas a la carpeta raiz del proyecto
RUTA_DATOS = "data/ejemplo.csv"
RUTA_RESUMEN = "resultados/resumen.csv"
RUTA_FIGURA = "resultados/figura_1.png"
datos = pd.read_csv(RUTA_DATOS, parse_dates=["fecha_hora"])
print(f"Filas: {len(datos)} Columnas: {list(datos.columns)}")
print("Valores faltantes por columna:")
print(datos.isna().sum())
# Resumen diario (promedio, minimo y maximo de temperatura)
datos["dia"] = datos["fecha_hora"].dt.date
resumen = datos.groupby("dia")["temperatura_c"].agg(["mean", "min", "max"])
resumen.to_csv(RUTA_RESUMEN)
print(f"Resumen guardado en {RUTA_RESUMEN}")
# Figura
fig, ax = plt.subplots(figsize=(9, 3.5))
ax.plot(datos["fecha_hora"], datos["temperatura_c"], linewidth=0.8)
ax.set_xlabel("Fecha")
ax.set_ylabel("Temperatura (grados C)")
ax.set_title("Temperatura horaria, sensor S01, marzo 2026")
fig.tight_layout()