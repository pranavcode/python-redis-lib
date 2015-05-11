import redis

# Globals
global redis_obj
global keyform

# Initialize
# initialize RedisDB connection
# Return error=False for success and error=True for failure
def Init(host, port):
    global keyform, redis_obj
    keyform = 'pylib:url:'
    redis_obj = redis.StrictRedis(host=host, port=port, db=0)
    if redis_obj is None:
        print 'Connection with Redis DB cannot be established.'
        return True
    return False

# Store new URL
# adds a count specific key and url value
# Return error=False for success and error=True for failure
def Store(count, url):
    global keyform
    if RedisAvailable():
        key = keyform + str(count)
        redis_obj.set(key, url)
        return False
    return True

# Fetch URL
# fetch url for a count specific key
# Return url for success and None for failure
def Fetch(count):
    global keyform
    if RedisAvailable():
        key = keyform + str(count)
        return redis_obj.get(key)

# Check for Redis availability
# Return False for non-connectivity and True otherwise
def RedisAvailable():
    global redis_obj
    if redis_obj is None:
        print 'Redis DB not connected.'
        return False
    return True
