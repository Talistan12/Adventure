Location = "Stream"
Decis    = "Go"
INVENTORY = "Inventory"
StuffDesc = ["Lamp","Serrated knife","Apple","Water","Rations","Ale"]
StuffLocation = ["InHut","InHut","Tavern","Stream","Stream","Tavern"]
FIRST_STUFF = 0
MAX_STUFF = 6
TERMINATE = "STOP"


class Thing:
   'Common base class for all things'
   thingCount = 0

   def __init__(self, code, shortName, longName, description):
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.description = description
      self.looks = 0
      print "New Thing %d " % Thing.thingCount + self.code
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
   #locCount = 0

   def __init__(self, shortWay, longWay, shortDesc, longDesc, movingDesc ,destLoc, hidden):
      self.shortWay = shortWay
      self.longWay = longWay
      self.shortDesc = shortDesc
      self.longDesc = longDesc
      self.movingDesc = movingDesc
      self.destLoc = destLoc
      self.hidden = hidden
      self.looks = 0
      #self.thingCount = 0
      #self.objects = []
      print "New Way " + shortWay + " to " + destLoc
      #Location.locCount += 1

   def displayWay(self):
      if not self.hidden:
        #print " " + self.shortDesc
        self.looks +=1
        if self.looks < 2:
          print " " + self.longDesc
        else:
         print " " + self.shortDesc
   
   #def displayCount(self):
 #    print "Total Locations %d" % Location.locCount

 #  def displayThings(self):
 #     if self.thingCount > 0 :
 #        print 'There is also ..'
 #        for i in range( 0, self.thingCount ):
 #              #print i
 #              #print self.objects[i].code
 #              self.objects[i].displayThing()

 #  def displayLocation(self):
 #     self.looks +=1
 #     if self.looks < 2:
 #       print self.longName
 #     else:
 #       print self.shortName
 #     self.displayThings()  

 #  def addObject(self, thing):
#
 #    self.objects.append(thing)
 #    print "Added " + thing.code + " to " + self.code + " as it's thing %d " % self.thingCount
 #    self.thingCount +=1




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
      print "New Location %d " % Location.locCount + self.code
      Location.locCount += 1
   
   def displayCount(self):
     print "Total Locations %d" % Location.locCount

   def displayThings(self):
      if self.thingCount > 0 :
         print 'There is also ..'
         for i in range( 0, self.thingCount ):
               #print i
               #print self.objects[i].code
               self.objects[i].displayThing()


   def displayWays(self):
      if self.wayCount > 0 :
         print 'Exits lead ..'
         for i in range( 0, self.wayCount ):
              self.ways[i].displayWay() 

   def displayLocation(self):
      self.looks +=1
      if self.looks < 2:
        print self.longName
      else:
        print self.shortName
      self.displayWays()
      self.displayThings()
      

   def addObject(self, thing):

     self.objects.append(thing)
     print "Added " + thing.code + " to " + self.code + " as it's thing %d " % self.thingCount
     self.thingCount +=1

   def addWay(self, way):

     self.ways.append(way)
     print "Added " + way.shortWay + " to " + self.code + " as it's way %d " % self.wayCount
     self.wayCount +=1
     

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
      #print "New Location %d " % Location.locCount + self.code
      #Location.locCount += 1
      print "initilize the landscape"
   
   #def displayCount(self):
   #  print "Total Locations %d" % Location.locCount

   def listLocations(self):
      if self.locCount > 0 :
         print 'Display all locations..'
         for i in range( 0, self.locCount ):
               #print i
               #print self.objects[i].code
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
     print "Added " + location.code + " to " + self.code + " as it's location %d " % self.locCount
     self.locCount +=1
     
   def addThingAtLocation(self,thing,locCode):
      if self.locCount > 0 :
         print 'Finding location..'
         for i in range( 0, self.locCount ):
               if self.locations[i].code == locCode:
                     self.locations[i].addObject(thing)
        
   def addWayAtLocation(self,way,locCode):
      if self.locCount > 0 :
         print 'Finding location..'
         for i in range( 0, self.locCount ):
               if self.locations[i].code == locCode:
                     self.locations[i].addWay(way)
   
        

print 'START DEMO1 - In this demo Locations are put together in a list of Locations'        
Locations = [
   Location('INHUT','In the Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.')
   ,Location('VILLAGE','At the Village','You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maybe you could get some ale and food. A path leads East.')
   ,Location('HUT','Near the Hut','You are standing outside a little hut.  The front door is ajar.  A path leads South and West.')
   ,Location('STREAM','By a Stream','You are standing by a stream. The stream runs NE to SW. A path leads North.')
   ,Location('TAVERN','In the Tavern','You have arrived at a tavern busy with people. It is called the Jolly Pig.  A door leads out.')
   ,Location('INVENT','Inventory','This is just a location to hold your gear.')
       ] 

Locations[0].addObject(Thing('KNIFE','A Knife','A nasty sharp knife','It is a serrated knife.  Looks sharp.'))
Locations[0].addObject(Thing('LAMP','A Lamp','An old oil Lamp','It is glowing softly.'))
Locations[0].displayLocation()
Locations[0].displayLocation()
Locations[1].displayLocation()
Locations[1].displayLocation()
#print
#print "Things at Location 1"
#Locations[1].displayThings()
#print
Locations[2].displayLocation()
Locations[2].displayLocation()
Locations[1].displayCount()
print Location.locCount


print 'END DEMO1' 
print


print 'START DEMO2 - In this demo we keep the OO theme going and put all the locations into a parent object, doing away with the list of locations.'

Adventure = Landscape("ADVENTURE","A Adventure","An amazing adventure")
Adventure.addLocation(Location('INHUT','In the Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.'))
Adventure.addLocation(Location('VILLAGE','At the Village','You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maybe you could get some ale and food. A path leads East.'))
Adventure.addLocation(Location('HUT','Near the Hut','You are standing outside a little hut.  The front door is ajar.  A path leads South and West.'))
Adventure.addLocation(Location('STREAM','By a Stream','You are standing by a stream. The stream runs NE to SW. A path leads North.'))
Adventure.addLocation(Location('TAVERN','In the Tavern','You have arrived at a tavern busy with people. It is called the Jolly Pig.  A door leads out.'))
Adventure.addLocation(Location('INVENT','Inventory','This is just a location to hold your gear.'))


Adventure.addThingAtLocation(Thing('KNIFE','A Knife','A nasty sharp knife','It is a serrated knife.  Looks sharp.'),'INHUT')
Adventure.addThingAtLocation(Thing('LAMP','A Lamp','An old oil Lamp','It is glowing softly.'),'INHUT')
Adventure.addWayAtLocation(Way('OUT','DOOR','Out','Out front door','The door creaks as you leave','HUT',False),'INHUT')
Adventure.addWayAtLocation(Way('UP','GO UP','Up','Up a ladder to the ceiling','You climb into the ceiling','ATTIC',False),'INHUT')

Adventure.listLocations()


print 'END DEMO2' 
print


InHut = ['In Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.',{'OUT':"hUT"},StuffDesc[0]]
Village = ['Village','You have arrived at a village. A path leads East.',{'EAST':'Hut'}]
Hut = ['Hut','You are standing outside a little hut.  The front door is ajar.  A path leads South and West.',{'SOUTH':'Stream','WEST':'Village','DOOR':'In Hut'}]
Stream = ['Stream','You are standing by a stream. The stream runs NE to SW. A path leads North.',{'NORTH':'Hut'}, [StuffDesc[2],StuffDesc[3],StuffDesc[4]]]
current_location = [Stream]




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
      print
      #Tell the adventurer where they are.
      if Location == "Stream" :
          print Stream[1]
      elif Location == "Hut" :
          print 'You are standing outside a little hut.  The front door is ajar.  A path leads South and West.'
      elif Location == "InHut" :
          print 'You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.'
      elif Location == "Village":
          print 'You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maye you could get some ale and food. A path leads East.'
      elif Location == "Tavern":
            print 'you have arrived at a tavern bustling with people. It is called the Jolly Pig. A door leads out.'
                        
      #list any stuff which has a location matching where we are now.     
      is_stuff_there = False
      for i in range( FIRST_STUFF, MAX_STUFF ):        
          if StuffLocation[i] == Location:
              is_stuff_there = True
      if is_stuff_there == True:                        
          print 'There is also ..'
      for i in range( FIRST_STUFF, MAX_STUFF ):                  
          if StuffLocation[i] == Location:
            print " " + StuffDesc[i]                  
           
      Decis = raw_input ('What now?')
      Decis = Decis.upper()
 
    #process their input
    
      if Location == "Stream" and Decis == 'N' or Decis == 'NORTH':
            Location = "Hut"
            print 'Off I go'
      elif Location == "Hut" and Decis == 'S' or Decis == 'SOUTH':
            Location = "Stream"  
            print 'Off I go'
      elif Location == "Hut" and Decis == 'W' or Decis == 'WEST':
            Location = 'Village'
            print 'Off I go'
      elif Location == "Hut" and (Decis == 'IN' or Decis == 'DOOR'):
            Location = "InHut"  
            print 'In I go'
      elif Location == "InHut" and (Decis == 'OUT' or Decis == 'DOOR'):
            Location = "Hut"  
            print 'Out I go'
      elif Location == "Village" and Decis == 'E':
            Location = 'Hut'
            print 'Off I go'  
      elif Location == "Village" and Decis == 'IN TAVERN':
            Location = "Tavern"
            print "In I go"
      elif Location == "Tavern" and (Decis == 'OUT' or Decis == 'DOOR'):
            Location = "Village"
            print 'Out I go'
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
            Stuff = StuffDesc[i].upper()

            if StuffLocation[i] == Location and (StuffName == Thing or Thing == 'ALL'):
                StuffLocation[i] = INVENTORY
                GotIt = True
                print 'Got ' + StuffDesc[i] + '!'
            elif StuffLocation[i] == INVENTORY and StuffName == Thing:
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

            if StuffLocation[i] == INVENTORY and (StuffName == Thing or Thing == 'ALL'):
                StuffLocation[i] = Location
                DroppedIt = True
                print 'Dropped ' + StuffDesc[i] + '!' 
            elif StuffLocation[i] == Location and StuffName == Thing:
                print "I don't have " +  StuffDesc[i].lower() + ' but I can see it!'
                DroppedIt = True
                
        if not DroppedIt:
            print "what? I don't have " + Thing + "!"
            
            
      elif Decis == 'LOOK':
            print "I'll repeat myself then, shall I?"
      elif Decis == 'I' or Decis == 'INVENT':
            #list any stuff which has a location of "Inventory"
            print 'You are currently holding'
            print ""
            for i in range( FIRST_STUFF, MAX_STUFF ):                  
                if StuffLocation[i] == INVENTORY:
                    print " " + StuffDesc[i]
                
      elif Decis == TERMINATE:
                print 'You did not like our game? What a shame.. what a shame..'
      else:
            print 'Huh?'
            

 
