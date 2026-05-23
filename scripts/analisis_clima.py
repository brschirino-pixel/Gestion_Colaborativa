"""
Script de análisis de datos climáticos
Trabajo Práctico - Organización Empresarial
Alumna: Brisa Chirino
Escenario A: Análisis de Datos Climáticos
"""

import csv
import matplotlib.pyplot as plt

# ============================================
# CONFIGURACIÓN DE RUTAS (rutas relativas)
# ============================================

ruta_csv = "datos/annual.csv"                              # Archivo de datos de entrada
ruta_resultado = "resultados/resumen_climatico.txt"        # Resultados numéricos
ruta_grafico = "resultados/grafico_temperatura.png"        # Gráfico de salida

# ============================================
# INICIALIZACIÓN DE LISTAS
# ============================================

años = []            # Almacenará los años extraídos del CSV
temperaturas = []    # Almacenará las temperaturas correspondientes

# ============================================
# LECTURA Y PROCESAMIENTO DEL ARCHIVO CSV
# ============================================

with open(ruta_csv, "r", encoding="utf-8") as archivo:

    lector = csv.reader(archivo)
    encabezado = next(lector)  # Saltar la primera fila (encabezados)

    # Recorrer cada fila del archivo
    for fila in lector:
        # Validar que la fila tenga al menos 3 columnas
        if len(fila) < 3:
            continue  # Saltar filas incompletas

        try:
            # Columna 1 (índice 1) = Año
            años.append(int(fila[1]))
            # Columna 2 (índice 2) = Temperatura
            temperaturas.append(float(fila[2]))

        except ValueError:
            # Si no se puede convertir a número, saltar esta fila
            continue

# ============================================
# VALIDACIÓN DE DATOS (evita división por cero)
# ============================================

if len(temperaturas) == 0:
    print("ERROR: No se encontraron datos válidos en el archivo CSV")
    print("Verifique que el archivo tenga números en las columnas correspondientes.")
    exit()       # Salir del programa si no hay datos válidos

# ============================================
# CÁLCULO DE INDICADORES ESTADÍSTICOS
# ============================================

promedio = sum(temperaturas) / len(temperaturas)   # Temperatura promedio
maxima = max(temperaturas)                         # Temperatura máxima
minima = min(temperaturas)                         # Temperatura mínima

# ============================================
# GENERACIÓN DEL INFORME DE RESULTADOS
# ============================================

resultado = f"""
RESULTADOS DEL ANALISIS CLIMATICO

Temperatura promedio: {round(promedio, 2)}
Temperatura maxima: {maxima}
Temperatura minima: {minima}
"""

# Mostrar en pantalla
print(resultado)

# Guardar en archivo de texto
with open(ruta_resultado, "w", encoding="utf-8") as archivo:
    archivo.write(resultado)

# ============================================
# GENERACIÓN DEL GRÁFICO DE TEMPERATURA
# ============================================

plt.figure(figsize=(10, 5))                 # Tamaño del gráfico (ancho=10, alto=5) 
plt.plot(años, temperaturas)                # Gráfico de líneas: años vs temperaturas
plt.title("Evolucion de temperatura")       # Título del gráfico
plt.xlabel("Año")                           # Etiqueta del eje X
plt.ylabel("Temperatura")                   # Etiqueta del eje Y

# Guardar el gráfico como imagen PNG
plt.savefig(ruta_grafico)
print("Gráfico guardado correctamente.")