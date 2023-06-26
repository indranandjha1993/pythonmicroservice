from app.repository import KeyValueStore

store = KeyValueStore()


def get_value(key):
    return store.get(key)


def set_value(key, value):
    store.set(key, value)
