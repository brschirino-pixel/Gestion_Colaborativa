# Gestion_Colaborativa

# ANÁLISIS DE DATOS CLIMÁTICOS

## Alumna
Brisa Chirino

## Materia
Organización Empresarial

## Trabajo Práctico
Gestión Colaborativa, Control de Versiones y Organización Empresarial (Git, GitHub y Jira)

---

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar un conjunto de datos climáticos históricos mediante Python.

A partir del procesamiento del dataset seleccionado se generan indicadores estadísticos básicos y una representación gráfica que permite observar la evolución de la temperatura a lo largo del tiempo.

---

## Objetivos

- Importar y procesar un archivo CSV con datos climáticos.
- Calcular temperatura promedio.
- Obtener temperatura máxima y mínima.
- Generar un gráfico de evolución de temperatura.
- Exportar automáticamente los resultados obtenidos.

---

## Dataset Utilizado

**Archivo:** `annual.csv`

El dataset contiene registros históricos de temperatura organizados por año y utilizados para realizar el análisis estadístico.

---

## Estructura del Proyecto

```text
GESTION_COLABORATIVA/
│
├── datos/
│   └── annual.csv
│
├── scripts/
│   └── analisis_clima.py
│
├── resultados/
│   ├── resumen_climatico.txt
│   └── grafico_temperatura.png
│
├── README.md
└── .gitignore
```

---

## Herramientas Utilizadas

- Python
- CSV
- Matplotlib
- Git
- GitHub
- Jira

---

## Resultados Generados

Al ejecutar el script se generan automáticamente:

- Un archivo de resumen con indicadores climáticos.
- Un gráfico de evolución de temperatura.

Ubicación:

```text
/resultados
```

---

## Instrucciones de Ejecución

1. Clonar el repositorio.
2. Abrir el proyecto en Visual Studio Code.
3. Acceder a la carpeta `scripts`.
4. Ejecutar:

```bash
python analisis_clima.py
```

---

## Consideraciones Técnicas

El proyecto fue desarrollado utilizando rutas relativas para garantizar su reproducibilidad y organización del código.

---

## Control de Versiones

El proyecto fue gestionado mediante Git y GitHub utilizando commits descriptivos y organización por ramas.