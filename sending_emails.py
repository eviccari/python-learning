from ast import Try
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from smtplib import SMTPAuthenticationError, SMTP
from string import Template

message = MIMEMultipart()
message["from"] = "Eduardo Viccari"
message["to"] = "test@test.com"
message["subject"] = "Sending e-mail from python"
template = Template(Path("templates/email_template.html").read_text())
body = template.substitute({"name": "Henrique"})

message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("images/doom.png").read_bytes()))

with SMTP(host="smtp.gmail.com", port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(user="test@test.com", password="pass123")
        smtp.send_message(message)
        print("Sent...")
    except SMTPAuthenticationError as error:
        print(error)
