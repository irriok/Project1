from typing import Optional
from dataclasses import dataclass

@dataclass
class EnvItemEntity:


    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

    key: str
    value: str


@dataclass
class EventEntity:

    def __init__(self, type: str, to: str, body: str):
        self.type = type
        self.to = to
        self.body = body

    type: str
    to: str
    body: str
