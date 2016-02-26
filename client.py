import redisDB
import json

class GameClient:
  def __init__(self, Name):
    db = redisDB("120.27.29.9")

    self.name = Name
    self.Stage = none
    self.Round = 0
    
    self.MembersList = []
    self.Members = {}

  def addMyname():
    
    
