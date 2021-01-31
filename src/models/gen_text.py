import streamlit as st

from ..components.fetch import *

from transformers import AutoModelWithLMHead, AutoTokenizer
model = AutoModelWithLMHead.from_pretrained("xlnet-base-cased")
tokenizer = AutoTokenizer.from_pretrained("xlnet-base-cased")

#TEXTO PADDING ayuda al modelo a generar texto coherente
PADDING_TEXT = """In 1991, the remains of Russian Tsar Nicholas II and his family
(except for Alexei and Maria) are discovered.
The voice of Nicholas's young son, Tsarevich Alexei Nikolaevich, narrates the
remainder of the story. 1883 Western Siberia,
a young Grigori Rasputin is asked by his father and a group of men to perform magic.
Rasputin has a vision and denounces one of the men as a horse thief. Although his
father initially slaps him for making such an accusation, Rasputin watches as the
man is chased outside and beaten. Twenty years later, Rasputin sees a vision of
the Virgin Mary, prompting him to become a priest. Rasputin quickly becomes famous,
with people, even a bishop, begging for his blessing. <eod> </s> <eos>"""

#Inferencia del Sistema de generacion de texto, por el momento en ingles
def get_answer(text):
    prompt = text
    inputs = tokenizer.encode(PADDING_TEXT + prompt, add_special_tokens=False, return_tensors="pt")
    prompt_length = len(tokenizer.decode(inputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True))
    outputs = model.generate(inputs, max_length=250, do_sample=True, top_p=0.95, top_k=60)
    generated = prompt + tokenizer.decode(outputs[0])[prompt_length:]
    return generated

#texto = "As far as I am concerned, I will"
#texto = "Somewhere over the rainbow "
#print(get_answer(texto))

def main():
    front_up()
    st.title('Sistema de Generacion de texto')
    context  = st.text_area(label="Ingrese el texto base:")
    if st.button("Cargar modelo"):
        answer_gen_text = get_answer(context)
        st.text("El texto generado es:")
        st.write(answer_gen_text)