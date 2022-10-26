import json
from . import config
from .repositories import ConfigRepo
from .services import SlackService, EmailService, LoggerService
from .providers import SlackServiceProvider, EmailServiceProvider, LoggerServiceProvider
from ..core.use_cases import NotifierUseCase

class BaseController:

    def __init__(self):
        self._slack_service = None
        self._slack_service_provider = None
        self._email_service = None
        self._email_service_provider = None
        self._logger_service = None
        self._logger_service_provider = None
        self._env_repo = ConfigRepo()


    @property
    def logger_service(self):
        if self._logger_service is None:
            self._logger_service = LoggerService().logger
        return self._logger_service

    @property
    def logger_service_provider(self):
        if self._logger_service_provider is None:
            self._logger_service_provider = LoggerServiceProvider(self.logger_service)
        return self._logger_service_provider

    @property
    def email_service(self):
        if self._email_service is None:
            host = self._env_repo.get_one(config.EMAIL_HOST).value
            port = self._env_repo.get_one(config.EMAIL_PORT).value
            self._email_service = EmailService(self.logger_service, host, port)
        return self._email_service

    @property
    def email_service_provider(self):
        if self._email_service_provider is None:
            api_key = self._env_repo.get_one(config.EMAIL_API_KEY).value
            secret_key = self._env_repo.get_one(config.EMAIL_SECRET_KEY).value
            sender = self._env_repo.get_one(config.EMAIL_SENDER).value
            self._email_service_provider = EmailServiceProvider(self.logger_service_provider, self.email_service, api_key, secret_key, sender)
        return self._email_service_provider

    @property
    def slack_service(self):
        if self._slack_service is None:
            token = self._env_repo.get_one(config.SLACK_TOKEN).value
            self._slack_service = SlackService(self.logger_service, token)
        return self._slack_service


    @property
    def slack_service_provider(self):
        if self._slack_service_provider is None:
            self._slack_service_provider = SlackServiceProvider(self.logger_service_provider, self.slack_service)
        return self._slack_service_provider



class APIController(BaseController):

    def process_event(self, file):
        with open(file) as f:
            return NotifierUseCase(json.load(f), self.email_service_provider,
                                   self.slack_service_provider, self.logger_service_provider).execute()


