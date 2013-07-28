from Util import userException, debug

class Thing:
   'Common base class for all things'
   thingCount = 0

   def __init__(self, code, shortName, longName, description, valueGold = 0, damagePoints = 0):
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.description = description
      self.valueGold = valueGold
      self.valueDamage = damagePoints
      self.looks = 0
      debug( "New Thing %d " % Thing.thingCount + self.code )
      Thing.thingCount += 1

   def displayCount(self):
     print "Total Things %d" % Thing.thingCount

   def displayThing(self):
      self.looks +=1
      if self.looks < 2:
        print " " + self.longName
      else:
        print " " + self.shortName