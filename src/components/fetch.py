import streamlit as st

def front_up():
    html_temp = """
		<script src="https://code.iconify.design/1/1.0.7/iconify.min.js"></script>
		<div style="background-color:#8489a4;padding:10px">
		<h1 style="color:white;text-align:center;">NLP para el lenguaje español</h1>
		<h4 style="color:white;text-align:center;">Tareas de NLP en español...</h4>
		<span class="iconify" data-icon="fa-solid:home"> icono </span>
		</div>
		<br></br>
		<br></br>
	"""
    st.markdown(html_temp,unsafe_allow_html=True)
