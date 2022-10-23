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


class APIController(BaseController):

    def process_event(self):
        pass


