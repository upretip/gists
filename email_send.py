#!python3
#-*- coding: utf-8 -*-

"""
Sending email using python simple smtplib
Author: PUpreti
Date: 2019??
"""

import smtplib
from email.mime.text import MIMEText

message = "this is a test message from the smtp using python"
address = "parash.upreti@smarterbalanced.org"
add_to = ["pupreti@ucsc.edu","alex.dean@smarterbalanced.org"]

#server setup
try:
    email = address
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email,"placeholder" )
    message =MIMEText("sent via lambda")
    message["From"]= email
    message["To"] = email
    message["Subject"] = "Auto email- lambda has been triggered"
    server.sendmail(email, email, message.as_string())
    print("email has been sent")
    server.quit()
except Exception as e:
    print(f"cannot send email because {e}")
