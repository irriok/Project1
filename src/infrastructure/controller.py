import json
from . import config
from .repositories import ConfigRepo
from .services import SlackService, EmailService
from .providers import SlackServiceProvider, EmailServiceProvider


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
            self._logger_service = LoggerService()
        return self._logger_service

    @property
    def logger_service_provider(self):
        if self._logger_service_provider is None:
            self._logger_service_provider = LoggerServiceProvider(self._logger_service)
        return "a"

    @property
    def email_service(self):
        if self._email_service is None:
            host = self._env_repo.get_one(config.EMAIL_HOST)
            port = self._env_repo.get_one(config.EMAIL_PORT)
            self._email_service = EmailService(host, port)
            # self._email_service = EmailService(self.logger_provider, api_key, secret_key)

        return self._email_service

    @property
    def email_service_provider(self):
        if self._email_service_provider is None:
            api_key = self._env_repo.get_one(config.EMAIL_API_KEY)
            secret_key = self._env_repo.get_one(config.EMAIL_SECRET_KEY)
            sender = self._env_repo.get_one(config.EMAIL_SENDER)
            # self._email_service_provider = EmailServiceProvider(self._logger_service_provider, self.email_service)
            self._email_service_provider = EmailServiceProvider(self.email_service, api_key, secret_key, sender)
        return self._email_service_provider

    @property
    def slack_service(self):
        if self._slack_service is None:
            token = self._env_repo.get_one(config.SLACK_TOKEN)
            self._slack_service = SlackService(token)
            # self._slack_service = SlackService(self.logger_provider, token)
        return self._slack_service


    @property
    def slack_service_provider(self):
        if self._slack_service_provider is None:
            # self._slack_service_provider = SlackServiceProvider(self._logger_service_provider, self._slack_service)
            self._slack_service_provider = SlackServiceProvider(self.slack_service)
        return self._slack_service_provider



class APIController(BaseController):

    @staticmethod
    def process_event(file):
        with open(file) as f:
            return json.load(f)


