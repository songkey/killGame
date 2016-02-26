import redisDB
import json

class GameClient:
  def __init__(self, Name = "nil"):
    self.db = redisDB("120.27.29.9")

    self.MembersListKey = "global_members_list"
    self.StageKey = "global_state_stage"
    self.RoundKey = "global_state_round"
    self.MemberNumKey = "global_state_membernum"

    self.name = Name
    self.Stage = none
    self.Round = 0
    self.MemberNum = 0
    
    self.MembersList = []
    self.Members = {}

  def getStage(self):
    return self.db.read(self.StageKey)

  def getRound(self):
    return self.db.read(self.RoundKey)

  def getMemberNum(self):
    return self.db.read(self.MemberNumKey)

  def addMyname(self):
    self.db.listAdd(self.MembersListKey, self.name)
  
  def getMembersList(self):
    return self.db.getList(self.MembersListKey, 0, self.MemberNum - 1)
    
