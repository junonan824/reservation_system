import redis

lock_client = redis.Redis(host='localhost', port=6379, db=1)

def acquire_lock(lock_name, timeout=10):
    return lock_client.set(lock_name, 'lock', ex=timeout, nx=True)

def release_lock(lock_name):
    lock_client.delete(lock_name)