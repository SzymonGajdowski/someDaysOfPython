import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'simonpytestuser@mail.com'
password = '******'

def sendMail(text='Email Body', subject='Hello World', fromEmail='PyTest <simonpytestuser@gmail.com>', toEmails=None, html=None):
    assert isinstance(toEmails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = fromEmail
    msg['To'] = ", ".join(toEmails)
    msg['Subject'] = subject

    txtPart = MIMEText(text, 'plain')
    msg.attach(txtPart)

    if html != None:
        htmlPart = MIMEText(html, 'html')
        msg.attach(htmlPart)

    msgStr = msg.as_string()

    # login to stmp server
    server = smtplib.SMTP(host='smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromEmail, toEmails, msgStr)

    server.quit()