"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    headers = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave",
    ]

    data = []
    current_row = []
    for line in lines[4:]:

        if re.match(r"^\s+\d+", line):
            if current_row:
                data.append(current_row)
                current_row = []
            current_row = re.split(r"\s{2,}", line.strip())
            palabras_unidas = " ".join(current_row[3:])
            current_row = current_row[0:3]
            current_row.append(palabras_unidas)

        else:
            line = re.sub(r"\s{2,}", " ", line.strip())
            current_row[-1] += " " + line.strip()

    if current_row:
        data.append(current_row)

    df = pd.DataFrame(data, columns=headers)
    df["cluster"] = df["cluster"].astype(int)
    df["cantidad_de_palabras_clave"] = df["cantidad_de_palabras_clave"].astype(int)
    df["porcentaje_de_palabras_clave"] = (
        df["porcentaje_de_palabras_clave"]
        .str.replace(",", ".")
        .str.rstrip(" %")
        .astype(float)
    )
    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )
    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"].str.replace(".", "").str.strip()
    )

    return df


if "__main__" in __name__:
    pregunta_01()
