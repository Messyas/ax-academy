import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

# definir variaveis, como o corpo do email, titulo e destinatario
GMAIL_USER = os.getenv('GMAIL_USER')
SENHA = os.getenv('GMAIL_PWD')
#anderson.fontoura@ifam.edu.br
DESTINATARIOS = ['teriorgamer@gmail.com', 'takanamessy@gmail.com', 'anderson.fontoura@ifam.edu.br']
ASSUNTO = 'teste de bot do gmail'



CORPO_TEXTO = """\
E ai malandro!!!

Teste de hacker aqui, perdeu

Att,

Hacker doidão
"""

#ANEXO = None
ANEXO = r'C:\Users\Turma01\Documents\messyas\ax-lg\02-playright\webscrap\noticias.json'
CAMINHO_IMG = r'C:\Users\Turma01\Downloads\zoro4.jfif'

arquivos_para_anexar = [CAMINHO_IMG, ANEXO]

# funcoes necessarias do bot
# 1. criar a msg
# 2. carregar o anexo
# 3. enviar o email

def criar_msg():
    # opcional
    msg = MIMEMultipart('alternative')

    msg['Subject'] = ASSUNTO
    msg['From'] = GMAIL_USER
    msg['To'] = ", ".join(DESTINATARIOS)

    msg.attach(MIMEText(CORPO_TEXTO, 'plain', 'utf-8'))

    return msg

def carregar_anexo(msg, path):
    # abrir o arquivo em formato binario
    with open(path, 'rb') as f:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(f.read())
    #criptofra o arquivo
    encoders.encode_base64(parte)
    #definir nome do arquivo
    nome_arquivo = os.path.basename(path)
    parte.add_header(
        'Content-Disposition',
        f"attachment; filename='{nome_arquivo}'"
    )

    msg.attach(parte)
    print(f'anexo adicionado: {nome_arquivo}')

def enviar_email(msg):
    print("Tentando se conectar no Gmail...")
    #porta diferente por causa do tipo critografado dos dados
    with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
        servidor.ehlo() #metodo de handskake entre cliente e servidor
        servidor.starttls() #criptografar a comunicacao
        servidor.login(GMAIL_USER, SENHA)
        print(f"Conectado: {GMAIL_USER}")
        servidor.sendmail(
            from_addr=GMAIL_USER,
            to_addrs=DESTINATARIOS,
            msg=msg.as_string()
        )
    print(f'Mensagem enviada com sucesso aos {DESTINATARIOS}')

def main():
    if not GMAIL_USER or not SENHA:
        print("Erro de autenticacao!")
        return
    print('Montando a mensagem...')
    msg = criar_msg()
    if ANEXO:
        for caminho in arquivos_para_anexar:
            if caminho:  # Verifica se não está vazio
                carregar_anexo(msg, caminho)
    enviar_email(msg)

if __name__ == '__main__':
    main()

#1. Tentar enviar anexo como imagem e o noticiar.json que criamos no outro bot

#2. Adicione multiplos destinatarios e tente usar um corpo de email em html (so pa ri)

#3. combime o scraper da aula passada onde, apos raspar 3 paginas, envie um email
# com o top 5 noticias em um corpo de html, com o titulo e link das noticias e o json apenas com essas 5 noticias.

#4. implemente os campos CC e CCO (msg['Cc'] e msg['Bcc']) e passe todos os enderecos como uma lista no parametro
# to_addrs no metodo sendmail().


