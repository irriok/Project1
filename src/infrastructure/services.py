# Code in here
from slack_sdk import WebClient
import smtplib
import logging


class EmailService:
    def __init__(self, logger, host, port):
        self.logger = logger
        self.__service = smtplib.SMTP(host, port)

    def get_client(self):
        return self.__service
#
class SlackService:
    def __init__(self, logger, token):
        self.logger = logger
        self.__client = WebClient(token=token)

    def get_client(self):
        return self.__client


#
class LoggerService:
    # Create and configure logger
    def __init__(self):
        self.logger = logging.basicConfig(filename="newfile.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')


