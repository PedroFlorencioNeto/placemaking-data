import streamlit as st

# configurando fonte da pagina de inicio
with open( "./style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
