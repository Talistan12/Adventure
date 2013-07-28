from Util import userException, debug

class Inventory:
   'Common base class for all inventories'
   invCount = 0

   def __init__(self, code, shortName, longName, things = []):
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.looks = 0
      if len(things) == 0:
         self.things = []
      else: self.things = things
      debug( "New Inventory %d " % Inventory.invCount + self.code)
      Inventory.invCount += 1

   def thingCount(self):
     return len(self.things)

   def displayCount(self):
     print "Total Locations %d" % Inventory.invCount

   def displayThings(self):
      if self.thingCount() > 0 :
         print
         if self.code == 'ME':
           print 'You are currently holding ..'
         else:
           print 'It has ..'  
         for thing in self.things:
            thing.displayThing()
      else:
         print
         if self.code == 'ME':
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
     debug( "Added " + thing.code + " to " + self.code + " as it's thing %d " % self.thingCount())

   def removeThing(self, thing):

     self.things.remove(thing)
     debug( "Removed " + thing.code + " from " + self.code)


   def dropThing(self, location, getCommand):

      if getCommand == 'DROP':
         if self.thingCount() == 1 :
           thingCode = 'ALL'
         elif self.thingCount() == 0:
           print 'You have nothing to drop.'
           return
         else:
           print 'Drop what?'
           self.displayThings()
           return

      elif getCommand.split()[0] == 'DROP':
         thingCode = getCommand.split()[1]
      else:
         raise userException("Non-Drop")

      debug( 'Searching for thing to drop.. ' + thingCode)

      DroppedIt = False
      for thing in reversed(self.things): #step backwards because removing items from the list changes the indexes.
              if thingCode in ['ALL',thing.code]:
                 print 'Dropped ' + thing.shortName + '!'
                 #add thing to location
                 location.addThing(thing)
                 #remove thing from inventory
                 self.removeThing(thing)
                 DroppedIt = True

      try:
        if not DroppedIt:
          Thing = location.findThing(thingCode)
          print 'I do not have ' +  Thing.shortName + ',but I can see it here.'
      except userException,e:
         print "what? I can't drop " + thingCode.lower() + "!"

   def lookThing(self, lookCommand):
      debug( 'Searching for thing.. ' + lookCommand)
      if lookCommand.split()[0] == 'LOOK':
         thingCode = lookCommand.split()[1]
      else:
         raise userException("Non-Look")

      try:
        Thing = self.findThing(thingCode)
        print Thing.description

      except userException,e:
         print "You don't have " + thingCode.lower() + "!"