import redis

class redisDB:
  def __init__(self, hostName):
    self.host = hostName
    self.port = 6379

  def write(self, key, val):
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
      r.set(key, val) 
    except Exception, exception:
      print exception
  def read(self, key):
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
      val = r.get(key)
      print val
      return val
    except Exception, exception:
      print exception
