from Util import userException, debug
from Inventory import Inventory
import random
from Thing import Weapon
from Location import Location
NOWHERE = Location('NOWHERE','You can not go here, but your hands can.')
HANDS = Weapon(NOWHERE,'HANDS','your fists','A couple of calloused hands','Look out I am desperate now.',['punch','thump'],2)

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
        self.oldCommand = ""

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
      fightingWords = ['FIGHT','ATTACK','KILL','HIT']
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
              if weaponCode in ['HANDS','FISTS']:
                  weapon = HANDS
              else:    
                  weapon = self.inventory.findThing(weaponCode)
              if isinstance(weapon, Weapon):
                  print "You " + random.sample(weapon.actions,1)[0] + " " + character.shortName + " with " + weapon.shortName
                  if random.randint(1,2)==1:
                      print "You got a direct hit!"
                      character.hitPoints = character.hitPoints - (self.damagePoints + weapon.damagePoints)
                      if character.hitPoints <= 0:
                          character.inventory.quickDropAll(character)
                          self.location.removeCharacter(character)
                          print "you have killed your foe!"
                      else:
                          print "It has " + str(character.hitPoints) + " health left!"
                  else:
                      print "You missed!"
                      #return True
                          
              else:
                  print weapon.shortName + "is not a weapon! You'd be better off fighting with your bare hands!"
                  return True


              
              #Foe fights back
              if character.hitPoints > 0:
                  print character.shortName + " takes a swing at you!" # + weapon.shortName
                  if random.randint(1,2)==1:
                      print "It hit you!!"
                      self.hitPoints = self.hitPoints - character.damagePoints #+ weapon.damagePoints)
                      if self.hitPoints <= 0:
                          self.inventory.quickDropAll(self)
                          print "YOU ............... ARE ............................... DEEEEEEEEAAAAAAAAD!"
                      else:
                          print "You have " + str(self.hitPoints) + " health left!"
                  else:
                      print "It missed!"
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
         if command == 'AGAIN':
             command = self.oldCommand
         if command <> '':
             if self.location.interpretCommand(self,command):
                debug('Location command')
                self.oldCommand = command #remember command

             elif self.inventory.interpretCommand(self,command):
                debug('Inventory command')
                self.oldCommand = command #remember command

             elif self.fightCharacter(command):
                debug('Fight Character Command')
                self.oldCommand = command #remember command
             else:
                print 'huh?'
         


    def doTurn(self):

         #Ask them what to do next
         self.interpretCommand()