mail_password='isjx rqrv tibl jamb'
import smtplib 
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('stephyhallel2002@gmail.com',mail_password)
    msg=EmailMessage()
    msg['FROM']='stephyhallel2002@gmailcom'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    print('MESSAGE SENT')
    server.close()