import smtplib
import os
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass


#----------Sumber------------
#belajarpython.com "parsing txt"
#realpython.com/python-send-email "penggunaan modul email"
#qastack.id/programming/3362600/how-to-send-email-attachments "attachment"


# Function for list all receiver email
def list_receiver(filename):

    with open(filename, 'r') as file:
        result = [line.strip() for line in file.readlines()]
    return result

def input_users(name, password):
    return name, password

def attach_file(filename):

    attach = open(filename, 'rb').read()
    return attach

def send_email(users, receiver, attach=None):

    # setting SMTP 
    smtp_server = "smtp.gmail.com"
    port = 587
    context = ssl.create_default_context()

    # Take username and passowrd
    username = users[0]
    password = users[1]

    body = f"""\
        Ini dikirim melalu SMPT Python
        Sebagai Tugas Terakhir
    

    Terimakasih :)
    """
    html ="""\
    <html>
        <body>
            <h1>----------Pesan Html----------</h1>
            <p style="color:red;">Warna Merah</p>
        </body>
    </html>
    """
    
    part = MIMEBase('application', "octet-stream")
    part.set_payload(attach)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="pilar.jpg"')

    # Draf mail
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = ', '.join(receiver)
    msg['Subject'] = 'Final Project'

    # attach body text email
    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(html,'html'))
    msg.attach(part)
    text = msg.as_string()

    # connect to server
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(username, password)
        server.sendmail(username, receiver, text)
        print("Mail Berhasil Dikirim")

    except Exception as e:
        print(e)

    finally:
        server.quit()

def main():
    # Receiver email list
    file_receiver = 'receiver_list.txt'

    # Attach file
    file_attach = 'pilar.jpg'

    curent_path = os.path.dirname(__file__)
    file_receiver_path = os.path.join(curent_path, file_receiver)
    file_attach_path = os.path.join(curent_path, file_attach)

    receiver = list_receiver(file_receiver_path)
    attach = attach_file(file_attach_path)

    sender_email = "sulthan.a2.pilkom@gmail.com"
    password = getpass('Masukan Password: ')

    user = input_users(sender_email, password)

    send_email(users=user, receiver=receiver, attach=attach)


if __name__ == "__main__":
    main()