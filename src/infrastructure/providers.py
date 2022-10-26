from ..core.interfaces import BaseMessengerServiceProvider, BaseEmailServiceProvider, BaseLoggerProvider
from .services import EmailService, SlackService, LoggerService
import smtplib


# Code in here
class EmailServiceProvider(BaseEmailServiceProvider):
    def __init__(self, logger, service, api_key, secret_key, sender):
        self.logger = logger
        self.service = service
        self.api_key = api_key
        self.secret_key = secret_key
        self.sender = sender

    def send_email(self, body, to):
        try:
            service = self.service.get_client()
            with service as server:
                server.login(self.api_key, self.secret_key)
                server.sendmail(self.sender, to, body)
                print('send_email')
                print(server.sendmail(self.sender, to, body))
            return self.logger.info("Message sent to email!")
        except:
            return self.logger.error("Message was not sent via email")



class SlackServiceProvider(BaseMessengerServiceProvider):
    def __init__(self, logger, service):
        self.logger = logger
        self.service = service

    def send_message(self, body, to):
        try:
            client = self.service.get_client()
            # client.chat_postMessage(
            #     channel=to,
            #     text=body
            # )
            return self.logger.info("Message sent via slack!")
        except:
            return self.logger.info("Message was not sent via slack")


class LoggerServiceProvider(BaseLoggerProvider):

    def __init__(self, logger):
        self.logger = logger

    def info(self, message):
        return self.logger.info(message)

    def warning(self, message):
        return self.logger.warning(message)

    def error(self, message):
        return self.logger.error(message)

    def critical(self, message):
        return self.logger.critical(message)