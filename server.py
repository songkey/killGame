import redisDB
import json
class GameServer:
  def __init__(self, MemberNum):
    db = redisDB("120.27.29.9")
    self.MemberNum = MemberNum
    self.setState("none", 0, MemberNum)

  # Stage : none, start, end
  # Round : 1, 2, ...
  # MemberNum : i > 0
  def setState(self, Stage, Round, MemberNum):
    val = {"global_Stage" : Stage, "Round" : str(Round), \
           "MemberNum" : str(MemberNum)}
    self.db.write("State", json.dumps(val))

  def getState(self):
    val = self.db.read("global_State")
    objs = json.loads(val)
    return objs["Stage"], int(objs["Round"]), int(objs["MemberNum"])
    
  def getMembers(self):
    val = self.db.read("global_Members")
    objs = json.loads(val)
    if len(objs) <= self.MemberNum : return objs
    else return objs[0:self.MemberNum]

  def getQuestion(self, player):
    key = "global_" + player + "_question"
    val = self.db.read(key)
    return val

  # player : player name
  # answer : true or false
  def setAnswer(self, player, answer):
    key = "global_" + player + "_question"
    self.db.write(key, answer): 
