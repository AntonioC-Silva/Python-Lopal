import email.message
import pandas as pd
import smtplib
from datetime import datetime
import time

def enviar_email(corpo_email): # Dados necessários para enviar o email e tambem faz o envio
    try:
        msg = email.message.Message()
        msg['Subject'] = 'Estoque Atualizado com Sucesso!!!'
        msg['From'] = 'integradorlopal@gmail.com'
        msg['To'] = 'integradorlopal@gmail.com'
        password = 'ytrkhiuxhbolbyby'
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        s.quit()
        print('Email de Relatorio diário enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar email: {e}')

email_enviado = False

while True: #Verificação de requisitos para envio do email e geração do relatório (Loop infinito que verifica novamente os requisitos de acordo com o tempo estabelecido em time.sleep() e envia caso os requisitos sejam atendidos)
    try:
        df = pd.read_csv('LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        hoje = datetime.today().date()
        df_hoje = df[df['Date'].dt.date == hoje]

        if not df_hoje.empty:
            df.to_excel("LOPAL-ProjetoIntegrador-Esp8266_Receiver.xlsx", index=False)

            if not email_enviado:
                relatorio_html = df_hoje.to_html(index=False)
                corpo_email = f"<h3>Relatório do dia {hoje}:</h3><br>{relatorio_html}"
                enviar_email(corpo_email)
                email_enviado = True
        else:
            print("Nenhuma atualização de estoque. Não foi enviado nenhum email!")
    except Exception as e:
        print(f'Erro ao processar arquivo: {e}')

    time.sleep(60) # pode ser ajustado para a necessidade do cliente
