import smtplib
from email.message import EmailMessage
import mimetypes
import os


def enviar_email(destinatario, assunto, corpo, remetente, senha_app, anexo=None):
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    msg.set_content(corpo)

    # Se houver anexo
    if anexo and os.path.isfile(anexo):
        mime_type, _ = mimetypes.guess_type(anexo)
        mime_type = mime_type or 'application/octet-stream'
        maintype, subtype = mime_type.split('/', 1)

        with open(anexo, 'rb') as file:
            msg.add_attachment(file.read(),
                               maintype=maintype,
                               subtype=subtype,
                               filename=os.path.basename(anexo))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(remetente, senha_app)
        smtp.send_message(msg)


if __name__ == "__main__":
    enviar_email('gustavo.campos1989@gmail.com','Teste RPA','Corpo teste','rpadogrc@gmail.com','qpzh fchp lxza roko')
