from ..core.interfaces import BaseMessengerServiceProvider
from services import EmailService, SlackService, LoggerService

# Code in here
class SlackMessengerProvider(BaseMessengerServiceProvider):
    #SlackService
    pass

class EmailServiceProvider(BaseMessengerServiceProvider):
    #EmailService
    pass

class LoggerServiceProvider(BaseMessengerServiceProvider):
    #LoggerService
    pass