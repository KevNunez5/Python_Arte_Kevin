import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import json

st.title("Análisis de Autos y Consumo de Gasolina")
st.write("Este dashboard analiza datos del dataset Auto MPG.")

# Cargar datos procesados
data = []
for file in os.listdir("resultados"):
    if file.endswith(".json"):
        with open(f"resultados/{file}") as f:
            data.append(json.load(f))

# Convertir a DataFrame
df = pd.DataFrame([x[0] for x in data])

# Mostrar tabla
st.subheader("Consumo promedio por número de cilindros")
st.dataframe(df)

# Gráfica
fig, ax = plt.subplots()
ax.bar(df["cylinders"], df["avg(mpg)"], color="skyblue")
ax.set_xlabel("Cilindros")
ax.set_ylabel("MPG promedio")
st.pyplot(fig)
