"""Modulo principal del App"""
import streamlit as st

import src.components.home
import src.models.question_answering
import src.models.sent_analysis
import src.models.masked
import src.models.translation
import src.models.summ


PAGES = {
    "Home": src.components.home,
    "Preguntas y Respuestas": src.models.question_answering,
    "Analisis de Sentimientos": src.models.sent_analysis,
    "Texto Autocompletado": src.models.masked,
    "Traducción (inglés a español)": src.models.translation,
    "Sumarización": src.models.summ,
}


def main():
    
    st.sidebar.title("NLP para el lenguaje español")
    st.sidebar.text("App de Procesamiento de Lenguaje Natural")
    
    st.sidebar.title("Navegación")
    options = list(PAGES.keys())
    page = st.sidebar.radio("Ir a", options )
    
    with st.spinner(f"Cargando {page} ..."):
        PAGES[page].main()
      
    st.sidebar.title("Acerca del App")
    if page == "Home":
        st.sidebar.info(
            """
            Esta App usa el estado del arte de modelos de Procesamiento de Lenguaje
            Natural con APIs de las librerías de Transformers de HuggingFace. Los modelos usados son
            BERT en español, distilBERT en español, BERT multilenguaje, XLNET, MarianMT
            """
        )
    elif page == "Preguntas y Respuestas":
        st.sidebar.info(
            """
            Este sistema de preguntas y respuestas utiliza el modelo de distilBERT 
            en español.
            """
        )
    elif page == "Analisis de Sentimientos":
        st.sidebar.info(
            """
            Este sistema de Analisis de Sentimientos utiliza el modelo de BERT 
            multilenguaje.
            """
        )
    elif page == "Texto Autocompletado":
        st.sidebar.info(
            """
            Este sistema de autocompletado utiliza el modelo BETO, el cual 
            tiene la misma arquitectura que BERT entrenado con el lenguaje español.
            """
        )
    elif page == "Traducción (inglés a español)":
        st.sidebar.info(
            """
            Este sistema de Traducción utiliza el modelo de MarianMT.
            """
        )
    elif page == "Sumarización":
        st.sidebar.info(
            """
            Este sistema de Sumarización utiliza el modelo de minibert con fine tuning en
            la tarea de sumarización y el modelo de Traducción de MarianMT.
            """
        )

    st.sidebar.title("Contacto")
    st.sidebar.info(
        """
            github: 
            https://github.com/JnavioT
            correo: 
            jnavio@uni.pe
        """
    )


if __name__ == "__main__":
    main()