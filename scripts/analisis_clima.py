import csv
import matplotlib.pyplot as plt

ruta_csv = "../datos/annual.csv"
ruta_resultado = "../resultados/resumen_climatico.txt"
ruta_grafico = "../resultados/grafico_temperatura.png"

años = []
temperaturas = []

with open(ruta_csv, "r", encoding="utf-8") as archivo:

    lector = csv.reader(archivo)

    encabezado = next(lector)

    for fila in lector:

        if len(fila) < 3:
            continue

        try:
            años.append(int(fila[1]))
            temperaturas.append(float(fila[2]))

        except ValueError:
            continue

promedio = sum(temperaturas) / len(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)

resultado = f"""
RESULTADOS DEL ANALISIS CLIMATICO

Temperatura promedio: {round(promedio, 2)}
Temperatura maxima: {maxima}
Temperatura minima: {minima}
"""

print(resultado)

with open(ruta_resultado, "w", encoding="utf-8") as archivo:
    archivo.write(resultado)

plt.figure(figsize=(10, 5))

plt.plot(años, temperaturas)

plt.title("Evolucion de temperatura")
plt.xlabel("Año")
plt.ylabel("Temperatura")

plt.savefig(ruta_grafico)

print("Grafico guardado correctamente.")