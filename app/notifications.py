# app/notifications.py

```python
class Notifications:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.receive_notification(message)
```

This code defines a `Notifications` class that allows subscribers to receive notifications. The class has methods to subscribe, unsubscribe, and notify subscribers.