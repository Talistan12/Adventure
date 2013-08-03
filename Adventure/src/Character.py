from Util import userException, debug
from Inventory import Inventory
import random

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

    def __init__(self, location,code, shortName, longName, description, damagePoints = 0,hitPoints = 30):
        self.code = code
        self.shortName = shortName
        self.longName = longName
        self.description = description
        self.location = location
        self.inventory = Inventory()
        self.damagePoints = damagePoints
        self.hitPoints = hitPoints
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


    def fightCharacter(self, fightCommand):
      fightingWords = ['FIGHT','ATTACK','KILL']
      fightWord = fightCommand.split()[0]
      debug( 'Searching for character.. ' + fightCommand)
      if (fightCommand in fightingWords):
          print fightWord.capitalize() + " what?"
          return True
      if (fightWord in fightingWords):
         characterCode = fightCommand.split()[1]
      else:
         return False

      try:
        character = self.location.findCharacter(characterCode)
        debug("Found character " + character.shortName)

      except userException,e:
         debug('Player is looking but if its a character its not here')
         print "There is no " + characterCode.capitalize() + " here to fight."
         return True

      if len(fightCommand.split()) < 4:
          print fightWord.capitalize() + " " + characterCode.capitalize() + " WITH something?"
          return True

      if fightCommand.split()[2] == 'WITH':
          weaponCode = fightCommand.split()[3]
          try:
              weapon = self.inventory.findThing(weaponCode)
              print "You swing at " + character.shortName + " with " + weapon.shortName
              if random.randint(1,3)==1:
                  print "You got a direct hit!"
                  character.hitPoints = character.hitPoints - (self.damagePoints + weapon.damagePoints)
                  if character.hitPoints <= 0:
                      self.location.removeCharacter(character)
                      print "you have killed your foe!"

                  return True

              else:
                  print "You missed!"
                  return True
          except userException,e:
              debug('Player is not holding weapon')
              print "You don't have " + weaponCode.capitalize()
              return True

      else:
          print fightWord.capitalize() + " " + characterCode.capitalize() + " WITH something?"
          return True


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

             elif self.fightCharacter(command):
                debug('Fight Character Command')
             else:
                print 'huh?'


    def doTurn(self):

         #Ask them what to do next
         self.interpretCommand()