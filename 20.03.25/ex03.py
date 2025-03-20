import streamlit as st #Importando a biblioteca Streamlit para criar a interface web
from datetime import datetime #Importando datetime para manipular datas e horários
import time #Importando time para fazer a atualização da contagem regressiva

#Definindo o título da aplicação    
st.title("Contagem Regressiva para um Evento!")

#Criando um seletor de data e hora para o usuário escolhero evento futuro
data_evento = st.date_input("Escolha a Data do Evento") #Usuário escolhe a data
hora_evento = st.time_input("Escolha o Horário do Evento") #Usuário escolhe o horário

#Criando um botão para iniciar a contagem regressiva
if st.button("Iniciar Contagem Regressiva"):
    #Convertendo a data e hora escolhida para um formato compatível
    evento_datetime = datetime.combine(data_evento, hora_evento) #Junta data e hora escolhida

    #Criando um espaço vazio para atualizar a contagem regressiva em tempo real
    contador = st.empty()

    #Loop para atualizar o tempo restante até o evento
    while True:
        agora = datetime.now() #Obtém a data e hora atuais do sistema
        diferenca = evento_datetime - agora #Calcula o tempo restante até o evento

        if diferenca.total_seconds() <= 0: #Verifica se o evento já aconteceu
            contador.success("O Evento Chegou!") #Exibe uma mensagem de celebração
            break #Sai do Loop

        #Converte a diferença para dias, horas, minutos e segundos
        dias = diferenca.days
        segundos_totais = diferenca.seconds
        horas = segundos_totais // 3600
        minutos = (segundos_totais % 3600) //60
        segundos = segundos_totais % 60

        #Exive a contagem regressiva formatada
        contador.write("Tempo restante: {} dias, {} horas, {} minutos, {} segundos".format(dias, horas, minutos, segundos))
        time.sleep(1) #Aguarda 1 segundo antes de atualizar novamente
