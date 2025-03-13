import streamlit as st

#Configuração da página
st.set_page_config(page_title="Informação da Empresa", layout="wide")

st.title("Informação de Departamentos")

#Criando um menu na sidebar para seleção do departamento
departamento = st.sidebar.radio(
    "Selecione um departamento:",
    ["Recursos Humanos", "Financeiro", "Tecnologia", "Marketing"]
)

#Exibindo informação conforme a escolha do usuário
st.write("### Departamento: {}".format(departamento))

if departamento == "Recursos Humanod":
    st.write("""
    - Responsável pela gestão de pessoas na empresa.
    - Cuida do recrutamento, treinamentos e bem-estar dos funcionários.
    - Mantém a cultura organizacional e políticas internas.
    """)
