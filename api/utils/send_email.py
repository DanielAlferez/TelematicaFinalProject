import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send(autor,titulo,cuerpo_email):
    try:
        # Configuración del servidor SMTP y credenciales
        smtp_host = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'jajasjojos15@gmail.com'
        smtp_password = 'tnuvlzqcrzodxfwk'

        # Crear objeto de mensaje
        mensaje = MIMEMultipart()
        mensaje['From'] = 'Remitente' 
        mensaje['To'] = autor
        mensaje['Subject'] = titulo

        # Cuerpo del correo
        cuerpo = cuerpo_email
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        # Iniciar conexión SMTP y enviar correo
        with smtplib.SMTP(smtp_host, smtp_port) as servidor:
            servidor.starttls()
            servidor.login(smtp_username, smtp_password)
            servidor.send_message(mensaje)

        print('Correo enviado exitosamente.')
    except Exception as e:
        print(str(e))
        return None