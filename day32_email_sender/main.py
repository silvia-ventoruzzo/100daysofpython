import smtplib
import os
import pandas as pd

os.chdir('day32_email_sender/')

providers_smtp = {'gmail':'smtp.gmail.com',
                  'hotmail':'smtp.live.com',
                  'outlook':'outlook.office365.com',
                  'yahoo':'smtp.mail.yahoo.com',
                  'aol':'smtp.aol.com'}

sender = pd.read_csv('sender_email.csv')
sender['provider'] = sender['email'].str.split('@')[0][1].split('.')[0]
sender['smtp'] = sender['provider'].map(providers_smtp)

connection = smtplib.SMTP_SSL(host=sender['smtp'].item())
connection.connect()
connection.starttls()
connection.login(user=sender['email'].item(),
                 password=sender['password'].item())
# Stopped because currently no found solution has worked