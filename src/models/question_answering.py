import streamlit as st

from ..components.fetch import *

from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
#Se carga el modelo destilado de BETO en español con fine tuning en la dataset de squad2 en español
the_model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
tokenizer = AutoTokenizer.from_pretrained(the_model, do_lower_case=False)
model = AutoModelForQuestionAnswering.from_pretrained(the_model)

nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

#Inferencia de Sistema de Preguntas y Respuestas
def get_answer(question,context):
    output = nlp({'question':question, 'context':context}) 
    answer = output['answer']
    return answer

def main():
    front_up()
    st.title('Sistema Inteligente de Preguntas y Respuestas usando el modelo de BETO destilado')
    context  = st.text_area(label="Ingrese el texto a analizar", height=250)
    question  = st.text_area(label="Ingrese pregunta sobre el texto")
    if st.button("Cargar modelo"):
        answer_qa = get_answer(question,context)
        #print (answer_qa)
        st.text("La respuesta del Sistema es:")
        st.write(answer_qa)


