from typing import Optional


class EnvItemEntity:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class EventEntity:
    def __init__(self, type, to, text):
        self.type = type
        self.to = to
        self.text = text
