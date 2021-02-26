import streamlit as st

from ..components.fetch import *
from .translation import *

from transformers import BertTokenizerFast, EncoderDecoderModel
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#Se carga el modelo mini2bert con fine tuning en cnn_daily_mail
tokenizer = BertTokenizerFast.from_pretrained('mrm8488/bert-mini2bert-mini-finetuned-cnn_daily_mail-summarization')
model = EncoderDecoderModel.from_pretrained('mrm8488/bert-mini2bert-mini-finetuned-cnn_daily_mail-summarization').to(device)

#Inferencia del modelo de Sumarizacion, por el momento en ingles.
def get_answer(text):
    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)
    output = model.generate(input_ids, attention_mask=attention_mask)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def main():
    front_up()
    st.title('Sistema de Sumarizacion de texto')
    context  = st.text_area(label="Ingrese el texto a resumir", height=320)
    if st.button("Cargar modelo"):
        context2 = get_answer_es_en(context)
        answer_summ = get_answer(context2)
        answer_summ2 = get_answer_en_es(answer_summ)
        st.text("El resumen del texto es:")
        st.write(answer_summ2)
