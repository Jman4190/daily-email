import os
from dotenv import load_dotenv
load_dotenv()
from httplib2 import Http
import smtplib

EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

#Send outbound email, to myself, subject line is constant, body
def send_email(book, quote, kt):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    #smtpObj.login('mannellyjohn@gmail.com', 'cjfjgnubxxowowwk')
    smtpObj.login('mannellyjohn@gmail.com', EMAIL_PASSWORD)
    body = 'Subject: Daily Quote\n\n %s\n %s\n %s' % (book, quote, kt)

    sendmailStatus = smtpObj.sendmail('Future John', 'mannellyjohn@gmail.com', body.encode('utf-8'))
    if sendmailStatus != {}:
        print('There was an error sending daily email to John')
    smtpObj.quit()

    print('Sending you an email now, sir.')
