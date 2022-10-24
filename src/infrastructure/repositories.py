import os
from dotenv import dotenv_values


class ConfigRepo:

    def __init__(self):
        self.env_data = EnvItemEntity.get_env_data()

    def get_one(self, env_var):
        return self.env_data[env_var]

class EnvItemEntity:
    def __init__(self):
        self.env_data = dotenv_values(".env")

    def get_env_data(self):
        return self.env_data

