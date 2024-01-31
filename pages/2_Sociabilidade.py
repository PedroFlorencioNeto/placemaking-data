import pandas as pd
import streamlit as st

# configurando fonte da pagina de inicio
with open( "./style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

container = st.container(border=True)

# grafico de pessoas observadas nos espacos (DataWrapper)
iframe_pessoas = """<iframe title="Número de Pessoas Observadas por Hora e por Espaço" aria-label="Interactive area chart" id="datawrapper-chart-vRcEy" src="https://datawrapper.dwcdn.net/vRcEy/5/" scrolling="no" frameborder="0" style="border: none;" width="600" height="400" data-external="1"></iframe>"""

# Execute your app
container.markdown(iframe_pessoas, unsafe_allow_html=True)

with st.expander("**Comentário**"):
    st.write("""
             A calçada é uma área frequentemente utilizada ao longo dos dias úteis, mas nos finais de semana, observa-se um aumento expressivo, chegando a ser quatro vezes maior em termos de visitantes. 
             Além disso, nota-se um acréscimo significativo no fluxo de pessoas no vão durante o intervalo de 12h às 13h. 
             """)

