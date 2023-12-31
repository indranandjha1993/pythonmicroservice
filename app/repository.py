class KeyValueStore:
    def __init__(self):
        self.store = {}

    def get(self, key):
        return self.store.get(key, None)

    def set(self, key, value):
        self.store[key] = value
