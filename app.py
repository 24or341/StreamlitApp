import streamlit as st

st.title('Formulario Simple')

nombre = st.text_input('Nombre')

edad = st.number_input('Edad', min_value=0)

genero = st.selectbox('Género', ['Masculino', 'Femenino', 'Otro'])

if st.button('Enviar'):
    st.write(f'Nombre: {nombre}')
    st.write(f'Edad: {edad}')
    st.write(f'Género: {genero}')
