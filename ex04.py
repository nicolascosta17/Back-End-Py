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

if departamento == "Recursos Humanos":
    st.write("""
    - Responsável pela gestão de pessoas na empresa.
    - Cuida do recrutamento, treinamentos e bem-estar dos funcionários.
    - Mantém a cultura organizacional e políticas internas.
    """)
elif departamento == "Financeiro":
    st.write("""
    - Gerencia os orçamentos, pagamentos e faturamento da empresa.
    - Controla os investimentos e fluxos de caixa.
    - Garante a conformidade com as regulações financeiras.
    """)
    
elif departamento == "Tecnologia":
    st.write("""
    - Responsável pelo desenvolvimento e manutenção dos sistemas internos.
    - Suporte técnico para funcionários e segurança da informação.
    - Inovação e automação de processos para eficiência operacional.
    """)

elif departamento == "Marketing":
    st.write("""
    - Cuida da estratégia de divulgação da empresa e seus produtos.
    - Planeja campanhas publicitárias e analisa o mercado.
    - Relacinamento com clientes e construção da identidade da marca.
    """)

st.write(" **Use a barra lateral para selecionar um departamento.**")
