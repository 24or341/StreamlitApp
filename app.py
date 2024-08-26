import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Formulario Simple')

# Campos del formulario
nombre = st.text_input('Nombre')
edad = st.number_input('Edad', min_value=0)
genero = st.selectbox('Género', ['Masculino', 'Femenino', 'Otro'])

# Botón para enviar
if st.button('Enviar'):
    st.write(f'Nombre: {nombre}')
    st.write(f'Edad: {edad}')
    st.write(f'Género: {genero}')
    
    # Datos de ejemplo para la visualización
    data = {
        'Edad': [20, 25, 30, 35, 40],
        'Cantidad': [10, 20, 15, 25, 30]
    }
    
    df = pd.DataFrame(data)
    
    # Mostrar el dataframe
    st.write("Datos de ejemplo de edades:")
    st.write(df)
    
    # Crear un gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(df['Edad'], df['Cantidad'], color='lightgreen')
    ax.set_xlabel('Edad')
    ax.set_ylabel('Cantidad')
    ax.set_title('Distribución de edades en una muestra')
    
    # Mostrar el gráfico en la aplicación
    st.pyplot(fig)
