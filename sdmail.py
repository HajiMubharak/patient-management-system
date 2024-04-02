import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('shaikhajimubarak12@gmail.com','rwog lgjp gbjk ynmz')
    msg=EmailMessage()
    msg['From']='shaikhajimubarak12@gmail.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()