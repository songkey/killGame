import redisDB
import json

class GameBase:
  def __init__(self, Name = "nil"):
    self.db = redisDB("120.27.29.9")

    self.name = Name

    self.Stage = "none"
    self.Round = 0
    self.MemberNum = 0
    self.KillerNum = 0
    self.StatementVote = "none"
    self.CurrentMember = 0
    self.StatementList = []
    self.Vote = 0

    self.MembersList = []

    self.MembersListKey = "global_members_list"
    
    self.StateKeyList = [ \
       "global_state_stage", \
       "global_state_round",\
       "global_state_membernum", \
       "global_state_killernum", \
       "global_state_statement_vote", \
       "global_state_current_member", \
       "global_state_statement", \
       "global_state_vote" \
    ]

  def getState(self):
    tmpVal = self.db.kmget(self.StateKeyList)
    self.Stage = tmpVal[0]
    self.Round = int(tmpVal[1])
    self.MemberNum = int(tmpVal[2])
    self.KillerNum = int(tmpVal[3])
    self.StatementVote = tmpVal[4]
    self.CurrentMember = int(tmpVal[5])
    self.StatementList = tmpVal[6].split("_")
    self.Vote = int(tmpVal[7])    

  def setStat(self):
    tmpKV = {}
    tmpKV["global_state_stage"] = self.Stage
    tmpKV["global_state_round"] = str(self.Round)
    tmpKV["global_state_membernum"] = str(self.MemberNum)
    tmpKV["global_state_killernum"] = str(self.KillerNum)
    tmpKV["global_state_statement_vote"] = self.StatementVote
    tmpKV["global_state_current_member"] = str(self.CurrentMember)
    tmpKV["global_state_statement"] = "_".join(self.StatementList)
    tmpKV["global_state_vote"] = str(self.Vote)

    self.db.kmset(tmpKV)

  def setSVCurrent(self):
    tmpKV = {}
    tmpKV["global_state_statement_vote"] = self.StatementVote
    tmpKV["global_state_current_member"] = str(self.CurrentMember)

    self.db.kmset(tmpKV)

  def setCurrentMember(self):
    self.db.kset("global_state_current_member", str(self.CurrentMember))

  # just for client
  def setStatement(self):
    self.db.kset("global_state_statement", "_".join(self.StatementList))

  # just for client
  def setVote(self):
    self.db.kset("global_state_vote", str(self.Vote))

  def setStageRound(self):
    tmpKV = {}
    tmpKV["global_state_stage"] = self.Stage
    tmpKV["global_state_round"] = str(self.Round)
    
    self.db.kmset(tmpKV)
    
  def setRound(self):
    self.db.kset("global_state_round", str(self.Round))

  def getStage(self):
    

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
    
