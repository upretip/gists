
"""
How to send text using twilio api
Aurhor : PUpreti
Date: 2019??
"""

import configparser

from twilio.rest import Client

config = configparser.ConfigParser()
config.read("config.ini")

twilio = config("twilio")


def twilio_send(to_number):
    """Sending text using twilio api"""
    
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure

    account_sid = twilio['account_sid']
    auth_token = twilio['auth_token']
    client = Client(account_sid, auth_token)
    try:
        message = client.messages \
                        .create(
                             body="Are you having a good day Sunshine?",
                             from_='+1 805-805-5058',
                             to= to_number
                     )
        print("sms successfully sent", message.sid)
    except Exception as e:
        print(f'exception {e} occured')

if __name__ == "__main__":
    twilio_send('+1 805-805-5058')
