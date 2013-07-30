from Util import userException, debug

class Way:
   'Common base class for all ways between locations'
   def __init__(self, originLocation, destLocation, wayCodes, shortDesc, longDesc, movingDesc , hidden = False):
      self.wayCodes = wayCodes
      self.shortDesc = shortDesc
      self.longDesc = longDesc
      self.movingDesc = movingDesc
      self.originLocation = originLocation
      self.destLocation = destLocation
      self.hidden = hidden
      self.looks = 0
      debug( "New Way " + shortDesc + " to " + destLocation.shortName)
      
      originLocation.addWay(self)

   def displayWay(self,looks):
      if not self.hidden:
        #self.looks +=1
        self.looks = looks #override with loc.looks so that a LOOK command also gives more way details.
        if self.looks < 2:
          print " " + self.longDesc
        else:
          print " " + self.shortDesc

class Location:
   'Common base class for all locations'

   locations = []
 
   @staticmethod
   def listLocations():
         print 'Display all locations..'
         for location in Location.locations:
               location.displayLocation() 
               
   @staticmethod
   def locationCount():
       return len(Location.locations)
 
   def __init__(self, shortName, longName ):
      self.code = '' #DONT NEED THIS ANYMORE
      self.shortName = shortName
      self.longName = longName
      self.looks = 0
      self.ways = []
      self.things = []
      self.characters = []
      
      Location.locations.append(self)

      debug( "New Location %d" % len(Location.locations) + self.shortName)

   def thingCount(self):
     return len(self.things)

   def wayCount(self):
     return len(self.ways)

   def characterCount(self):
     return len(self.characters)

   def displayCount(self):
     print "Total Locations %d" % Location.locCount

   def displayWays(self, looks):
      if self.wayCount() > 0 :
         print
         print 'Exits lead ..'
         for way in self.ways:
            way.displayWay(looks)

   def displayThings(self):
      if self.thingCount() > 0 :
         print
         print 'Nearby is ..'
         for thing in self.things:
            thing.displayThing()

   def displayCharacters(self):
      if self.characterCount() > 0 :
         print
         print 'I can see ..'
         for character in self.characters:
            character.displayCharacter()

   def findThing(self,thingCode):
      for thing in self.things:
         if thing.code == thingCode:
            return thing
      raise userException("No such thing")

   def findCharacter(self,characterCode):
      for character in self.characters:
         if character.code == characterCode:
            return character
      raise userException("No such character")


   def displayLocation(self):
      print
      self.looks +=1
      if self.looks < 2:
        print self.longName
      else:
        print self.shortName
      self.displayWays(self.looks)
      self.displayThings()
      self.displayCharacters()
 
   def addThing(self, thing):

     self.things.append(thing)
     debug( "Added " + thing.code + " to " + self.code + " as it's thing %d " % self.thingCount())


   def removeThing(self, thing):

     self.things.remove(thing)
     debug( "Removed " + thing.code + " from " + self.code)
     
 



   def addWay(self, way):

     self.ways.append(way)
     debug( "Added " + way.shortDesc + " to " + self.code + " as it's way %d " % self.wayCount())




   def addCharacter(self, character):

     self.characters.append(character)
     debug( "Added " + character.shortName + " to " + self.code + " as it's character %d " % self.characterCount())

   def removeCharacter(self, character):

     self.characters.remove(character)
     debug( "Removed " + character.shortName + " from " + self.code)
  

   def goWay(self, player, wayCommand):
      #returns a Location unless an exception is raised.
#      if wayCommand == 'GO':
#         print 'Go where?'
#         print self.displayWays(0)
#         return self

      if wayCommand.split()[0] == 'GO':
          wayCode = wayCommand.split(" ",1)[1]
      else:
         wayCode = wayCommand

      debug( 'Searching for way.. ' + wayCode)
      debug( 'way count ' + str ( self.wayCount() ) )
      debug( 'ways length ' + str( len(self.ways)) )
      #   debug( 'at least 1 way exists' )
      for way in self.ways:
          debug("Check way " + way.shortDesc)
          if wayCode in way.wayCodes:
                  print
                  print way.movingDesc
                  debug(way.destLocation.shortName)
                  player.location = way.destLocation #self.getLocation(way.destLoc)
                  #Tell the adventurer where they are.
                  player.location.displayLocation()
                  return True
                  #return newLocation

      debug( 'Does it get here?')
      if ( wayCode in ['NORTH','SOUTH','EAST','WEST','N','S','E','W','NW','NE','SW','SE','UP','DOWN','IN','OUT','OVER','UNDER','THRU','AROUND']):
            print 'You cannot go ' + wayCode.lower()
            return True

      debug( 'Non-Directional')
      return False

   def getThing(self, player, getCommand):

      if getCommand == 'GET':
         if self.thingCount() == 1 :
           thingCode = 'ALL'
         elif self.thingCount() == 0:
           print 'There is nothing to get.'
           return True
         else:
           print 'Get what?'
           self.displayThings()
           return True

      elif getCommand.split()[0] == 'GET':
         thingCode = getCommand.split()[1]
      else:
         return False

      debug( 'Searching for thing to get.. ' + thingCode)


      GotIt = False
      for thing in reversed(self.things): #step backwards because removing items from the list changes the indexes.
          if thingCode in ['ALL',thing.code]:
                 print 'Got ' + thing.shortName + '!'
                 thing.moveThing(player.location, player.inventory)
                 GotIt = True

      try:
        if not GotIt:
          Thing = player.inventory.findThing(thingCode)
          print 'Got ' +  Thing.shortName + ' already!'

      except userException,e:
         print "what? I can't pick " + thingCode.lower() + " up!"
     
      return True

   def lookCharacter(self, lookCommand):
      debug( 'Searching for character.. ' + lookCommand)
      if lookCommand.split()[0] == 'LOOK':
         characterCode = lookCommand.split(" ",1)[1]
      else:
         return False

      try:
        character = self.findCharacter(characterCode)
        print character.description
        return True

      except userException,e:
         debug('Player is looking but if its a character its not here')
         #Don't say its not here, because it could be a thing they are looking for
         #So the lookThing routine will either find it or say its not here.
         #print "There is no " + characterCode.lower() + " here!"
         return False
 
#   def fightCharacter(self, player, fightCommand):
#      debug( 'Searching for character.. ' + fightCommand)
#      if lookCommand.split()[0] == 'FIGHT':
#         characterCode = lookCommand.split()[1]
#      else:
#         return False
#
#      try:
#        character = self.findCharacter(characterCode)
#        debug("Found character " + character.shortName)
#        if lookCommand.split()[2] == 'WITH':
#          weaponCode = lookCommand.split()[3]
#          player.inventory
#        else:
#          print "With what?"
#          return True
#        
#        
#        
#        
#        print character.description
#        return True
#
#      except userException,e:
#         debug('Player is looking but if its a character its not here')
#         print "There is no " + characterCode.lower + " here to fight."
#         return True
#     
         
   def interpretCommand(self,player,command):
   # All commands related to a location, or stuff at locations (things, characters)
   # Return True if the command was understood in this context.

      if command in ['L','LOOK']:
          debug('LOOK command')
          player.location.looks = 0
          player.location.displayLocation()
          return True
      elif ( command in ['GO']):
          print "Go where?"
          debug('GO command')
          return True
      if self.goWay(player, command):
          debug('Go Command')
          return True
      elif self.getThing(player,command):
          debug('Get Command')
          return True
      elif self.lookCharacter(command):
          debug('Look Character Command')
          return True
#      elif self.fightCharacter(player,command):
#          debug('Fight Character Command')
#          return True
      else:
          return False
         
