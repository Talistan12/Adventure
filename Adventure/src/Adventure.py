from Location import Location

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
 

class Way:
   'Common base class for all ways between locations'
   def __init__(self, shortWay, longWay, shortDesc, longDesc, movingDesc ,destLoc, hidden = False):
      self.shortWay = shortWay
      self.longWay = longWay
      self.shortDesc = shortDesc
      self.longDesc = longDesc
      self.movingDesc = movingDesc
      self.destLoc = destLoc
      self.hidden = hidden
      self.looks = 0
      debug( "New Way " + shortWay + " to " + destLoc)

   def displayWay(self,looks):
      if not self.hidden:
        #self.looks +=1
        self.looks = looks #override with loc.looks so that a LOOK command also gives more way details.
        if self.looks < 2:
          print " " + self.longDesc
        else:
         print " " + self.shortDesc
 


 

class Inventory:
   'Common base class for all inventories'
   invCount = 0

   def __init__(self, code, shortName, longName, objects = []):
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.looks = 0
      self.thingCount = 0
      self.objects = objects
      debug( "New Inventory %d " % Inventory.invCount + self.code)
      Inventory.invCount += 1
   
   def displayCount(self):
     print "Total Locations %d" % Inventory.invCount
 
   def displayThings(self):
      if self.thingCount > 0 :
         print
         print 'You are currently holding ..'
         for i in range( 0, self.thingCount ):
               self.objects[i].displayThing()
      else:
         print
         print 'You have nothing.'

   def findThing(self,thingCode):
      if self.thingCount > 0 :
         for i in range( 0, self.thingCount ):
            if self.objects[i].code == thingCode:
               return self.objects[i]
      raise userException("No such thing")
 
   def score(self):
      myScore = 0
      if self.thingCount > 0 :
         for i in range( 0, self.thingCount ):
           myScore += self.objects[i].valueGold * 10
           
      return myScore
 
   def addObject(self, thing):

     self.objects.append(thing)
     debug( "Added " + thing.code + " to " + self.code + " as it's thing %d " % self.thingCount)
     self.thingCount +=1

   def removeObject(self, thing):

     self.objects.remove(thing)
     debug( "Removed " + thing.code + " from " + self.code)
     self.thingCount -=1
 

   def dropThing(self, location, getCommand):
      if getCommand == 'DROP':
         print 'Drop what?'
         return
      
      elif getCommand.split()[0] == 'DROP':
         thingCode = getCommand.split()[1]
      else:
         raise userException("Non-Drop")

      debug( 'Searching for thing to drop.. ' + thingCode)
 
      DroppedIt = False
      if self.thingCount > 0 :
           for k in range( self.thingCount, 0, -1 ): #step backwards because removing items from the list changes the indexes.
              i = k-1
              debug( str( i ) )
              if self.objects[i].code == thingCode or thingCode == 'ALL':
                 print 'Drop ' +self.objects[i].shortName + '!'
                 #add object to location
                 location.addObject(self.objects[i])
                 #remove object from inventory
                 self.removeObject(self.objects[i])
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

 

class Landscape:
   'place to put the locations'
   locCount = 0
   location = Location('','','')
   inventory = Inventory('','','')

   def __init__(self, code, shortName, longName):
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.looks = 0
      self.LocCount = 0
      self.locations = []
      debug ("Initilizing the landscape")


   def listLocations(self):
      if self.locCount > 0 :
         print 'Display all locations..'
         for i in range( 0, self.locCount ):
               self.locations[i].displayLocation()

   def displayLandscape(self):
      self.looks +=1
      if self.looks < 2:
        print self.longName
      else:
        print self.shortName
      self.listLocations()  

   def addLocation(self, location):
     self.locations.append(location)
     debug( "Added " + location.code + " to " + self.code + " as it's location %d " % self.locCount)
     self.locCount +=1

   def getLocation(self, locCode):
      debug( 'Searching for location.. ' + locCode)
      if self.locCount > 0 :
         for i in range( 0, self.locCount ):
               if self.locations[i].code == locCode:
                     debug( 'Found ' + locCode)
                     return self.locations[i]
 
      raise userException("Location Not Found")
 
   def goWay(self, fromLocation, wayCommand):
      #returns a Location unless an exception is raised.
      if wayCommand == 'GO':
         print 'Go where?'
         return fromLocation 
      
      elif wayCommand.split()[0] == 'GO':
         wayCode = wayCommand.split()[1]
      else:
         wayCode = wayCommand

      debug( 'Searching for way.. ' + wayCode)
      debug( 'way count ' + str (fromLocation.wayCount) )
      if fromLocation.wayCount > 0 :
         for i in range( 0, fromLocation.wayCount ):
               if fromLocation.ways[i].shortWay == wayCode or fromLocation.ways[i].longWay == wayCode:
                  print
                  print fromLocation.ways[i].movingDesc
                  debug(fromLocation.ways[i].destLoc)
                  return self.getLocation(fromLocation.ways[i].destLoc)

      debug( 'Does it get here?')
      if ( wayCode in ['NORTH','SOUTH','EAST','WEST','N','S','E','W','NW','NE','SW','SE','UP','DOWN','IN','OUT','OVER','UNDER','THRU','AROUND']):
            print 'You cannot go ' + wayCode.lower()
            return self 
         
      debug( 'Non-Directional')
      raise userException("Non-Directional")
               
   def locationAddObject(self,locCode,thing):
      try:
          Loc = self.getLocation(locCode)
          Loc.addObject(thing)
 
      except userException,e:
          print e.args
  
   def locationAddWay(self,locCode,way):
      try:
          Loc = self.getLocation(locCode) 
          Loc.addWay(way)
          
      except userException,e:
          print e.args

   def interpretCommand(self):
   # All commands are processed here.  Returns a Location
         newLocation = self.location
         print     
         command = raw_input ('What next?')
         command = command.upper()
         try:
             newLocation = self.goWay(self.location, command)
         except userException,e:
            try:
              self.location.getThing(self.inventory,command)
            except userException,e:
               try:
                   self.inventory.dropThing(self.location,command)
               except userException,e:
                 try:
                    if ( command in ['L','LOOK']):
                       debug("recognised " + command)
                       self.location.looks = 0
                    elif ( command in ['I','INVENT']):
                       debug("recognised " + command)
                       self.inventory.displayThings()
                    elif ( command in ['S','SCORE']):
                       debug("recognised " + command)
                       print "Your current score is " + str (self.inventory.score() )
                    else:
                       self.inventory.lookThing(command) #Look at an object in the inventory
                 except userException,e:
                    print 'huh?'
         finally:
            return newLocation



   def doTurn(self):

      #Tell the adventurer where they are.
      self.location.displayLocation()

      #Ask them what to do next
      self.location = self.interpretCommand()
 
print

Adventure = Landscape("ADVENTURE","An Adventure","An amazing adventure")

Adventure.addLocation(Location('STREAM','By a Stream','You are standing by a stream. The stream runs NE to SW.'))
Adventure.locationAddObject('STREAM',Thing('WATER','Some Water','A bottle of water','Not mineral water, but smells ok.'))
Adventure.locationAddObject('STREAM',Thing('APPLE','An Apple','A juicy looking Apple',"It is pulsating strangely. I'd better not eat it."))
Adventure.locationAddObject('STREAM',Thing('RATIONS','Some Rations','A bag of Rations.',"The Rations look stale, but there all I've got till I reach an Inn or a Tavern"))
Adventure.locationAddWay('STREAM',Way('N','NORTH','North','North by a narrow track','A short walk later ...','HUT'))
Adventure.locationAddWay('STREAM',Way('W','WEST','West','West by a narrow track','A short walk later ...','PALMFOREST'))

Adventure.addLocation(Location('HUT','Near the Hut','You are standing outside a little hut.'))
Adventure.locationAddWay('HUT',Way('S','SOUTH','South','South by a narrow track','A short walk later ...','STREAM'))
Adventure.locationAddWay('HUT',Way('IN','DOOR','Inside','The front door is ajar.','The door creaks erily as you enter ...','INHUT'))
Adventure.locationAddWay('HUT',Way('W','WEST','West','West by a narrow track','A short walk later ...','VILLAGE'))

Adventure.addLocation(Location('INHUT','In the Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.'))
Adventure.locationAddObject('INHUT',Thing('KNIFE','A Knife','A nasty sharp knife','It is a serrated knife.  Looks sharp.',0,2))
Adventure.locationAddWay('INHUT',Way('OUT','DOOR','Out','Out front door','The door creaks as you leave','HUT'))
Adventure.locationAddWay('INHUT',Way('UP','GO UP','Up','Up a ladder to the ceiling','You climb into the ceiling','ATTIC'))
Adventure.locationAddWay('INHUT',Way('XYZZY','','Magic Word','Magic word unknown to adventurer','Wow! how did i get here?','STREAM',True))

Adventure.addLocation(Location('PALMFOREST','at the Palm Forest','You are standing in a lush, Palm Forest full of palms and ferns.'))
Adventure.locationAddWay('PALMFOREST',Way('S','SOUTH','South','South by a narrow track','A short walk later ...','BEACH'))
Adventure.locationAddWay('PALMFOREST',Way('W','WEST','West','West by a narrow track','A short walk later ...','DOCKS'))
Adventure.locationAddWay('PALMFOREST',Way('E','EAST','East','East by a narrow track.',"A short walk later ...",'STREAM')) 

Adventure.addLocation(Location('BEACH','at the Beach','You are standing by the sea, with the water licking at your toes.'))
Adventure.locationAddWay('BEACH',Way('N','NORTH','North','North by a narrow track','A short walk later ...','PALMFOREST'))


Adventure.addLocation(Location('ATTIC','In the Atttic','This is a dark hot place.'))
Adventure.locationAddWay('ATTIC',Way('D','DOWN','Down','Down through the trapdoor','Going down','INHUT'))

Adventure.addLocation(Location('DOCKS','at the Docks','You are standing by the docks. There are a lot of ships, but one catches your eye and it seems to cost only 100 gold coins.'))
Adventure.locationAddWay('DOCKS',Way('W','WEST','West','West by a narrow track','A short walk later ...','PALMFOREST'))
Adventure.locationAddObject('DOCKS',Thing('Boat','A Small One-Man Craft.','The Fresh Cucumber',"          "))

Adventure.addLocation(Location('VILLAGE','At the Village','You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maybe you could get some ale and food.'))
Adventure.locationAddWay('VILLAGE',Way('IN','IN TAVERN','In','In too the Tavern.',"You enter the Tavern with it's hot, stuffy air.",'TAVERN')) 
Adventure.locationAddWay('VILLAGE',Way('E','EAST','East','East by a narrow track.',"A short walk later ...",'HUT')) 
Adventure.locationAddWay('VILLAGE',Way('N','NORTH','North','North by a thin, narrow track.','A short walk later ...','FOREST')) 

Adventure.addLocation(Location('FOREST','At the Forest','You have arrived at a dark and spooky forest. There is a stench of something long dead, and no way back to the Village.'))
Adventure.locationAddWay('FOREST',Way('N','NORTH','North','North by a thin, narrow track.',"A short walk later ...",'GRAVEYARD'))

Adventure.addLocation(Location('GRAVEYARD','At the Graveyard','You have arrived at a dark, abandoned Graveyard. There is a stench of something long dead, and no way back to the Forest.'))
Adventure.locationAddWay('GRAVEYARD',Way('PASS','VILLAGE','Secret Passage','Underground by a dark, thin, narrow passage.',"A long crawl later ...",'VILLAGE'))
Adventure.locationAddWay('GRAVEYARD',Way('PATH','CURSEDGLADE','Disguised path','Through the cliff by a dark, thin, narrow path.',"A long walk later ...",'CURSEDGLADE'))

Adventure.addLocation(Location('CURSEDGLADE','At the Cursed Glade','You have arrived at a dark, Cursed Glade. There is a stench of something long dead.'))
Adventure.locationAddWay('CURSEDGLADE',Way('PASS','GRAVEYARD','Hidden Tunnel','Underground by a dark, thin, narrow passage.',"A long crawl later ...",'GRAVEYARD'))
Adventure.locationAddObject('CURSEDGLADE',Thing('DIAMONDRING','A Diamond Ring','A shiny Diamond Ring','It is a very shiny Diamond Ring.  Looks beautiful.',50))

 
Adventure.addLocation(Location('TAVERN','In the Tavern','You have arrived at a tavern busy with people. It is called the Jolly Pig.'))
Adventure.locationAddWay('TAVERN',Way('OUT','OUT TAVERN','Out','Out of the Tavern.','You leave the Tavern for the fresh air.','VILLAGE'))
Adventure.locationAddObject('TAVERN',Thing('ALE','Some Ale','A pint of Ale','Looks good. I feel like a pint of Ale.'))
 

##Adventure.listLocations()

Adventure.location  = Adventure.getLocation('STREAM')

Adventure.inventory = Inventory('INVENT','Inventory','This is a set of stuff held by a character')
Adventure.inventory.addObject(Thing('NOTE','A Note','An interesting small note.','It reads,"XYZZY".'))



 
#storyline
print 'You have just woken up. Your'
print "memory is hazy and you can't "
print 'even remember your name and'
print 'decide to give yourself one'
name = raw_input('pick a name. ')
print ''
print 'You think you are in the'
print 'lands of Hawcry, a land'
print 'once ruled by giant eagles'
print 'of immense strength and' 
print 'great power.'
print 'You are a wanderer whose'
print 'aim in life is too collect things.'
print 'Your goal. Collect all'
print 'objects in the region. There are ' + str( Thing.thingCount )
print ' in total. FIND THOSE OBJECTS!'
raw_input('Press enter to continue.')

#perpetual loop
while True:
 
  Adventure.doTurn()
 
 
 
