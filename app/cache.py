import redis

cache = redis.Redis(host='localhost', port=6379, db=0)

def get_data(key):
    return cache.get(key)

def set_data(key, value):
    cache.set(key, value)