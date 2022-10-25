from ..core.interfaces import BaseMessengerServiceProvider, BaseEmailServiceProvider
from .services import EmailService, SlackService, LoggerService
import smtplib


# Code in here
class EmailServiceProvider(BaseEmailServiceProvider):
    def __init__(self, service, api_key, secret_key, sender):
        # self.logger = logger
        self.service = service
        self.api_key = api_key
        self.secret_key = secret_key
        self.sender = sender

    def send_email(self, text, to):
        service = self.service.get_client()
        print(service)
        with service as server:
            server.login(self.api_key, self.secret_key)
            server.sendmail(self.sender, to, text)
            print('send_email')
            print(server.sendmail(self.sender, to, text))



class SlackServiceProvider(BaseMessengerServiceProvider):
    def __init__(self, service):
    # def __init__(self, logger, service):
    #     self.logger = logger
        self.service = service

    def send_message(self, text, to):
        client = self.service.get_client()
        response = client.chat_postMessage(
            channel=to,
            text=text
        )

class LoggerServiceProvider(BaseMessengerServiceProvider):
    #LoggerService
    pass