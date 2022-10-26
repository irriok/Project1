from abc import ABC, abstractmethod
from ..infrastructure.serializers import EventSerializer


class BaseUseCase(ABC):

    @abstractmethod
    def execute(self):
        pass


class NotifierUseCase(BaseUseCase):

    def __init__(self, data, email, slack, logger):
        self.data = data
        self.email = email
        self.slack = slack
        self.logger = logger

    def execute(self):
        data = EventSerializer(self.data).serialize()
        if data.type == "new_publication":
            self.slack.send_message(data.body, data.to)
        elif data.type == "approved_publication":
            self.email.send_email(data.body, data.to)
        else:
            return None
