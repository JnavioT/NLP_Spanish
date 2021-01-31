import streamlit as st

from ..components.fetch import *

import torch
from transformers import BertForMaskedLM, BertTokenizer

tokenizer = BertTokenizer.from_pretrained("src/data", do_lower_case=False)
model = BertForMaskedLM.from_pretrained("src/data")

def get_tupla(context): 
    # Funcion que obtiene indices de las palabras enmascaradas ([MASK]) y 
    # los une en una tupla
    tp1 = context.split(",")
    tp2 = ""
    for i in range(len(tp1)):
        tp2 = tp2+tp1[i]+" , "
    tp2 = tp2[:-2]
    tp3 = tp2.split()
    list_i = []
    for i in range(len(tp3)):
        if tp3[i] == "[MASK]":
            list_i.append(i)
    return tuple(list_i)
def show_answer(context, list_i): 
    # Funcion que reemplaza una posible respuesta
    tp1 = context.split(",")
    tp2 = ""
    for i in range(len(tp1)):
        tp2 = tp2+tp1[i]+" , "
    tp2 = tp2[:-2]
    tp3 = tp2.split()
    result = []
    for k in range (5):
        s = ""
        j = 0
        for i in range(len(tp3)):
            if tp3[i] == "[MASK]":
                s += list_i[j][k] + " "
                j +=1
            else:
                s += tp3[i] + " "
        result.append(s)
    return result
#Inferencia de Sistema de Completado de Texto
def get_answer(context):
    text = context
    masked_indxs = get_tupla(text)
    tokens = tokenizer.tokenize(text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokens)
    tokens_tensor = torch.tensor([indexed_tokens])

    predictions = model(tokens_tensor)[0]
    list_f = []

    for i,midx in enumerate(masked_indxs):
        idxs = torch.argsort(predictions[0,midx], descending=True)
        predicted_token = tokenizer.convert_ids_to_tokens(idxs[:5])
        #print('MASK',i,':',predicted_token)
        list_f.append(predicted_token)
    return list_f

#EjmS
# [CLS] Para [MASK] los [MASK] de Perú, el presidente debe [MASK] de inmediato. [SEP]
def main():
    front_up()
    st.title('Sistema de Autocompletacion de Texto')
    context  = st.text_area(label="Ingrese el texto base")
    if st.button("Cargar modelo"):
        answer_ta = get_answer(context)
        st.text("La prediccion/generacion del Sistema es:")
        for i in show_answer(context, answer_ta):
            st.write(i)
