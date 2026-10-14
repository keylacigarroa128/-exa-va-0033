# Keyla Paola NC = 0033
import sys
import os
import pandas as pd
import importlib.util
import io

print("Keyla Paola Machine Learning pandas, NC 0033")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Keyla Paola Machine Learning pandas, NC 0033"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# Cargar 'dicc-0033.py' que está en la raíz
ruta_dicc = os.path.join(os.path.dirname(__file__), 'dicc-0033.py')

spec = importlib.util.spec_from_file_location("dicc_0033", ruta_dicc)
dicc_0033 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dicc_0033)

# 1. Convertir diccionario a DataFrame usando datos_habitaciones
df = pd.DataFrame(dicc_0033.datos_habitaciones)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Precio_noche)
registrar("3. Estadísticas Generales de la Columna 'Precio_noche'", df['Precio_noche'].describe())

# 4. Ordenar Ascendente por Precio_noche
df_asc_precio = df.sort_values(by="Precio_noche", ascending=True)
registrar("4. Ordenar Ascendente por Precio_noche", df_asc_precio)

# 5. Ordenar Descendente por Capacidad
df_desc_capacidad = df.sort_values(by="Capacidad", ascending=False)
registrar("5. Ordenar Descendente por Capacidad", df_desc_capacidad)

# 7. Guardar el archivo resultados-ml-0033.md dentro de la carpeta resultados-0033
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resultados-0033'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0033.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Keyla Paola Machine Learning pandas, NC 0033")
print("Keyla Paola Machine Learning, NC 0033")
