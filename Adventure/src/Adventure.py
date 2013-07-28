from Location import Location, Way
from Inventory import Inventory
from Character import Character
from Thing import Thing
from Util import userException, debug


class Landscape:
   'place to put the locations'
   locCount = 0
   #  location = Location('','','')
   # characters = Character('','','')
   mainCharacter = None

   #inventory = Inventory('','','')

   def __init__(self, code, shortName, longName):
      self.code = code
      self.shortName = shortName
      self.longName = longName
      self.looks = 0
      self.LocCount = 0
      self.locations = []
      debug ("Initialising the landscape")

   def locCount(self):
     return len(self.locations)


   def listLocations(self):
      if self.locCount() > 0 :
         print 'Display all locations..'
         for location in self.locations:
               location.displayLocation()

   def displayLandscape(self):
      self.looks +=1
      if self.looks < 2:
        print self.longName
      else:
        print self.shortName
      self.listLocations()

   def addLocation(self, location):
     self.locations.append(location)
     debug( "Added " + location.code + " to " + self.code + " as it's location %d " % self.locCount())


   def getLocation(self, locCode):
      debug( 'Searching for location.. ' + locCode)
      for location in self.locations:
               if location.code == locCode:
                     debug( 'Found ' + locCode)
                     return location

      raise userException("Location Not Found")




   def locationAddThing(self,locCode,thing):
      try:
          Loc = self.getLocation(locCode)
          Loc.addThing(thing)

      except userException,e:
          print e.args

   def locationAddWay(self,locCode,way):
      try:
          Loc = self.getLocation(locCode)
          Loc.addWay(way)

      except userException,e:
          print e.args


   def locationAddCharacter(self,locCode,character):
      try:
          Loc = self.getLocation(locCode)
          Loc.addCharacter(character)

      except userException,e:
          print e.args


   def interpretCommand(self,player):
   # All commands are processed here.  Returns a Location
         newLocation = self.mainCharacter.location
         print
         command = raw_input ('What next, ' + player.shortName + '?').replace('\r', '')
         command = command.upper().strip()
         if command <> '':
             if player.location.interpretCommand(player,command):
                debug('Location command')
                
             elif player.inventory.interpretCommand(player,command):
                debug('Inventory command')
             else:
                print 'huh?'


   def doTurn(self):
 
      #Ask them what to do next
      self.interpretCommand(self.mainCharacter)

print

Adventure = Landscape("ADVENTURE","An Adventure","An amazing adventure")

Adventure.addLocation(Location('STREAM','By a Stream','You are standing by a stream. The stream runs NE to SW.'))
Adventure.locationAddThing('STREAM',Thing('WATER','some Water','a bottle of water','Not mineral water, but smells ok.'))
Adventure.locationAddThing('STREAM',Thing('APPLE','an Apple','a juicy looking Apple',"It is pulsating strangely. I'd better not eat it."))
Adventure.locationAddThing('STREAM',Thing('RATIONS','some Rations','a bag of Rations.',"The Rations look stale, but there all I've got till I reach an Inn or a Tavern"))
Adventure.locationAddWay('STREAM',Way(['N','NORTH'],'North','North by a narrow track','A short walk later ...','HUT'))
Adventure.locationAddWay('STREAM',Way(['W','WEST'],'West','West by a narrow track','A short walk later ...','PALMFOREST'))

Adventure.addLocation(Location('HUT','Near the Hut','You are standing outside a little hut.'))
Adventure.locationAddWay('HUT',Way(['S','SOUTH'],'South','South by a narrow track','A short walk later ...','STREAM'))
Adventure.locationAddWay('HUT',Way(['IN','DOOR'],'Inside','The front door is ajar.','The door creaks eerily as you enter ...','INHUT'))
Adventure.locationAddWay('HUT',Way(['W','WEST'],'West','West by a narrow track','A short walk later ...','VILLAGE'))

Adventure.addLocation(Location('INHUT','In the Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.'))
Adventure.locationAddThing('INHUT',Thing('KNIFE','A Knife','A nasty sharp knife','It is a serrated knife.  Looks sharp.',0,2))
Adventure.locationAddWay('INHUT',Way(['OUT','DOOR'],'Out','Out front door','The door creaks as you leave','HUT'))
Adventure.locationAddWay('INHUT',Way(['UP','U','MAGIC'],'Up','Up a ladder to the ceiling','You climb into the ceiling','ATTIC'))

Adventure.addLocation(Location('PALMFOREST','at the Palm Forest','You are standing in a lush, Palm Forest full of palms and ferns.'))
Adventure.locationAddWay('PALMFOREST',Way(['S','SOUTH'],'South','South by a narrow track','A short walk later ...','BEACH'))
Adventure.locationAddWay('PALMFOREST',Way(['W','WEST'],'West','West by a narrow track','A short walk later ...','DOCKS'))
Adventure.locationAddWay('PALMFOREST',Way(['E','EAST'],'East','East by a narrow track.',"A short walk later ...",'STREAM'))

Adventure.addLocation(Location('BEACH','at the Beach','You are standing by the sea, with the water licking at your toes.'))
Adventure.locationAddWay('BEACH',Way(['N','NORTH'],'North','North by a narrow track','A short walk later ...','PALMFOREST'))


Adventure.addLocation(Location('ATTIC','In the Attic','This is a dark hot place.'))
Adventure.locationAddWay('ATTIC',Way(['D','DOWN'],'Down','Down threw the trap door','Going down','INHUT'))

Adventure.addLocation(Location('DOCKS','at the Docks','You are standing by the docks. There are a lot of ships, but one catches your eye and it seems to cost only 100 gold coins.'))
Adventure.locationAddWay('DOCKS',Way(['W','WEST'],'West','West by a narrow track','A short walk later ...','PALMFOREST'))
Adventure.locationAddThing('DOCKS',Thing('Boat','A Small One-Man Craft.','The Fresh Cucumber',"          "))

Adventure.addLocation(Location('VILLAGE','At the Village','You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maybe you could get some ale and food.'))
Adventure.locationAddWay('VILLAGE',Way(['IN','IN TAVERN'],'In','In too the Tavern.',"You enter the Tavern with it's hot, stuffy air.",'TAVERN'))
Adventure.locationAddWay('VILLAGE',Way(['E','EAST'],'East','East by a narrow track.',"A short walk later ...",'HUT'))
Adventure.locationAddWay('VILLAGE',Way(['N','NORTH'],'North','North by a thin, narrow track.','A short walk later ...','FOREST'))

Adventure.addLocation(Location('FOREST','At the Forest','You have arrived at a dark and spooky forest. There is a stench of something long dead, and no way back to the Village.'))
Adventure.locationAddWay('FOREST',Way(['N','NORTH'],'North','North by a thin, narrow track.',"A short walk later ...",'GRAVEYARD'))

Adventure.addLocation(Location('GRAVEYARD','At the Grave yard','You have arrived at a dark, abandoned Grave yard. There is a stench of something long dead, and no way back to the Forest.' ))
Adventure.locationAddWay('GRAVEYARD',Way(['PASS','VILLAGE'],'Secret Passage','Underground by a dark, thin, narrow passage.',"A long crawl later ...",'VILLAGE'))
Adventure.locationAddWay('GRAVEYARD',Way(['PATH','CURSEDGLADE'],'Disguised path','Through the cliff by a dark, thin, narrow path.',"A long walk later ...",'CURSEDGLADE'))
Adventure.locationAddCharacter('GRAVEYARD',Character('ZOMBIE'
                                   ,'A Zombie'
                                   ,'A rotting Zombie'
                                   ,'A rotting creature of the undead, who I believe used to be called "Bob"'
                                   ,Adventure.getLocation('GRAVEYARD')
                                   ,Inventory('INVENT'
                                             ,'Inventory'
                                             ,'This is a set of stuff held by a character'
                                             ,[Thing('BRAIN','A Brain','A bloody Brain.','Looks like it has just been removed.')])))

Adventure.addLocation(Location('CURSEDGLADE','At the Cursed Glade','You have arrived at a dark, Cursed Glade. There is a stench of something long dead.'))
Adventure.locationAddWay('CURSEDGLADE',Way(['PASS','GRAVEYARD'],'Hidden Tunnel','Underground by a dark, thin, narrow passage.',"A long crawl later ...",'GRAVEYARD'))
Adventure.locationAddThing('CURSEDGLADE',Thing('DIAMONDRING','A Diamond Ring','A shiny Diamond Ring','It is a very shiny Diamond Ring.  Looks beautiful.',50))
Adventure.locationAddWay('CURSEDGLADE',Way(['XYZZY'],'Magic Word','Magic word unknown to adventurer','Wow! how did i get here?','STREAM',True))
Adventure.locationAddCharacter('CURSEDGLADE',Character('SKELETON'
                                   ,'A Skeleton'
                                   ,'A moist, glistening skeleton'
                                   ,"A moist, glistening creature of the undead, who I can't recognise from any features."
                                   ,Adventure.getLocation('CURSEDGLADE')
                                   ,Inventory('INVENT'
                                             ,'Inventory'
                                             ,'This is a set of stuff held by a character'
                                             ,[Thing('BONE','A Bone','A glistening Bone.','Looks like it is the last remains of the Skeleton.')])))


Adventure.addLocation(Location('TAVERN','In the Tavern','You have arrived at a tavern busy with people. It is called the Jolly Pig.'
                             ,[Way(['OUT','OUT TAVERN'],'Out','Out of the Tavern.','You leave the Tavern for the fresh air.','VILLAGE')]
                             ,[Thing('ALE','Some Ale','A pint of Ale','Looks good. I feel like a pint of Ale.')]))

#Adventure.listLocations()



debug ("BEGIN testing ways list iteration")
wayCode = 'D'
someways = [Way(['D','DOWN'],'Down','Down threw the trapdoor','Going down','INHUT'),Way(['OUT','DOOR'],'Out','Out front door','The door creaks as you leave','HUT')]
for way in someways:
   debug("Check way " + way.shortDesc) # + "[" + way.wayCodes + "]")
   for w in way.wayCodes:
      debug( "way:" + w )

   if wayCode in way.wayCodes:
        debug( way.movingDesc)


debug ("END testing ways list iteration")


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
print 'things in the region. There are ' + str( Thing.thingCount )
print ' in total. FIND THOSE OBJECTS!'
raw_input('Press enter to continue.')

Adventure.mainCharacter = Character('ME'
                                   ,name
                                   ,'the main character'
                                   ,'this is the guy we care about'
                                   ,Adventure.getLocation('STREAM')
                                   ,Inventory('INVENT'
                                             ,'Inventory'
                                             ,'This is a set of stuff held by a character'
                                             ,[Thing('NOTE','a Note','an interesting small note.','It reads,"XYZZY".')]))


Adventure.mainCharacter.location.displayLocation()

#perpetual loop
while True:

  Adventure.doTurn()



