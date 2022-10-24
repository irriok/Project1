import json
import config
from repositories import ConfigRepo

class BaseController:

    def __init__(self, slack_service, email_service, logger_service, env_repo, email_service_provider,
                 messenger_service_provider, logger_service_provider):
        self._slack_service = slack_service
        self._email_service = email_service
        self._logger_service = logger_service
        self._env_repo = env_repo
        self._email_service_provider = email_service_provider
        self._messenger_service_provider = messenger_service_provider
        self._logger_service_provider = logger_service_provider

    def env_repo(self):
        return ConfigRepo

    def logger_service(self):
        return LoggerService

    def logger_service_provider(self):
        return LoggerServiceProvider

    def email_service(self):
        if _email_service is None:
            api_key = self._env_repo.get_one(config.EMAIL_SECRET_KEY)

    def emailservice_provider(self):
        return EmailServiceProvider

    def slack_service(self):
        return SlackService

    def slack__service_provider(self):
        return SlackServiceProvider


class APIController(BaseController):

    @staticmethod
    def process_event(file):
        with open(file) as f:
            data = json.load(f)


