from ..core.entities import EventEntity

class EventSerializer:

    # Code in here
    def __init__(self, eventData):
        self.eventData = eventData

    def serialize(self):
        return EventEntity(self.eventData['type'], self.eventData['to'], self.eventData['body'])

    def deserialize(self):
        return dict({"type": self.eventData.type,
                "to": self.eventData.to,
                "body": self.eventData.body})
