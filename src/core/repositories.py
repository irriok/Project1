from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def get_one(self):
        pass
