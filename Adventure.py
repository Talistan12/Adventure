Location = "Stream"
Decis    = "Go"
INVENTORY = "Inventory"
StuffDesc = ["Lamp","Serrated knife","Apple","Water","Rations"]
StuffLocation = ["InHut",INVENTORY,"Stream","Stream","Stream"]
FIRST_STUFF = 0
MAX_STUFF = 5
TERMINATE = "STOP"

current_location = ['Stream',['NORTH','Hut'], ]

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

while Decis != TERMINATE:
      print
      #Tell the adventurer where they are.
      if Location == "Stream" :
          print 'You are standing by a stream. The stream runs NE to SW. A path leads North.'
      elif Location == "Hut" :
          print 'You are standing outside a little hut.  The front door is ajar.  A path leads South and West.'
      elif Location == "InHut" :
          print 'You are standing inside a dark smelly little hut with a trap-door in the floor and a ladder to the attic.  A door leads out.'
      elif Location == "Village":
          print 'You have arrived at a village. A path leads East.'
                        
      #list any stuff which has a location matching where we are now.     
      is_stuff_there = False
      for i in range( FIRST_STUFF, MAX_STUFF ):        
          if StuffLocation[i] == Location:
              is_stuff_there = True
      if is_stuff_there == True:                        
          print 'There is also ..'
      for i in range( FIRST_STUFF, MAX_STUFF ):                  
          if StuffLocation[i] == Location:
              print StuffDesc[i]                 
           
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
      elif Decis == 'N' or Decis == 'NORTH' or Decis == 'SOUTH' or Decis == 'EAST' or Decis == 'WEST' or Decis == 'S' or Decis == 'E' or Decis == 'W':
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
        #Check whether the Stuff is in your Inentory  
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
                print "Don't have " +  StuffDesc[i] + ' but I can see it!'
                #DroppedIt = True
                
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
                    print StuffDesc[i]
                
      elif Decis == TERMINATE:
                print 'You did not like our game? What a shame.. what a shame..'
      else:
            print 'Huh?'
            

 
