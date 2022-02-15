#!/usr/bin/python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login("cyrus123live@gmail.com", "kukjzafzeyirxvvz")

# create a message
msg = MIMEMultipart()

# add in the actual person name to the message template
message = ""
with open("message.txt", 'r', encoding='utf-8') as f:
    message = Template(f.read()).substitute(PERSON_NAME="Cyrus")

# setup the parameters of the message
msg['From']="cyrus123live@gmail.com"
msg['To']="cyrus123live@gmail.com"
msg['Subject']="Sending email using code"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)

del msg
