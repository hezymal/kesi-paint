class EventBus:
    def __init__(self):
        self.channels = {}

    def subscribe(self, channel_name: str, listener):
        channel = self.channels.get(channel_name)
        if channel is None:
            self.channels[channel_name] = []
            channel = self.channels[channel_name]
        channel.append(listener)

    def publish(self, channel_name, data):
        channel = self.channels.get(channel_name)
        if channel is None:
            return
        for listener in channel:
            listener(data)
