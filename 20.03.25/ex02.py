import streamlit as st #Importando a biblioteca Streamlit para criar a interface web
from datetime import datetime #Impotando datetime para trabalho com data e hora
import time #Importando time para controlar a atualização do relógio

#Definindo o título da aplicação
st.title("Relógio Digital em Tempo Real")

#Criando um espaço vazio para exibir a hora (esse espaço será atualizado constantemente)
relogio = st.empty()

#Loop infinito para atuializar a hora em tempo real
while True:
    agora = datetime.now() #Obtém a data e hora atuais do sistema
    hora_formatada = agora.strftime("%H:%M:%S") #Formata a hora no formato HH:MM:SS

    relogio.title("Hora Atual: {}".format(hora_formatada)) #Exibe a hora na interface

    time.sleep(1) #Aguarda 1 segundo antes de atualizar novamente
 
