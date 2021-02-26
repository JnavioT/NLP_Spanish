import streamlit as st
from ..components.fetch import *


from transformers import MarianTokenizer, MarianMTModel
from typing import List

src = 'en'  # lenguaje de origen 
trg = 'es'  # lenguaje objetivo
mname = f'Helsinki-NLP/opus-mt-{src}-{trg}'
model = MarianMTModel.from_pretrained(mname)
tok = MarianTokenizer.from_pretrained(mname)

src2 = 'es'  # lenguaje de origen 
trg2 = 'en'  # lenguaje objetivo
mname2 = f'Helsinki-NLP/opus-mt-{src2}-{trg2}'
model2 = MarianMTModel.from_pretrained(mname2)
tok2 = MarianTokenizer.from_pretrained(mname2)

#Inferencia del modelo de translación Ingles Español
def get_answer_en_es(text):
    batch = tok.prepare_seq2seq_batch(src_texts=[text], return_tensors="pt")  # don't need tgt_text for inference
    gen = model.generate(**batch)  # for forward pass: model(**batch)
    words: List[str] = tok.batch_decode(gen, skip_special_tokens=True)  # returns "Where is the bus stop ?"
    return words[0]
#print(get_answer('I am Jose'))

def get_answer_es_en(text):
    batch = tok2.prepare_seq2seq_batch(src_texts=[text], return_tensors="pt")  # don't need tgt_text for inference
    gen = model2.generate(**batch)  # for forward pass: model(**batch)
    words: List[str] = tok2.batch_decode(gen, skip_special_tokens=True)  # returns "Where is the bus stop ?"
    return words[0]

def main():
    front_up()
    st.title('Sistema de Traducción Automatica (Inglés a Español)')
    context  = st.text_area(label="Ingrese el texto a traducir", height=280)
    if st.button("Cargar modelo"):
        answer_tr= get_answer_en_es(context)
        st.text("El texto en español es:")
        st.write(answer_tr)