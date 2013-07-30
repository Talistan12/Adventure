from Util import userException, debug
from Inventory import Inventory

class Character:
    ' A player or NPC in the game'
    characters = []
   
    @staticmethod
    def listCharacters():
         print 'Display all Characters..'
         for character in Character.characters:
               character.displayCharacter() 
    @staticmethod
    def characterCount():
       return len(Character.characters)
    
    def __init__(self, location,code, shortName, longName, description):
        self.code = code
        self.shortName = shortName
        self.longName = longName
        self.description = description
        self.location = location
        self.inventory = Inventory()
        self.looks = 0
        
        Character.characters.append(self)
      
        debug( "New Character %d " % Character.characterCount() + self.code )
        
        #now add the character to the location
        self.location.addCharacter(self)
  
    def displayCharacter(self): 
      print
      self.looks +=1
      if self.looks < 2:
        print self.longName
      else:
        print self.shortName
      self.inventory.displayThings(self)
      
    def moveCharacter(self, originLocation, destLocation):  
       originLocation.removeCharacter(self)   
       destLocation.addCharacter(self)
       self.location = destLocation

    def interpretCommand(self):
    # All commands are processed here.  Returns a Location
         newLocation = self.location
         print
         command = raw_input ('What next, ' + self.shortName + '?').replace('\r', '')
         command = command.upper().strip()
         if command <> '':
             if self.location.interpretCommand(self,command):
                debug('Location command')

             elif self.inventory.interpretCommand(self,command):
                debug('Inventory command')
             else:
                print 'huh?'


    def doTurn(self):

         #Ask them what to do next
         self.interpretCommand()