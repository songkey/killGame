import redisDB
import json

class GameServer:
  def __init__(self, MemberNum):
    self.db = redisDB("120.27.29.9")
    self.MembersListKey = "global_members_list"

    self.MembersListKey = "global_members_list"
    self.StageKey = "global_state_stage"
    self.RoundKey = "global_state_round"
    self.MemberNumKey = "global_state_membernum"

    self.Stage = none
    self.Round = 0
    self.MemberNum = MemberNum

    self.MembersList = []
    self.Members = {}

    self.setStage("none")
    self.setRound(0)
    self.setMemberNum(MemberNum)

  # val: none, start, end
  def setStage(self, val):
    return self.db.write(self.StageKey, val)

  # val: 0, 1, 2, ...
  def setRound(self, val):
    return self.db.write(self.RoundKey, val)
  
  # val: int > 0
  def setMemberNum(self, val):
    return self.db.write(self.MemberNumKey, val)

  def getStage(self):
    return self.db.read(self.StageKey)

  def getRound(self):
    return self.db.read(self.RoundKey)

  def getMemberNum(self):
    return self.db.read(self.MemberNumKey)
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
    
  def getMembersList(self):
    return self.db.getList(self.MembersListKey, 0, self.MemberNum - 1)

  def getQuestion(self, player):
    key = "global_" + player + "_question"
    val = self.db.read(key)
    return val

  # player : player name
  # answer : true or false
  def setAnswer(self, player, answer):
    key = "global_" + player + "_question"
    self.db.write(key, answer): 
