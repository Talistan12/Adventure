Loc = "Stream"
Decis    = "Go"
##INVENTORY = "Inventory"
##StuffDesc = ["Lamp","Serrated knife","Apple","Water","Rations","Ale"]
##StuffLoc = ["InHut","InHut","Tavern","Stream","Stream","Tavern"]
##FIRST_STUFF = 0
##MAX_STUFF = 6
TERMINATE = "STOP"

DEBUGGING = False

def debug( str ):
   if DEBUGGING:
     print str;
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

   def displayWay(self):
      if not self.hidden:
        self.looks +=1
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


   def displayWays(self):
      if self.wayCount > 0 :
         print
         print 'Exits lead ..'
         for i in range( 0, self.wayCount ):
              self.ways[i].displayWay() 

   def displayLocation(self):
      print
      self.looks +=1
      if self.looks < 2:
        print self.longName
      else:
        print self.shortName
      self.displayWays()
      self.displayThings()
      

   def addObject(self, thing):

     self.objects.append(thing)
     debug( "Added " + thing.code + " to " + self.code + " as it's thing %d " % self.thingCount)
     self.thingCount +=1

   def addWay(self, way):

     self.ways.append(way)
     debug( "Added " + way.shortWay + " to " + self.code + " as it's way %d " % self.wayCount)
     self.wayCount +=1

   def findWay(self, wayCommand):
      debug( 'Searching for way.. ' + wayCommand)
      if self.wayCount > 0 :
         for i in range( 0, self.wayCount ):
               if self.ways[i].shortWay == wayCommand or self.ways[i].longWay == wayCommand:
                  print self.ways[i].movingDesc
                  return self.ways[i].destLoc
      return "NOTFOUND"

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
                     return self.locations[i]
                  
      #raise "Location Not Found" ,locCode
      raise userException("Location Not Found")
 
   def locationAddObject(self,locCode,thing):
      try:
          Loc = self.getLocation(locCode)
          Loc.addObject(thing)
      #except "Location Not Found", arg:
      except userException,e:
          print e.args


##try:
##   raise Networkerror("Bad hostname")
##except Networkerror,e:
##   print e.args

   
        
      
##      if self.locCount > 0 :
##         debug( 'Finding location.. ' + locCode)
##         for i in range( 0, self.locCount ):
##               if self.locations[i].code == locCode:
##                     self.locations[i].addObject(thing)
        
   def locationAddWay(self,locCode,way):
      try:
          Loc = self.getLocation(locCode) 
          Loc.addWay(way)
##      except "Location Not Found", arg:
##          print "Couldn't find " + arg
      except userException,e:
          print e.args

 
##      if self.locCount > 0 :
##         debug( 'Finding location.. ' + locCode)
##         for i in range( 0, self.locCount ):
##               if self.locations[i].code == locCode:
##                     self.locations[i].addWay(way)
   
        

##print 'START DEMO1 - In this demo Locations are put together in a list of Locations'        
##Locations = [
##   Location('INHUT','In the Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.')
##   ,Location('VILLAGE','At the Village','You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maybe you could get some ale and food. A path leads East.')
##   ,Location('HUT','Near the Hut','You are standing outside a little hut.  The front door is ajar.  A path leads South and West.')
##   ,Location('STREAM','By a Stream','You are standing by a stream. The stream runs NE to SW. A path leads North.')
##   ,Location('TAVERN','In the Tavern','You have arrived at a tavern busy with people. It is called the Jolly Pig.  A door leads out.')
##   ,Location('INVENT','Inventory','This is just a location to hold your gear.')
##       ] 
##
##Locations[0].addObject(Thing('KNIFE','A Knife','A nasty sharp knife','It is a serrated knife.  Looks sharp.'))
##Locations[0].addObject(Thing('LAMP','A Lamp','An old oil Lamp','It is glowing softly.'))
##Locations[0].displayLocation()
##Locations[0].displayLocation()
##Locations[1].displayLocation()
##Locations[1].displayLocation()
###print
###print "Things at Location 1"
###Locations[1].displayThings()
###print
##Locations[2].displayLocation()
##Locations[2].displayLocation()
##Locations[1].displayCount()
##print Location.locCount
##
##
##print 'END DEMO1' 
print


print 'START DEMO2 - In this demo we keep the OO theme going and put all the locations into a parent object, doing away with the list of locations.'

Adventure = Landscape("ADVENTURE","A Adventure","An amazing adventure")
Adventure.addLocation(Location('INHUT','In the Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.'))
Adventure.addLocation(Location('VILLAGE','At the Village','You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maybe you could get some ale and food.'))
Adventure.addLocation(Location('HUT','Near the Hut','You are standing outside a little hut.  The front door is ajar.'))
Adventure.addLocation(Location('STREAM','By a Stream','You are standing by a stream. The stream runs NE to SW.'))
Adventure.addLocation(Location('TAVERN','In the Tavern','You have arrived at a tavern busy with people. It is called the Jolly Pig.'))
Adventure.addLocation(Location('INVENT','Inventory','This is just a location to hold your gear.'))

Adventure.locationAddObject('STREAM',Thing('WATER','Some Water','A bottle of water','Not mineral water, but smells ok.'))
Adventure.locationAddWay('STREAM',Way('N','NORTH','North','North by a narrow track','A short walk later ...','HUT'))
Adventure.locationAddWay('HUT',Way('S','SOUTH','South','South by a narrow track','A short walk later ...','STREAM'))
Adventure.locationAddObject('INHUT',Thing('KNIFE','A Knife','A nasty sharp knife','It is a serrated knife.  Looks sharp.'))
Adventure.locationAddObject('INHUT',Thing('LAMP','A Lamp','An old oil Lamp','It is glowing softly.'))
Adventure.locationAddWay('INHUT',Way('OUT','DOOR','Out','Out front door','The door creaks as you leave','HUT'))
Adventure.locationAddWay('INHUT',Way('UP','GO UP','Up','Up a ladder to the ceiling','You climb into the ceiling','ATTIC'))
Adventure.locationAddWay('INHUT',Way('XYZZY','','Magic Word','Magic word unknown to adventurer','Wow! how did i get here?','STREAM',True))

##Adventure.listLocations()

currentLocation = Adventure.getLocation('STREAM')

print 'END DEMO2' 
print


##InHut = ['In Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.',{'OUT':"hUT"},StuffDesc[0]]
##Village = ['Village','You have arrived at a village. A path leads East.',{'EAST':'Hut'}]
##Hut = ['Hut','You are standing outside a little hut.  The front door is ajar.  A path leads South and West.',{'SOUTH':'Stream','WEST':'Village','DOOR':'In Hut'}]
##Stream = ['Stream','You are standing by a stream. The stream runs NE to SW. A path leads North.',{'NORTH':'Hut'}, [StuffDesc[2],StuffDesc[3],StuffDesc[4]]]
##current_location = [Stream]




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

print 'You are a wanderer whose aim in life is too collect things. Your goal. Collect all objects in the region. There are 6 in total. FIND THOSE OBJECTS!'

while Decis != TERMINATE:
      #print Loc
      #Tell the adventurer where they are.

      currentLocation.displayLocation()
         
##      if Loc == "Stream" :
##          print Stream[1]
##      elif Loc == "Hut" :
##          print 'You are standing outside a little hut.  The front door is ajar.  A path leads South and West.'
##      elif Loc == "InHut" :
##          print 'You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.'
##      elif Loc == "Village":
##          print 'You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maye you could get some ale and food. A path leads East.'
##      elif Loc == "Tavern":
##            print 'you have arrived at a tavern bustling with people. It is called the Jolly Pig. A door leads out.'
##                        
##      #list any stuff which has a Loc matching where we are now.     
##      is_stuff_there = False
##      for i in range( FIRST_STUFF, MAX_STUFF ):        
##          if StuffLoc[i] == Loc:
##              is_stuff_there = True
##      if is_stuff_there == True:                        
##          print 'There is also ..'
##      for i in range( FIRST_STUFF, MAX_STUFF ):                  
##          if StuffLoc[i] == Loc:
##            print " " + StuffDesc[i]                  

      print     
      Decis = raw_input ('What now?')
      Decis = Decis.upper()

      newLocCode = currentLocation.findWay(Decis)
      if newLocCode <> "NOTFOUND":
        currentLocation = Adventure.getLocation(newLocCode)

      
    #process their input
    
##      if Loc == "Stream" and Decis == 'N' or Decis == 'NORTH':
##            Loc = "Hut"
##            print 'Off I go'
##      elif Loc == "Hut" and Decis == 'S' or Decis == 'SOUTH':
##            Loc = "Stream"  
##            print 'Off I go'
##      elif Loc == "Hut" and Decis == 'W' or Decis == 'WEST':
##            Loc = 'Village'
##            print 'Off I go'
##      elif Loc == "Hut" and (Decis == 'IN' or Decis == 'DOOR'):
##            Loc = "InHut"  
##            print 'In I go'
##      elif Loc == "InHut" and (Decis == 'OUT' or Decis == 'DOOR'):
##            Loc = "Hut"  
##            print 'Out I go'
##      elif Loc == "Village" and Decis == 'E':
##            Loc = 'Hut'
##            print 'Off I go'  
##      elif Loc == "Village" and Decis == 'IN TAVERN':
##            Loc = "Tavern"
##            print "In I go"
##      elif Loc == "Tavern" and (Decis == 'OUT' or Decis == 'DOOR'):
##            Loc = "Village"
##            print 'Out I go'

            
      elif Decis == 'NORTH' or Decis == 'SOUTH' or Decis == 'EAST' or Decis == 'WEST' or Decis == 'N' or Decis == 'S' or Decis == 'E' or Decis == 'W'or Decis == 'NW' or Decis == 'NE' or Decis == 'SW' or Decis == 'SE':
            print 'You cannot go that way'
      elif Decis == 'GET':
            print 'Get what?'
      elif Decis.split()[0] == 'GET':       
        #Check whether the Stuff is here  
        GotIt = False
        GotWhat = ""
        Thing = Decis.split()[1]
        for i in range( FIRST_STUFF, MAX_STUFF ):
            StuffName = StuffDesc[i].upper()

            if StuffLoc[i] == Loc and (StuffName == Thing or Thing == 'ALL'):
                StuffLoc[i] = INVENTORY
                GotIt = True
                print 'Got ' + StuffDesc[i] + '!'
            elif StuffLoc[i] == INVENTORY and StuffName == Thing:
                print 'Got ' +  StuffDesc[i] + ' already!'
                GotIt = True
                
        if not GotIt:
            print "what? I can't pick " + Thing.lower() + " up!"

      elif Decis == 'DROP':
            print 'Drop what?'
            
      elif Decis.split()[0] == 'DROP':       
        #Check whether the Stuff is in your Inventory  
        DroppedIt = False
        DroppedWhat = ""
        Thing = Decis.split()[1]
        for i in range( FIRST_STUFF, MAX_STUFF ):
            StuffName = StuffDesc[i].upper()

            if StuffLoc[i] == INVENTORY and (StuffName == Thing or Thing == 'ALL'):
                StuffLoc[i] = Loc
                DroppedIt = True
                print 'Dropped ' + StuffDesc[i] + '!' 
            elif StuffLoc[i] == Loc and StuffName == Thing:
                print "I don't have " +  StuffDesc[i].lower() + ' but I can see it!'
                DroppedIt = True
                
        if not DroppedIt:
            print "what? I don't have " + Thing + "!"
            
            
      elif Decis == 'LOOK':
            print "I'll repeat myself then, shall I?"
      elif Decis == 'I' or Decis == 'INVENT':
            #list any stuff which has a Loc of "Inventory"
            print 'You are currently holding'
            print ""
            for i in range( FIRST_STUFF, MAX_STUFF ):                  
                if StuffLoc[i] == INVENTORY:
                    print " " + StuffDesc[i]
                
      elif Decis == TERMINATE:
                print 'You did not like our game? What a shame.. what a shame..'
      else:
            print 'Huh?'
            

 
