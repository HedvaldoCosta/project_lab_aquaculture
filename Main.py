import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

def extract_data(dataset):
    data_raw = pd.read_csv(dataset,sep=';')
    return data_raw


dataframe = extract_data(dataset="https://raw.githubusercontent.com/HedvaldoCosta/project_lab_aquaculture/master"
                                 "/dataset/aquicultura.csv")

st.title("AQUICULTURA E ALAGOAS")

selected_products = st.sidebar.multiselect("Selecione os produtos aquáticos:", dataframe["Produto"].unique())
start_year = st.sidebar.number_input("Ano inicial:", min_value=dataframe["Ano"].min(), max_value=dataframe["Ano"].max())
end_year = st.sidebar.number_input("Ano final:", min_value=dataframe["Ano"].min(), max_value=dataframe["Ano"].max())
# Filtrando os dados
filtered_data = dataframe[(dataframe["Produto"].isin(selected_products)) & (dataframe["Ano"].between(start_year, end_year)) & (dataframe["Tipo"] == "Quantidade produzida")]
# Criando o gráfico de barras
chart = alt.Chart(filtered_data).mark_bar().encode(
    x='Ano:O',
    y='Valor/Quantidade:Q',
    color=alt.Color('Produto:N', legend=None)
).properties(
    width=600,
    height=400
)
# Exibindo o gráfico
st.altair_chart(chart, use_container_width=True)
st.dataframe(dataframe)

