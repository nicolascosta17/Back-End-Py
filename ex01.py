#Importa a biblioteca Streamlit para criar a aplicação web
import streamlit as st

#Define um título para a aplicação
st.title("Entrada do Usuário")

#Cria um campo de entrada de texto para o usuário digitar seu nome
nome = st.text_input("Digite o seu nome: ")

#Se o usuário digitou um nome, exibe uma mensagem personalizada
if nome:
    st.write(f"Olá, {nome}!")

#Cria um controle deslizante (slider) para escolher um número entre 1 e 100
numero - st.slider("Escolha um número", 1, 100)

#Exibe o número escolhido pelo usuário
st.write(f"Você escolheu o {numero}.")
