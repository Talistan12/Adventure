from Util import userException, debug

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

   def __init__(self, location, code, shortName, longName, description, valueGold = 0, damagePoints = 0):
      self.location = location
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.description = description
      self.valueGold = valueGold
      self.valueDamage = damagePoints
      self.looks = 0
      self.hidden = False
 
      Thing.things.append(self)
      
      debug( "New Thing %d " % Thing.thingCount() + self.code )
      
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