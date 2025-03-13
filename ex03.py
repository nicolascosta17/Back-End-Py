import streamlit as st

st.title("Escolha uma opção")

#Criando opções para o usuário selecionar
opcao = st.radio(
    "Selecione uma fruta favorita:",
    ("Maçã🍎", "Banana🍌", "Laranja🍊", "Uva🍇",)
)

#Exibe a escolha do usuário
st.write("Você escolheu: {}".format(opcao))
