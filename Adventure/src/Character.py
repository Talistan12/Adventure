from Util import userException, debug

class Character:
    'A player or NPC in the game'
#    name = ""
#    location = None
#    inventory = None
    
    def __init__(self, code, shortName, longName, description, location, inventory):
        self.code = code
        self.shortName = shortName
        self.longName = longName
        self.description = description
        self.location = location
        self.inventory = inventory
        self.looks = 0
  
    def displayCharacter(self): 
      print
      self.looks +=1
      if self.looks < 2:
        print self.longName
      else:
        print self.shortName
      self.inventory.displayThings()

