from abc import ABC, abstractmethod


class BaseMessengerServiceProvider(ABC):

    @abstractmethod
    def send_message(self):
        pass


class BaseEmailServiceProvider(ABC):

    @abstractmethod
    def send_email(self):
        pass


class BaseLoggerProvider(ABC):

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def warning(self):
        pass

    @abstractmethod
    def error(self):
        pass

    @abstractmethod
    def critical(self):
        pass
