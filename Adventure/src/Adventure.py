from Location import Location

CurrentLocation = "Stream"
Decis    = "Go"
INVENTORY = "Inventory"
StuffDesc = ["Lamp","Serrated knife","Apple","Water","Rations","Ale"]
StuffLocation = ["InHut","InHut","Tavern","Stream","Stream","Tavern"]
money = 0
FIRST_STUFF = 0
MAX_STUFF = 6
TERMINATE = "STOP"

#InHut = ['In Hut','You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.',{'OUT':"hUT"},StuffDesc[0]]
Tavern = Location("Tavern",
                  'you have arrived at a tavern bustling with people. It is called the Jolly Pig. A door leads out.',
                  {'OUT':'Village'},
                  [StuffDesc[3],StuffDesc[5]])
InHut = Location( 'In Hut',
                  'You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.',
                  {'OUT':"Hut"},
                  [StuffDesc[0],StuffDesc[1]] )

Village = Location('Village',
                   'You have arrived at a village. A path leads East.',
                   {'EAST':'Hut','IN TAVERN':'Tavern'},
                   [])
Hut = Location('Hut',
               'You are standing outside a little hut.  The front door is ajar.  A path leads South and West.',
               {'SOUTH':'Stream','WEST':'Village',
                'DOOR':'In Hut'},[])
Stream = Location('Stream',
          'You are standing by a stream. The stream runs NE to SW. A path leads North.',
          {'NORTH':'Hut'},
           [StuffDesc[3], StuffDesc[4]])
current_location = Stream

#current_location.visit()
print current_location.visit()
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
      if CurrentLocation == "Stream" :
          print Stream.Description
      elif CurrentLocation == "Hut" :
          print 'You are standing outside a little hut.  The front door is ajar.  A path leads South and West.'
      elif CurrentLocation == "InHut" :
          print 'You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.'
      elif CurrentLocation == "Village":
          print 'You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maye you could get some ale and food. A path leads East.'
      elif CurrentLocation == "Tavern":
            print 'you have arrived at a tavern bustling with people. It is called the Jolly Pig. A door leads out.'
                        
      #list any stuff which has a location matching where we are now.     
      is_stuff_there = False
      for i in range( FIRST_STUFF, MAX_STUFF ):        
          if StuffLocation[i] == CurrentLocation:
              is_stuff_there = True
      if is_stuff_there == True:                        
          print 'There is also ..'
      for i in range( FIRST_STUFF, MAX_STUFF ):                  
          if StuffLocation[i] == CurrentLocation:
            print " " + StuffDesc[i]                  
           
      Decis = raw_input ('What now?')
      Decis = Decis.upper()
 
    #process their input
    
      if CurrentLocation == "Stream" and Decis == 'N' or Decis == 'NORTH':
            CurrentLocation = "Hut"
            print 'Off I go'
      elif CurrentLocation == "Hut" and Decis == 'S' or Decis == 'SOUTH':
            CurrentLocation = "Stream"  
            print 'Off I go'
      elif CurrentLocation == "Hut" and Decis == 'W' or Decis == 'WEST':
            CurrentLocation = 'Village'
            print 'Off I go'
      elif CurrentLocation == "Hut" and (Decis == 'IN' or Decis == 'DOOR'):
            CurrentLocation = "InHut"  
            print 'In I go'
      elif CurrentLocation == "InHut" and (Decis == 'OUT' or Decis == 'DOOR'):
            CurrentLocation = "Hut"  
            print 'Out I go'
      elif CurrentLocation == "Village" and Decis == 'E':
            CurrentLocation = 'Hut'
            print 'Off I go'  
      elif CurrentLocation == "Village" and Decis == 'IN TAVERN':
            CurrentLocation = "Tavern"
            print "In I go"
      elif CurrentLocation == "Tavern" and (Decis == 'OUT' or Decis == 'DOOR'):
            CurrentLocation = "Village"
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
            StuffName = StuffDesc[i].upper()

            if StuffLocation[i] == CurrentLocation and (StuffName == Thing or Thing == 'ALL'):
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
                StuffLocation[i] = CurrentLocation
                DroppedIt = True
                print 'Dropped ' + StuffDesc[i] + '!' 
            elif StuffLocation[i] == CurrentLocation and StuffName == Thing:
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
            

 
