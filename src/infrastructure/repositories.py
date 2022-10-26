import os
from dotenv import dotenv_values
from ..core.repositories import BaseRepository
from ..core.entities import EnvItemEntity


class ConfigRepo(BaseRepository):

    def __init__(self):
        self.env_data = dict(dotenv_values("src/.env"))


    def get_one(self, env_var):
        return EnvItemEntity(env_var, self.env_data[env_var])



