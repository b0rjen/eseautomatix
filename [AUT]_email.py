import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

#configuración del email

sender_email = "borjaramosoliva@gmail.com"
receiver_email = "borjaramos@outlook.com"
subject = "Prueba de email"
message = "Hola, esto es una prueba de email"

# Crear un objeto multiparte para el mensaje

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Añadir el mensaje al objeto multiparte

msg.attach(MIMEText(message, 'plain'))

# configuración del smtp
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = os.getenv("smtp_username")
smtp_password = os.getenv("smtp_password")

# Crear una conexión segura con el servidor smtp

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email enviado correctamente")