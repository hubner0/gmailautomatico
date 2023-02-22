#Iportando
from PySimpleGUI import PySimpleGUI as sg
import smtplib
import email.message

#usando PysimpleGUI
sg.theme('NeutralBlue')
fonte = ('Helvetica',16)
layout = [
    [sg.Text('Gmail Automático',font='Helvetica, 30',justification='center',pad=(300,0))],
    [sg.Text('De:',font=fonte), sg.Input(key='from',size=35)],
    [sg.Text('Para:',font=fonte), sg.Input(key='to',size=35)],
    [sg.Text('Senha:',font=fonte), sg.Input(key='password', password_char='*',size=35)],
    [sg.Text('Assunto:',font=fonte), sg.Input(key='subject',size=35)],
    [sg.Text('Corpo do Email',font=fonte), sg.Input(key='corpoemail',pad=((0,0),(10,0)))],
    [sg.Button('Enviar',font=fonte,size=20)],
    [sg.Text('Feito por © , Hubner', justification='center', pad=(400,0))]
]

#codigo do gmail automatico
def enviar_email(from_addr, to_addr, password, subject, body):
    try:
        #puxando informações
        msg = email.message.Message()
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(body)
        
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Faz login no seu email
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    except Exception as e:
        sg.popup('Ocorreu um erro ao enviar o email:', str(e), icon='gmail.ico') #mensagem de erro

#mais MysimpleGUI
janela = sg.Window('Gmail Automático', layout)
janela.set_icon('gmail.ico')
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enviar':
        from_addr = valores['from']
        to_addr = valores['to']
        password = valores['password']
        subject = valores['subject'] #recupera o valor do campo de entrada do assunto
        body = valores['corpoemail']
        enviar_email(from_addr, to_addr, password, subject, body)
        sg.popup('E-mail enviado com sucesso!',icon='gmail.ico') #mensagem de sucesso

janela.close()
