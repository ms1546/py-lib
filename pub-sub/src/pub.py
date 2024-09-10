class Publisher:
    def __init__(self, pubsub_manager):
        self.pubsub = pubsub_manager

    def publish(self, event_type, data):
        self.pubsub.publish(event_type, data)
