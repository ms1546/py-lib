import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

singleton1 = ThreadSafeSingleton()
singleton2 = ThreadSafeSingleton()

singleton1.set_value('Singleton instance data')

print(singleton1.get_value())
print(singleton2.get_value())
print(singleton1 is singleton2)
