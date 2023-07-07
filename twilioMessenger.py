import password
import requests
import os
from twilio.rest import Client


class TwillioMessenger:
    def __init__(self, message, title):
        self.message = message
        self.title = title

    def sendMessage(self):
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = password.twillioAccountSid
        auth_token = password.twillioAuthToken
        client = Client(account_sid, auth_token)

        article = self.title+"\n\n"+"\n\n".join(self.message)


        message = client.messages.create(
            body=article,
            from_=f'{password.twillioPhoneNumber}',
            to=f'{password.myPhoneNumber}'
        )

        print(message.sid)
