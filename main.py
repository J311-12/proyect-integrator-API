import requests
import io
import pandas as pd

def descargar_datos(url):
  # Realizando un GET request a la url especificada
  response = requests.get(url)

  # Obteniendo el contenido de la respuesta
  contenido = response.content

  # Creando un archivo de texto plano con extensión csv
  with io.open("datos.csv", "w", encoding="utf-8") as archivo:
    # Escribimos el contenido de la respuesta en el archivo
    archivo.write(contenido.decode("utf-8"))

  # Devolviendo el nombre del archivo creado
  return "datos.csv"


# Descargando los datos y obteniendo el nombre del archivo creado
nombre_archivo = descargar_datos("https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv")

# Imprimiendo el nombre del archivo creado
print(nombre_archivo)


# Convertiendo el archivo csv a un DataFrame de Pandas
df = pd.read_csv("datos.csv")

# Imprimiendo el DataFrame
print(df.head())


# Separando el DataFrame en dos, uno con las personas que perecieron y otro con el complemento
df_muertos = df[df["is_dead"] == 1]
df_vivos = df[df["is_dead"] == 0]

# Calculando los promedios de las edades de cada dataset
promedio_edad_muertos = df_muertos["age"].mean()
promedio_edad_vivos = df_vivos["age"].mean()

# Imprimiendo los promedios de edad
print(promedio_edad_muertos)
print(promedio_edad_vivos)
