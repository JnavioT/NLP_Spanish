import streamlit as st

from .fetch import *

def main():
	front_up()
	#fetch.front_up()
	st.markdown("""
            Esta es una App de Procesamiento de Lenguaje Natural (NLP) util para diversas 
            tareas de NLP implementada usando APIs de NLP sobre el Framework Streamlit
			""")

	st.header('Aplicaciones')
	st.markdown("""
			#### Preguntas y Respuestas:
			+ Copie un párrafo y haga preguntas en funcion al texto. El resultado será el texto más
			breve encontrado en el párrafo dado.
			"""
			)
	st.markdown("""
			#### Analisis de Sentimientos:
			+ Analiza el sentimiento del texto dado. El resultado varía desde 1 estrella(sentimiento
			negativo) hasta 5 estrellas (sentimiento positivo). \n
			  Por ejemplo: \n
			  El inesperado final valio la pena. 
			"""
			)
	st.markdown("""
			#### Autocompletado de Texto:
			+ Autocompleta palabras en textos con la palbra clave : [MASK]. \n
			  Por ejemplo: \n
			  [CLS] Para [MASK] los [MASK] de Perú, el presidente 
			  debe [MASK] de inmediato. [SEP]
			"""
			)
	st.markdown("""
			#### Traducción (Inglés - Español):
			+ Traduce el texto dado. Copie y pegué el texto que quiera en español.
			"""
			)
	st.markdown("""
			#### Sumarización de Texto:
			+ Sumariza el texto dado. Copie y pegué el texto que quiera sumarizar.
			"""
			)