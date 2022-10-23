from typing import Optional


class EnvItemEntity:
    key = str
    value: str


class EventEntity:
    event_type: str  # choices: [new_publication, approved_publication]
    body: str
    to: Optional[str]
