from manager import PubSubManager
from pub import Publisher
from sub import Subscriber


pubsub_manager = PubSubManager()
publisher = Publisher(pubsub_manager)
subscriber1 = Subscriber('test_event', pubsub_manager)
subscriber2 = Subscriber('another_event', pubsub_manager)

publisher.publish('test_event', 'Hello, this is test_event!')
publisher.publish('another_event', 'Greetings from another_event!')
