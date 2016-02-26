import redis

class redisDB:
  def __init__(self, hostName):
    self.host = hostName
    self.port = 6379
    r = None
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
    except Exception, exception:
      print exception
    

  def write(self, key, val):
    try:
      if r == None : r = redis.StrictRedis(host=self.host, port=self.port)
      r.set(key, val) 
    except Exception, exception:
      print exception

  def read(self, key):
    try:
      if r == None : r = redis.StrictRedis(host=self.host, port=self.port)
      val = r.get(key)
      print val
      return val
    except Exception, exception:
      print exception

  def listAdd(self, key, val):
    try:
      if r == None : r = redis.StrictRedis(host=self.host, port=self.port)
      return r.lpush(key, val)
    except Exception, exception:
      print exception

  def getList(self, key, start, end):
    try:
      if r == None : r = redis.StrictRedis(host=self.host, port=self.port)
      return r.lrange(key, start, end)
    except Exception, exception:
      print exception
     
