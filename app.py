import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import json

#Link al colab donde se usó el codigo de SPARK: https://colab.research.google.com/drive/1-Dvc5l3OVwpq8jimOemBoIG4WxAZiBfL?usp=sharing

st.title("Análisis de Autos y Consumo de Gasolina")
st.write("Este dashboard analiza datos del dataset Auto MPG.")

# Cargar archivo único JSON generado por Spark
import json

with open("resultados/resultado.json", "r") as f:
    lines = f.readlines()

data = [json.loads(line) for line in lines]
df = pd.DataFrame(data)


# Mostrar tabla
st.subheader("Consumo promedio por número de cilindros")
st.dataframe(df)

# Gráfica
fig, ax = plt.subplots()
ax.bar(df["cylinders"], df["avg(mpg)"], color="skyblue")
ax.set_xlabel("Cilindros")
ax.set_ylabel("MPG promedio")
st.pyplot(fig)
