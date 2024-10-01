import streamlit as st
import pandas as pd
from tensorflow.keras.models import model_from_json
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Carregue seu modelo treinado
with open('Musical_Instruments_5.json', 'r') as json_file:
    json_model = json_file.read()

model = model_from_json(json_model)
model.load_weights('cnn_model.h5')
# Função para pré-processar o texto
def preprocess_text(text):
    return text.lower()

# Função para prever o sentimento
def predict_sentiment(text):
    processed_text = preprocess_text(text)
    X = np.array([processed_text])
    prediction = model.predict(X)
    return 'Positivo' if prediction[0][0] >= 0.5 else 'Negativo'

st.title('Classificador de Sentimentos de Avaliações de Produtos')
st.write("Insira sua avaliação abaixo:")
user_input = st.text_area("Avaliação:")

if st.button('Classificar'):
    if user_input:
        sentiment = predict_sentiment(user_input)
        st.write(f"Sentimento previsto: **{sentiment}**")
    else:
        st.write("Por favor, insira uma avaliação.")

