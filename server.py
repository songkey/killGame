import redisDB
import json
class GameServer:
  def __init__(self):
    db = redisDB("120.27.29.9")
    self.setState("none", 0)

  # Stage : none, start, end
  # Round : 1, 2, ...
  def setState(self, Stage, Round):
    val = {"Stage" : Stage, "Round" : str(Round)}
    self.db.write("State", json.dumps(val))

  def getState(self):
    val = self.db.read("State")
    objs = json.loads(val)
    return objs["Stage"], objs["Round"]
    
