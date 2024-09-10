class Subscriber:
    def __init__(self, event_type, pubsub_manager):
        self.event_type = event_type
        self.pubsub_manager = pubsub_manager
        self.pubsub_manager.subscribe(event_type, self.notify)

    def notify(self, data):
        print(f"Subscriber received {self.event_type} with data: {data}")

    def unsubscribe(self):
        self.pubsub_manager.unsubscribe(self.event_type, self.notify)
