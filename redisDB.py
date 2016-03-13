import redis

class redisDB:
  def __init__(self, hostName):
    self.host = hostName
    self.port = 6379

  def kset(self, key, val):
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
      r.set(key, val) 
    except Exception, exception:
      print exception

  def kget(self, key):
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
      val = r.get(key)
      print val
      return val
    except Exception, exception:
      print exception

  def kmset(KeyValDict):
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
      return r.mset(KeyValDict)
    except Exception, exception:
      print exception
      
  def kmget(KeyList):
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
      return r.mget(KeyList)
    except Exception, exception:
      print exception
    
  def lpush(self, key, val):
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
      return r.rpush(key, val)
    except Exception, exception:
      print exception

  def lrange(self, key, start, end):
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
      return r.lrange(key, start, end)
    except Exception, exception:
      print exception
     
  def llength(self, key):
    try:
      r = redis.StrictRedis(host=self.host, port=self.port)
      return r.llength(key)
    except Exception, exception:
      print exception
