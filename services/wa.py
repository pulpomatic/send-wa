import os
from dotenv import load_dotenv
from twilio.rest import Client
account_sid = os.getenv('TWILIO_ACCOUNT_SID') 
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')


def send_message(content_sid: str, to: str, content_variables: dict, from_=twilio_whatsapp_number):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        content_sid=content_sid,
        content_variables=content_variables,
        from_=from_,
        to=to
    )
    print(message)
    return message