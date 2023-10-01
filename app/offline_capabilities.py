# app/offline_capabilities.py

```python
class OfflineCapabilities:
    def __init__(self):
        self.offline_mode = False

    def enable_offline_mode(self):
        self.offline_mode = True

    def disable_offline_mode(self):
        self.offline_mode = False

    def is_offline_mode_enabled(self):
        return self.offline_mode
```
