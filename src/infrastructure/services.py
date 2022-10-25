# Code in here
from slack_sdk import WebClient
import smtplib

class EmailService:
    def __init__(self, host, port):
        self.__service = smtplib.SMTP(host, port)

    def get_client(self):
        return self.__service
#
class SlackService:
    def __init__(self, token):
        self.__client = WebClient(token=token)

    def get_client(self):
        return self.__client


#
class LoggerService:
    pass
#
