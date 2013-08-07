from Util import userException, debug

class Inventory:
   'Common base class for all inventories'
   invCount = 0

   def __init__(self):
      self.looks = 0
      self.things = []
      debug( "New Inventory %d " % Inventory.invCount)
      Inventory.invCount += 1

   def thingCount(self):
     return len(self.things)

   def displayCount(self):
     print "Total Locations %d" % Inventory.invCount

   def displayThings(self,player):
      if self.thingCount() > 0 :
         print
         if player.code == 'ME':
           print 'You are currently holding ..'
           for thing in self.things:
              thing.displayThing()
         else:
           visibleThings = False
           for thing in self.things:
              if not thing.hidden:
                  visibleThings = True
           if visibleThings:
               print 'It has ..'
               for thing in self.things:
                  if not thing.hidden:
                     thing.displayThing()

      else:
         print
         if player.code == 'ME':
           print 'You have nothing.'


   def findThing(self,thingCode):
         for thing in self.things:
            if thing.code == thingCode:
               return thing
         raise userException("No such thing")

   def score(self):
      myScore = 0
      for thing in self.things:
           myScore += thing.valueGold * 10

      return myScore

   def addThing(self, thing):

     self.things.append(thing)
     debug( "Added " + thing.code + " to inventory as it's thing %d " % self.thingCount())

   def removeThing(self, thing):

     self.things.remove(thing)
     debug( "Removed " + thing.code + " from inventory")


   def dropThing(self, player, getCommand):
      if getCommand == 'DROP':
         if self.thingCount() == 1 :
           thingCode = 'ALL'

         elif self.thingCount() == 0:
           print 'You have nothing to drop.'
           return True
         else:
           print 'Drop what?'
           self.displayThings()
           return True

      elif getCommand.split()[0] == 'DROP':
         thingCode = getCommand.split()[1]
      else:
         return False

      debug( 'Searching for thing to drop.. ' + thingCode)

      DroppedIt = False
      for thing in reversed(self.things): #step backwards because removing items from the list changes the indexes.
              if thingCode in ['ALL',thing.code]:
                 print 'Dropped ' + thing.shortName + '!'
                 thing.moveThing(player.inventory, player.location)
                 DroppedIt = True

      try:
        if not DroppedIt:
          Thing = player.location.findThing(thingCode)
          print 'I do not have ' +  Thing.shortName + ',but I can see it here.'

      except userException,e:
         print "what? I can't drop " + thingCode.lower() + "!"

      return True

   def lookThing(self, player, lookCommand):
      debug( 'Searching for thing.. ' + lookCommand)
      if lookCommand.split()[0] == 'LOOK':
         thingCode = lookCommand.split()[1]
      else:
         return False

      try:
        Thing = self.findThing(thingCode)
        print Thing.description

      except userException,e:
         try:
            Thing = player.location.findThing(thingCode)
            print 'I do not have ' +  Thing.shortName + ', but I can see it here.'

         except userException,e:
            print "You don't have " + thingCode.lower() + "!"

      return True

   def interpretCommand(self,player,command):
   # All commands related to an Inventory
   # Return True if the command was understood in this context.

      if command in ['I','INVENT']:
         debug('INVENTORY command')
         self.displayThings(player)
         return True
      elif self.dropThing(player,command):
         debug('Drop Command')
         return True
      elif self.lookThing(player, command):
         debug('Look Thing Command')
         return True
      elif ( command in ['S','SCORE']):
          debug('SCORE command')
          print "Your current score is " + str (self.score() )
          return True
      else:
        return False
   
   def quickDropAll(self,player):
             for thing in reversed(self.things): #step backwards because removing items from the list changes the indexes.
                 print player.shortName + ' dropped ' + thing.shortName + '!'
                 thing.moveThing(player.inventory, player.location)


