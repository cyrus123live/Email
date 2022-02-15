#!/usr/bin/python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login("cyrus123live@gmail.com", "kukjzafzeyirxvvz")

# add in the actual person name to the message template
message = input("Please enter message: ")
subject = input("Please enter subject: ")
recipient = input("Please enter recipient: ")

msg = MIMEMultipart()

if (recipient == "Cyrus"):
    msg['To'] = "cyrus123live@gmail.com"
elif (recipient == "Michael"):
    msg['To'] = "michaeljschmidt13@gmail.com"
else:
    msg['To'] = recipient

# setup the parameters of the message
msg['From']="cyrus123live@gmail.com"
msg['Subject']=subject

msg.attach(MIMEText(message, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)

s.quit()
del msg
