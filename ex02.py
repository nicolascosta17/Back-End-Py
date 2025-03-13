import streamlit as st

st.title("Fazendo Soma")

#Entrada de dados
num1 = st.number_input("Digite o primeiro número: ", value=0.0, step=0.1)
num2 = st.number_input("Digite o segundo número: ", value=0.0, step=0.1)

#Botão para calcular a soma
if st.button("Somar"):
    resultado = num1 + num2
    st.success("O resultado da soma é: {}".format(resultado))
    
