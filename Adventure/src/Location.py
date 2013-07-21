from Util import userException, debug

class Location:
   'Common base class for all locations'
   locCount = 0

   def __init__(self, code, shortName, longName):
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.looks = 0
      self.thingCount = 0
      self.objects = []  
      self.wayCount = 0
      self.ways = []
 
      debug( "New Location %d " % Location.locCount + self.code)
      Location.locCount += 1
   
   def displayCount(self):
     print "Total Locations %d" % Location.locCount

   def displayThings(self):
      if self.thingCount > 0 :
         print
         print 'There is also ..'
         for i in range( 0, self.thingCount ):
               self.objects[i].displayThing()
 
   def findThing(self,thingCode):
      if self.thingCount > 0 :
         for i in range( 0, self.thingCount ):
            if self.objects[i].code == thingCode:
               return self.objects[i]
      raise userException("No such thing")
 

  
   def displayWays(self, looks):
      if self.wayCount > 0 :
         print
         print 'Exits lead ..'
         for i in range( 0, self.wayCount ):
              self.ways[i].displayWay(looks) 

   def displayLocation(self):
      print
      self.looks +=1
      if self.looks < 2:
        print self.longName
      else:
        print self.shortName
      self.displayWays(self.looks)
      self.displayThings()
      

   def addObject(self, thing):

     self.objects.append(thing)
     debug( "Added " + thing.code + " to " + self.code + " as it's thing %d " % self.thingCount)
     self.thingCount +=1

   def removeObject(self, thing):

     self.objects.remove(thing)
     debug( "Removed " + thing.code + " from " + self.code)
     self.thingCount -=1

   def addWay(self, way):

     self.ways.append(way)
     debug( "Added " + way.shortWay + " to " + self.code + " as it's way %d " % self.wayCount)
     self.wayCount +=1

   def getThing(self, inventory, getCommand):

      if getCommand == 'GET':
         print 'Get what?'
         return
      
      elif getCommand.split()[0] == 'GET':
         thingCode = getCommand.split()[1]
      else:
         raise userException("Non-Get")

      debug( 'Searching for thing to get.. ' + thingCode)

 
      GotIt = False
      if self.thingCount > 0 :
           for k in range( self.thingCount, 0, -1 ): #step backwards because removing items from the list changes the indexes.
              i = k-1
              debug( str( i ) )
              if self.objects[i].code == thingCode or thingCode == 'ALL':
                 print 'Got ' +self.objects[i].shortName + '!'
                 #add object to inventory
                 inventory.addObject(self.objects[i])
                 #remove object from location
                 self.removeObject(self.objects[i])
                 GotIt = True
      try:
        if not GotIt:
          Thing = inventory.findThing(thingCode)
          print 'Got ' +  Thing.shortName + ' already!'
      except userException,e:
         print "what? I can't pick " + thingCode.lower() + " up!"

