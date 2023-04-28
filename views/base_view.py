from utils.event_bus import EventBus


class BaseView:
    def __init__(self):
        self.event_bus = EventBus()
