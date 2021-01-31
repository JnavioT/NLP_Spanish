import streamlit as st

def front_up():
    html_temp = """
		<script src="https://kit.fontawesome.com/yourcode.js"></script>
		<div style="background-color:#8489a4;padding:10px">
		<h1 style="color:white;text-align:center;">NLP para el lenguaje español</h1>
		<h4 style="color:white;text-align:center;">Tareas de NLP en español...</h4>
		<i class="fas fa-band-aid"></i>
		</div>
		<br></br>
		<br></br>
	"""
    st.markdown(html_temp,unsafe_allow_html=True)
