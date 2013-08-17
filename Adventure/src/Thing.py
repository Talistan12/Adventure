from Util import userException, debug
from Location import Location
import random

class Thing:
   'Common base class for all things'
   things = []

   @staticmethod
   def listThings():
         print 'Display all Things..'
         for thing in Thing.things:
               thing.displayThing()
   @staticmethod
   def thingCount():
       return len(Thing.things)

   def __init__(self, location, codes, shortName, longName, description):
      if location.shortName == 'RANDOMLOCATION':
          debug( "finding random location" )
          randomLocations = random.sample(Location.locations, 1)
          self.location = randomLocations[0]
          debug(self.location.shortName)
      else:
          self.location = location
      self.codes = codes
      self.shortName = shortName
      self.longName = longName
      self.description = description
      self.hidden = False
      self.looks = 0

      Thing.things.append(self)

      debug( "New Thing %d " % Thing.thingCount() + self.shortName )

      #now add the thing to the location
      self.location.addThing(self)

   def displayCount(self):
     print "Total Things %d" % Thing.thingCount

   def displayThing(self):
      self.looks +=1
      if self.looks < 2:
        print " " + self.longName
      else:
        print " " + self.shortName

   def moveThing(self, originLocation, destLocation):
       originLocation.removeThing(self)
       destLocation.addThing(self)
       self.location = destLocation

class Treasure(Thing):

   def __init__(self, location, codes, shortName, longName, description, valueGold):

      Thing.__init__(self,location, codes, shortName, longName, description)
      self.hidden = True
      self.valueGold = valueGold

class Armour(Thing):

   def __init__(self, location, codes, shortName, longName, description,   hitPoints):

      Thing.__init__(self,location, codes, shortName, longName, description)
      self.hitPoints = hitPoints

class Weapon(Thing):

   def __init__(self, location, codes, shortName, longName, description, actions, damagePoints):

      Thing.__init__(self,location, codes, shortName, longName, description)
      self.actions = actions
      self.damagePoints = damagePoints

class Food(Thing):

   def __init__(self, location, codes, shortName, longName, description, eatMessage, valueFood):

      Thing.__init__(self,location, codes, shortName, longName, description)
      self.eatMessage = eatMessage
      self.valueFood = valueFood

class Drink(Thing):

   def __init__(self, location, codes, shortName, longName, description, eatMessage, valueFood):

      Thing.__init__(self,location, codes, shortName, longName, description)
      self.eatMessage = eatMessage
      self.valueFood = valueFood


class Junk(Thing):
   def __init__(self, location, codes, shortName, longName, description):

      Thing.__init__(self,location, codes, shortName, longName, description)

class Transport(Thing):

   def __init__(self, location, codes, shortName, longName, description, cost):

      Thing.__init__(self,location, codes, shortName, longName, description)
      self.cost = cost
