import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go 
import streamlit as st
st.set_page_config(page_title="Anuncios de Coches", layout="wide")
st.header('Análisis de Anuncios de Venta de Coches')
st.write('Esta aplicación te permite explorar los datos de anuncios de coches mediante visualizaciones interactivas.')
try:
    df = pd.read_csv("vehicles_us.csv")
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encuentra. Asegúrate de que esté en el mismo directorio que 'app.py'.")
    st.stop()
st.subheader('Visualizaciones con Botones')
hist_button = st.button('Construir Histograma de Odómetro')
scatter_button = st.button('Construir Gráfico de Dispersión (Odómetro vs. Precio)', key='scatter_btn')
if hist_button:
    st.write('Creando un histograma para la distribución del odómetro.')
    fig_hist = px.histogram(df, x='odometer', title='Distribución del Odómetro')
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_button:
    st.write('Creando un gráfico de dispersión para odómetro vs. precio.')
    fig_scatter = px.scatter(df, x='odometer', y='price', title='Precio vs. Odómetro')
    st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader('Visualizaciones con Casillas de Verificación (Desafío Extra)')
build_histogram_checkbox = st.checkbox('Mostrar Histograma de Odómetro')
build_scatter_checkbox = st.checkbox('Mostrar Gráfico de Dispersión (Odómetro vs. Precio)')

if build_histogram_checkbox:
    st.write('Mostrando un histograma interactivo de la distribución del odómetro.')
    fig_hist_cb = px.histogram(df, x='odometer', title='Distribución del Odómetro')
    st.plotly_chart(fig_hist_cb, use_container_width=True)

if build_scatter_checkbox:
    st.write('Mostrando un gráfico de dispersión interactivo de precio vs. odómetro.')
    fig_scatter_cb = px.scatter(df, x='odometer', y='price', title='Precio vs. Odómetro')
    st.plotly_chart(fig_scatter_cb, use_container_width=True)

st.write('---')
st.write('¡Gracias por usar la aplicación de análisis de coches!')