import email.message
import pandas as pd
import smtplib
from datetime import datetime
import time
import os

def enviar_email(corpo_email):
    try:
        msg = email.message.Message() #cria variavel do email
        msg['Subject'] = 'Estoque Atualizado com Sucesso!!!' # Asssunto
        msg['From'] = 'integradorlopal@gmail.com'  # Remetente
        msg['To'] = 'integradorlopal@gmail.com'    # Destinatário
        password = 'ytrkhiuxhbolbyby'  # Senha do app, gerada do Google
        msg.add_header('Content-Type', 'text/html') #adiciona cabeçalho ao e-mail, indica que o conteudo será HTML
        msg.set_payload(corpo_email) #define corpo do email

        s = smtplib.SMTP('smtp.gmail.com: 587') # cria instância SMTP q se conecta ao Servidor SMTP do Gmail, na porta 587 que é usada para TLS
        s.starttls() #Criptografa a conexão 
        s.login(msg['From'], password) #Faz login usando o email remetente e a senha q foi gerada pelo Google
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))  # envia email formatado em utf-8
        s.quit() #Encerra Conexão com servidor SMTP
        print('Email de Relatorio diário enviado com sucesso!') #Exibe no terminal se o email for enviado
    except Exception as e: # guardar qualquer erro q ocorra no try
        print(f'Erro ao enviar email: {e}') # Exibe a Mensagem e o erro

email_enviado = False

while True:
    try:
        # Leitura do arquivo CSV e seleção dos dados
        df = pd.read_csv('LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv') #lê aerquivo
        df['Date'] = pd.to_datetime(df['Date']) #coverte a coluna Date para o tipo datime 
        hoje = datetime.today().date() #pega a data atual e coloca na variavel hoje
        df_hoje = df[df['Date'].dt.date == hoje] #filtra a coluna Date, verificando se a alguma data igual a armazenada anteriormente em hoje e depois a armazena 

        if not df_hoje.empty and not email_enviado: # se na filtragem não for encontrada uma data correspondente, a variavel df_hoje fica vazia, nesse if estamos perguntando se ela não está vasia  
            relatorio_html = df_hoje.to_html(index=False) # converte tabela em uma tabela HTML e tira o indice
            corpo_email = f"<h3>Relatório do dia {hoje}:</h3><br>{relatorio_html}" # Cria o corpo do email que é chamado la na nossa função,  nele temos um cabeçalho simples dentro do <H3> com a data um <br> para quebrar a linha  e logo depois temos nossa tabela Html
            df.to_excel("LOPAL-ProjetoIntegrador-Esp8266_Receiver.xlsx", index=False)  # Salva o arquivo como Excel
            enviar_email(corpo_email)
            email_enviado = True
        else: #caso a df_hoje esteja vazia
            print("Nenhuma atualização de estoque. Não foi enviado nenhum email!")
    except Exception as e:
        print(f'Erro ao processar arquivo: {e}') 
        
    time.sleep(60)




