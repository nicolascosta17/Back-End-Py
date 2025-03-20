from datetime import datetime
import time

#Significa loop infinito 
while True:
    #Pedando data e hora atuais
    agora = datetime.now()
    print("Data e Hora Atuais: ", agora)

    #Formatando data e hora
    formatando = agora.strftime("%d/%m/%Y %H:%M:%S")
    print("Formato: ", formatando)
    time.sleep(1)
