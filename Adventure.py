Location = "Stream"
Decis    = "Go"
INVENTORY = "Inventory"
StuffDesc = ["Candle","Knife","Apple","Water","Rations","Ale"]
StuffLocation = ["InHut","InHut","Tavern",INVENTORY,INVENTORY,"Tavern"]
FIRST_STUFF = 0
MAX_STUFF = 6
TERMINATE = "STOP"

print 'You are a wanderer whose aim in life is too collect things. Your goal. Collect all objects in the region. There are 6 in total. FIND THOSE OBJECTS!'

while Decis != TERMINATE:
      print
      #Tell the adventurer where they are.
      if Location == "Stream" :
          print 'You are standing by a stream. The stream runs NE to SW. A path leads North.'
      elif Location == "Hut" :
          print 'You are standing outside a little hut.  The front door is ajar.  A path leads South and West.'
      elif Location == "InHut" :
          print 'You are standing inside a dark smelly little hut.  A door leads out.'
      elif Location == "Village":
          print 'You have arrived at a village bustling with life. There is a tavern which seems to be booming in buisness. Maye you could get some ale and food. A path leads East.'
      elif Location == "Tavern":
            print 'you have arrived at a tavern bustling with people. It is called the Jolly Pig. A door leads out.'
                        
      #list any stuff which has a location matching where we are now.                 
      print 'There is also ..'
      for i in range( FIRST_STUFF, MAX_STUFF ):                  
        if StuffLocation[i] == Location:
            print " " + StuffDesc[i]                 
           
      Decis = raw_input ('What now?')
      Decis = Decis.upper()
 
    #process their input
    
      if Location == "Stream" and Decis == 'N':
            Location = "Hut"
            print 'Off I go'
      elif Location == "Hut" and Decis == 'S':
            Location = "Stream"  
            print 'Off I go'
      elif Location == "Hut" and Decis == 'W':
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
      elif Decis == 'N' or Decis == 'S' or Decis == 'E' or Decis == 'W' or Decis == 'NW' or Decis == 'NE' or Decis == 'SW' or Decis == 'SE':
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
                
        if not GotIt:
            print "what? I can't pick " + Thing + " up!"

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
                
        if not DroppedIt:
            print "what? I don't have " + Thing + "!"
            
            
      elif Decis == 'LOOK':
            print "I'll repeat myself then, shall I?"
      elif Decis == 'INVENT':
            #list any stuff which has a location of "Inventory"
            print 'You are currently holding'
            for i in range( FIRST_STUFF, MAX_STUFF ):                  
                if StuffLocation[i] == INVENTORY:
                    print " " + StuffDesc[i]
                
      elif Decis == TERMINATE:
                print 'You did not like our game? What a shame.. what a shame..'
      else:
            print 'Huh?'
            

 
