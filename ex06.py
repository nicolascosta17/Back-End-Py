import streamlit as st

# Os ícones podem ser copiados da página https://emojipedia.org/
# Configuração da página
st.set_page_config(page_title="Calculadora Simples", layout="wide")

st.title("🖩Calculadora Simples")

# Criando checkboxes na sidebar para escolher as operações
st.sidebar.header("Escolha as operações:")
soma = st.sidebar.checkbox("Soma")
subtracao = st.sidebar.checkbox("Subtração")
multiplicação = st.sidebar.checkbox("Multiplicação")
divisao = st.sidebar.checkbox("Divisão")

# Entrada de números pelo usuário
st.write("### 🖩Insira os números para o cálculo:")
num1 = st.number_input("Digite o primeiro número:", value=0.0, step=0.1)
num2 = st.number_input("Digite o segundo número:", value=0.0, step=0.1)

#Exibindo os resultados com base na seleção do usuário
st. write("### 📌 Resultado:")

if soma:
    resultado = num1 + num2
    st.write("☑ **Soma:** {} + {} = {}".format(num1, num2, resultado))

if subtracao:
    resultado = num1 - num2
    st.write("☑ **Subtração:** {} - {} = {}".format(num1, num2, resultado))

if multiplicação:
    resultado = num1 * num2
    st.write("☑ **Multiplicação:** {} X {} = {}".format(num1, num2, resultado))

if divisao:
    if num2 != 0:
        resultado = num1 / num2
        st.write("☑ **Divisão:** {}  {} = {}".format(num1, num2, resultado))
    else:
        st.write("⚠️**Erro:** Divisão por zero não é permitida.")

st.write("👈🏾 ** Selecione as operações na barra lateral. **")
