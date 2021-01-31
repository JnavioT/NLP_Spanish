import streamlit as st

from ..components.fetch import *

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

# Se carga el modelo Multilenguaje BERT con fine tuning en sentiment analysis
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

#Inferencia del Sistema de Analisis de Sentimientos
def get_answer(context):
  answer = classifier(context)
  return answer[0]['label'][0]

def main():
  front_up()
  st.title('Sistema de Analisis de Sentimientos')
  context  = st.text_area(label="Ingrese el texto a analizar")
  if st.button("Cargar modelo"):
      answer_sa = get_answer(context)
      st.text("La predicción del sentimiento es:")
      st.write(answer_sa + " estrellas")
