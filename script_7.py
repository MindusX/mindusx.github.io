from twilio.rest import Client
from flask import current_app
from .models import SMSLog, db
from flask_login import current_user


class SMSService:
    def __init__(self):
        self.client = Client(
            current_app.config['TWILIO_ACCOUNT_SID'],
            current_app.config['TWILIO_AUTH_TOKEN']
        )
        self.from_number = current_app.config['TWILIO_FROM_NUMBER']

    def send(self, to_number: str, message: str) -> str:
        msg = self.client.messages.create(
            body=message,
            from_=self.from_number,
            to=to_number
        )
        # log
        log = SMSLog(
            to_number=to_number,
            message=message,
            status=msg.status,
            user=current_user
        )
        db.session.add(log)
        db.session.commit()
        return msg.sid