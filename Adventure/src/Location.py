from Util import userException, debug

class Location:
   'Common base class for all locations'
   locCount = 0

   def __init__(self, code, shortName, longName, ways = [], things = []):
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.looks = 0
      self.things = []  
      self.ways = []
      if len(ways) == 0:
         self.ways = []
      else: self.ways = ways
      if len(things) == 0:
         self.things = []
      else: self.things = things       
 
      debug( "New Location %d " % Location.locCount + self.code)
      Location.locCount += 1

   def thingCount(self):
     return len(self.things)

   def wayCount(self):
     return len(self.ways)
   
   def displayCount(self):
     print "Total Locations %d" % Location.locCount

   def displayThings(self):
      if self.thingCount() > 0 :
         print
         print 'Nearby is ..'
         for thing in self.things:
            thing.displayThing()
 
 
   def findThing(self,thingCode):
      if self.thingCount() > 0 :
         for thing in self.things:
            if thing.code == thingCode:
               return thing
      raise userException("No such thing")
 

  
   def displayWays(self, looks):
      if self.wayCount() > 0 :
         print
         print 'Exits lead ..'
         for way in self.ways:
            way.displayWay(looks) 

   def displayLocation(self):
      print
      self.looks +=1
      if self.looks < 2:
        print self.longName
      else:
        print self.shortName
      self.displayWays(self.looks)
      self.displayThings()
      

   def addThing(self, thing):

     self.things.append(thing)
     debug( "Added " + thing.code + " to " + self.code + " as it's thing %d " % self.thingCount())


   def removeThing(self, thing):

     self.things.remove(thing)
     debug( "Removed " + thing.code + " from " + self.code)


   def addWay(self, way):

     self.ways.append(way)
     debug( "Added " + way.shortDesc + " to " + self.code + " as it's way %d " % self.wayCount())


   def goWay(self, wayCommand):
      #returns a Location unless an exception is raised.
      if wayCommand == 'GO':
         print 'Go where?'
         print self.displayWays(0)
         return self 
      
      elif wayCommand.split()[0] == 'GO':
          wayCode = wayCommand.split().remove('GO')
      else:
         wayCode = wayCommand

      debug( 'Searching for way..[' + wayCode + ']')
      debug( 'way count ' + str ( self.wayCount() ) )
      debug( 'ways length ' + str( len(self.ways)) ) 
      #   debug( 'at least 1 way exists' )
      for way in self.ways:
          debug("Check way " + way.shortDesc)
          if wayCode in way.wayCodes:
			      print
			      print way.movingDesc
			      debug(way.destLoc)
			      return Adventure.getLocation(way.destLoc)
               
      debug( 'Does it get here?')
      if ( wayCode in ['NORTH','SOUTH','EAST','WEST','N','S','E','W','NW','NE','SW','SE','UP','DOWN','IN','OUT','OVER','UNDER','THRU','AROUND']):
            print 'You cannot go ' + wayCode.lower()
            return self 
         
      debug( 'Non-Directional')
      raise userException("Non-Directional")

   def getThing(self, inventory, getCommand):

      if getCommand == 'GET':
         if self.thingCount() == 1 :
           thingCode = 'ALL'
         elif self.thingCount() == 0:
           print 'There is nothing to get.'
           return
         else:
           print 'Get what?'
           self.displayThings()
           return
      
      elif getCommand.split()[0] == 'GET':
         thingCode = getCommand.split()[1]
      else:
         raise userException("Non-Get")

      debug( 'Searching for thing to get.. ' + thingCode)

 
      GotIt = False
      for thing in reversed(self.things): #step backwards because removing items from the list changes the indexes.
          if thingCode in ['ALL',thing.code]:
                 print 'Got ' + thing.shortName + '!'
                 #add thing to inventory
                 inventory.addThing(thing)
                 #remove thing from location
                 self.removeThing(thing)
                 GotIt = True

 
      try:
        if not GotIt:
          Thing = inventory.findThing(thingCode)
          print 'Got ' +  Thing.shortName + ' already!'
      except userException,e:
         print "what? I can't pick " + thingCode.lower() + " up!"

 
