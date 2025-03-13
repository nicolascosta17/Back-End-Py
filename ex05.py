import streamlit as st

#Configuração da página
st.set_page_config(page_title="Benefícios para Funcionários", layout="wide")

st.title("Consulta de Benefícios para Funcionários")

#Criando um selectbox na sidebar para escolher um cargo
cargo = st.sidebar.selectbox(
    "Selecione um cargo:",
    ["Analista", "Gerente", "Diretor", "Estagiário"]
)

#Exibindo informações conforme a escolha do usuário
st.write ("###Cargo: {}".format(cargo))

if cargo == "Analista":
    st.write("""
    - Plano de saúde e odontológico
    - Vale-refeição e vele-transporte
    - Participação nos lucros
""")

elif cargo == "Gerente":
    st.write("""
    - Todos os benefícios do Analista
    - Bônus anual por desempenho
    - Auxlio-educação para cursos de especialização
""")

elif cargo == "Diretor":
    st.write("""
    - Todos os benefícios do Gerente
    - Plano de previdência privada
    - Carro corporativo e despesas de viagem
""")

elif cargo == "Estagiário":
    st.write("""
    - Bolsa-auxilio mensal
    - Vale-transporte
    - Cursos e treinamentos internos
""")

st.write (" ** Use a barra lateral para selecionar um cargo e ver os benefícos.**")
