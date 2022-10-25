from abc import ABC, abstractmethod


class BaseUseCase(ABC):

    @abstractmethod
    def execute(self):
        pass


class NotifierUseCase(BaseUseCase):

    def __init__(self):
        pass
    # Code in here
    def execute(self):
        pass

