
DEBUGGING = False

def debug( str ):
   if DEBUGGING:
     print "** " + str;
   return;

class userException(RuntimeError):
   def __init__(self, arg):
      self.args = arg


class Thing:
   'Common base class for all things'
   thingCount = 0

   def __init__(self, code, shortName, longName, description):
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.description = description
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

   def inventThings(self):
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

   def goWay(self, wayCommand):
      #returns a Location unless an exception is raised.
      if wayCommand == 'GO':
         print 'Go where?'
         return self 
      
      elif wayCommand.split()[0] == 'GO':
         wayCode = wayCommand.split()[1]
      else:
         wayCode = wayCommand

      debug( 'Searching for way.. ' + wayCode)
      debug( 'way count ' + str (self.wayCount) )
      if self.wayCount > 0 :
         for i in range( 0, self.wayCount ):
               if self.ways[i].shortWay == wayCode or self.ways[i].longWay == wayCode:
                  print
                  print self.ways[i].movingDesc
                  debug(self.ways[i].destLoc)
                  return Adventure.getLocation(self.ways[i].destLoc)
               
      debug( 'Does it get here?')
      if ( wayCode in ['NORTH','SOUTH','EAST','WEST','N','S','E','W','NW','NE','SW','SE','UP','DOWN','IN','OUT','OVER','UNDER','THRU','AROUND']):
            print 'You cannot go ' + wayCode.lower()
            return self 
         
      debug( 'Non-Directional')
      raise userException("Non-Directional")

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


 
def interpretCommand(loc,inv):
# All commands are processed here.  Returns a Location
      print     
      command = raw_input ('What next?')
      command = command.upper()
      try:
          loc = loc.goWay(command)
      except userException,e:
         try:
           loc.getThing(inv,command)
         except userException,e:
            try:
                inv.dropThing(loc,command)
            except userException,e:
              try:
                 if ( command in ['L','LOOK']):
                    loc.looks = 0
                 elif ( command in ['I','INVENT']):
                    inv.inventThings()
                 else:
                    inv.lookThing(command) #Look at an object in the inventory
              except userException,e:
                 print 'huh?'
      finally:
         return loc

 
 
print


print 'START DEMO2 - In this demo we keep the OO theme going and put all the locations into a parent object, doing away with the list of locations.'

Adventure = Landscape("ADVENTURE","A Adventure","An amazing adventure")

Adventure.addLocation(Location('STREAM','By a Stream','You are standing by a stream. The stream runs NE to SW.'))
Adventure.locationAddObject('STREAM',Thing('WATER','Some Water','A bottle of water','Not mineral water, but smells ok.'))
Adventure.locationAddObject('STREAM',Thing('APPLE','An Apple','A juicy looking Apple',"It is pulsating strangely. I'd better not eat it."))
Adventure.locationAddObject('STREAM',Thing('RATIONS','Some Rations','A bag of Rations.',"The Rations look stale, but there all I've got till I reach an Inn or a Tavern"))
Adventure.locationAddWay('STREAM',Way('N','NORTH','North','North by a narrow track','A short walk later ...','HUT'))


Adventure.addLocation(Location('HUT','Near the Hut','You are standing outside a little hut.  The front door is ajar.'))
Adventure.locationAddWay('HUT',Way('S','SOUTH','South','South by a narrow track','A short walk later ...','STREAM'))
Adventure.locationAddWay('HUT',Way('IN','DOOR','Inside','The front door is ajar.','The door creaks erily as you enter ...','INHUT'))
Adventure.locationAddWay('HUT',Way('W','WEST','West','West by a narrow track','A short walk later ...','VILLAGE'))

Adventure.addLocation(Location('INHUT','In the Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.'))
Adventure.locationAddObject('INHUT',Thing('KNIFE','A Knife','A nasty sharp knife','It is a serrated knife.  Looks sharp.'))
Adventure.locationAddWay('INHUT',Way('OUT','DOOR','Out','Out front door','The door creaks as you leave','HUT'))
Adventure.locationAddWay('INHUT',Way('UP','GO UP','Up','Up a ladder to the ceiling','You climb into the ceiling','ATTIC'))
Adventure.locationAddWay('INHUT',Way('XYZZY','','Magic Word','Magic word unknown to adventurer','Wow! how did i get here?','STREAM',True))

Adventure.addLocation(Location('ATTIC','In the Atttic','This is a dark hot place.'))
Adventure.locationAddWay('ATTIC',Way('D','DOWN','Down','Down threw the trapdoor','Going down','INHUT'))


Adventure.addLocation(Location('VILLAGE','At the Village','You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maybe you could get some ale and food.'))
Adventure.locationAddWay('VILLAGE',Way('IN','IN TAVERN','In','In too the Tavern.',"You enter the Tavern with it's hot, stuffy air.",'TAVERN')) 
Adventure.locationAddWay('VILLAGE',Way('E','EAST','East','East by a narrow track.',"A short walk later ...",'HUT')) 
Adventure.locationAddWay('VILLAGE',Way('N','NORTH','North','North by a thin, narrow track.','A short walk later ...','FOREST')) 

Adventure.addLocation(Location('FOREST','At the Forest','You have arrived at a dark and spooky forest. There is a stench of somthing long dead, and no way back to the Village.'))
Adventure.locationAddWay('FOREST',Way('N','NORTH','North','North by a thin, narrow track.',"A short walk later ...",'GRAVEYARD'))

Adventure.addLocation(Location('GRAVEYARD','At the Graveyard','You have arrived at a dark, abandoned Graveyard. There is a stench of somthing long dead, and no way back to the Forest.'))
Adventure.locationAddWay('GRAVEYARD',Way('PASS','PASSAGE','Secret Passage','Underground by a dark, thin, narrow passage.',"A long crawl later ...",'VILLAGE'))

Adventure.addLocation(Location('TAVERN','In the Tavern','You have arrived at a tavern busy with people. It is called the Jolly Pig.'))
Adventure.locationAddObject('TAVERN',Thing('ALE','Some Ale','A pint of Ale','Looks good. I feel like a pint of Ale.'))
Adventure.locationAddWay('TAVERN',Way('OUT','OUT TAVERN','Out','Out of the Tavern.','You leave the Tavern for the fresh air.','VILLAGE')) 


Adventure.addLocation(Location('INVENT','Inventory','This is just a location to hold your gear.'))
Adventure.locationAddObject('INVENT',Thing('NOTE','A Note','A interesting small note.','It reads,"XYZZY".'))

 

##Adventure.listLocations()

currentLocation = Adventure.getLocation('STREAM')
inventory       = Adventure.getLocation('INVENT')

print 'END DEMO2' 
print

 
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
print ''
raw_input('Press enter to continue.')
print
print 'You are a wanderer whose aim in life is too collect things. Your goal. Collect all objects in the region. There are 6 in total. FIND THOSE OBJECTS!'

#perpetual loop
while 1 != 2:
 
      #Tell the adventurer where they are.
      currentLocation.displayLocation()

      #Ask them what to do next
      currentLocation = interpretCommand(currentLocation,inventory)
 
 
 
