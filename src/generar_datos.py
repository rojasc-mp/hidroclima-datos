"""Genera un conjunto de datos de ejemplo: mediciones horarias
de temperatura y humedad de un sensor durante 30 dias."""
import numpy as np
import pandas as pd
# Semilla fija: cada ejecucion produce exactamente los mismos numeros
rng = np.random.default_rng(seed=2026)
horas = pd.date_range("2026-03-01 00:00", periods=30 * 24, freq="h")
n = len(horas)
tiempo = np.arange(n)
# Temperatura: ciclo diario + ruido; humedad: inversamente relacionada
temperatura_c = 18 + 6 * np.sin(2 * np.pi * tiempo / 24) + rng.normal(0, 0.8, n)
humedad_pct = 60 - 1.5 * (temperatura_c - 18) + rng.normal(0, 3, n)
humedad_pct = np.clip(humedad_pct, 20, 95)
# Simular un 2 % de valores faltantes en la humedad
faltantes = rng.random(n) < 0.02
humedad_pct[faltantes] = np.nan
datos = pd.DataFrame({
"fecha_hora": horas,
"sensor_id": "S01",
"temperatura_c": temperatura_c.round(2),
"humedad_pct": humedad_pct.round(1),
})
datos.to_csv("data/ejemplo.csv", index=False)
print(f"Se generaron {n} filas en data/ejemplo.csv")