from Location import Location, Way
from Inventory import Inventory
from Character import Character
from Thing import Thing
from Util import userException, debug

print


STREAM = Location('By a Stream','You are standing by a stream. The stream runs NE to SW.')
HUT = Location('Near the Hut','You are standing outside a little hut.')
PALMFOREST = Location('At the Palm Forest','You are standing in a lush, Palm Forest full of palms and ferns.')
INHUT = Location('In the Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.')
BEACH = Location('At the Beach','You are standing by the sea, with the water licking at your toes.')
ATTIC = Location('In the Attic','This is a dark hot place.')
DOCKS = Location('At the Docks','You are standing by the docks. There are a lot of ships, but one catches your eye and it seems to cost only 100 gold coins.')
FOREST = Location('At the Forest','You have arrived at a dark and spooky forest. There is a stench of something long dead, and no way back to the Village.')
GRAVEYARD = Location('At the Grave yard','You have arrived at a dark, abandoned Grave yard. There is a stench of something long dead, and no way back to the Forest.' )
VILLAGE = Location('At the Village','You have arrived at a village bustling with life. There is a tavern which seems to be booming in business. Maybe you could get some ale and food.')
CURSEDGLADE = Location('At the Cursed Glade','You have arrived at a dark, Cursed Glade. There is a stench of something long dead.')
TAVERN = Location('In the Tavern','You have arrived at a tavern busy with people. It is called the Jolly Pig.')

#STREAM
Way(STREAM, HUT       ,['N','NORTH'],'North','North by a narrow track','A short walk later ...')
Way(STREAM, PALMFOREST,['W','WEST'] ,'West','West by a narrow track','A short walk later ...')

WATER   = Thing(STREAM, 'WATER','some Water','a bottle of water','Not mineral water, but smells ok.')
APPLE   = Thing(STREAM, 'APPLE','an Apple','a juicy looking Apple',"It is pulsating strangely. I'd better not eat it.")
RATIONS = Thing(STREAM, 'RATIONS','some Rations','a bag of Rations.',"The Rations look stale, but there all I've got till I reach an Inn or a Tavern")

#HUT
Way(HUT, STREAM ,['S','SOUTH'],'South','South by a narrow track','A short walk later ...')
Way(HUT, INHUT  ,['IN','DOOR'],'Inside','The front door is ajar.','The door creaks eerily as you enter ...')
Way(HUT, VILLAGE,['W','WEST'] ,'West','West by a narrow track','A short walk later ...')

#PALMFOREST
Way(PALMFOREST,STREAM,['E','EAST'],'East','East by a narrow track.',"A short walk later ...")
Way(PALMFOREST,BEACH ,['S','SOUTH'],'South','South by a narrow track','A short walk later ...')
Way(PALMFOREST,DOCKS ,['W','WEST'],'West','West by a narrow track','A short walk later ...')

#INHUT
Way(INHUT,HUT  ,['OUT','DOOR'],'Out','Out front door','The door creaks as you leave')
Way(INHUT,ATTIC,['UP','U','MAGIC'],'Up','Up a ladder to the ceiling','You climb into the ceiling')

KNIFE = Thing(INHUT,'KNIFE','A Knife','A nasty sharp knife','It is a serrated knife.  Looks sharp.',0,2)

#BEACH
Way(BEACH,PALMFOREST,['N','NORTH'],'North','North by a narrow track','A short walk later ...')

#ATTIC
Way(ATTIC,INHUT,['D','DOWN'],'Down','Down through the trap door','Going down')

#DOCKS
Way(DOCKS,PALMFOREST,['W','WEST'],'West','West by a narrow track','A short walk later ...')

BOAT = Thing(DOCKS,'Boat','A Small One-Man Craft.','The Fresh Cucumber',"          ")

#FOREST
Way(FOREST,GRAVEYARD,['N','NORTH'],'North','North by a thin, narrow track.',"A short walk later ...")

#GRAVEYARD
Way(GRAVEYARD,VILLAGE,['PASS','VILLAGE'],'Secret Passage','Underground by a dark, thin, narrow passage.',"A long crawl later ...")
Way(GRAVEYARD,CURSEDGLADE,['PATH','CURSEDGLADE'],'Disguised path','Through the cliff by a dark, thin, narrow path.',"A long walk later ...",'')

ZOMBIE = Character(GRAVEYARD, 'ZOMBIE' ,'A Zombie' ,'A rotting Zombie' ,'A rotting creature of the undead, who I believe used to be called "Bob"')
BRAIN = Thing(ZOMBIE.inventory,'BRAIN','A Brain','A bloody Brain.','Looks like it has just been removed.')

#VILLAGE
Way(VILLAGE,TAVERN,['IN','IN TAVERN'],'In','In too the Tavern.',"You enter the Tavern with it's hot, stuffy air.")
Way(VILLAGE,HUT   ,['E','EAST']      ,'East','East by a narrow track.',"A short walk later ...")
Way(VILLAGE,FOREST,['N','NORTH']     ,'North','North by a thin, narrow track.','A short walk later ...')

#CURSEDGLADE
Way(CURSEDGLADE,GRAVEYARD,['PASS','GRAVEYARD'],'Hidden Tunnel','Underground by a dark, thin, narrow passage.',"A long crawl later ...")
Way(CURSEDGLADE,STREAM,['XYZZY'],'Magic Word','Magic word unknown to adventurer','Wow! how did i get here?',True)


DIAMOND_RING = Thing(CURSEDGLADE,'DIAMOND RING','A Diamond Ring','A shiny Diamond Ring','It is a very shiny Diamond Ring.  Looks beautiful.',50)

SKELETON = Character(CURSEDGLADE,'SKELETON','A Skeleton' ,'A moist, glistening skeleton' ,"A moist, glistening creature of the undead, who I can't recognise from any features.")
BONE = Thing(SKELETON.inventory,'BONE','A Bone','A glistening Bone.','Looks like it is the last remains of the Skeleton.')
BONE.hidden = True


#TAVERN
Way(TAVERN,VILLAGE,['OUT','OUT TAVERN'],'Out','Out of the Tavern.','You leave the Tavern for the fresh air.')

ALE = Thing(TAVERN,'ALE','Some Ale','A pint of Ale','Looks good. I feel like a pint of Ale.')



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
#raw_input('Press enter to continue.')
print
print

PLAYER = Character( STREAM
                   ,'ME'
                   , name
                   ,'the main character'
                   ,'this is the guy we care about' )

Thing(PLAYER.inventory,'NOTE','a Note','an interesting small note.','It reads,"XYZZY".')

#KEEP example of how to get lists of all objects
#print
#print "Total Locations = %d " % Location.locationCount()
#Location.listLocations()
#print
#print "Total Things = %d " % Thing.thingCount()
#Thing.listThings()
#print
#print "Total Characters = %d " % Character.characterCount()
#Character.listCharacters()

PLAYER.location.displayLocation()



#perpetual loop
while True:

    PLAYER.doTurn()



