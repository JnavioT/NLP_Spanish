import streamlit as st

from ..components.fetch import *

from transformers import pipeline
ner = pipeline("ner", grouped_entities=True)

#sequence = "Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge which is visible from the window."

#Inferencia del modelo de Name Entity Recognition (ingles)
def get_answer(text):
    output = ner(text)
    answer=''
    for i in output:
        aux = ''
        if i['entity_group'] == 'PER':
            aux = 'Persona'
        elif i['entity_group'] == 'LOC':
            aux = 'Ubicación'
        elif i['entity_group'] == 'ORG':
            aux = 'Organización'
        answer += str(i['word'])+ " -> " + str(aux)+ ' ; '
    return answer
#Ejm
#text = "Sagasti is the new president of Peru. He studied at UNI."
#print(get_answer(text))

def main():
    front_up()
    st.title('Sistema de Reconocimiento de Entidades')
    context = st.text_area(label="Ingrese el texto a analizar:")
    if st.button("Cargar modelo"):
        answer_gen_ner = get_answer(context)
        st.text("Las entidades en el texto son:")
        st.write(answer_gen_ner)