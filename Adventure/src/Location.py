class Location:
      Name = ""
      Description = ""
      Objects = []
      Exits = {}
    
    # Constructor for Location
    # Exit s is a dictionary of Command -> New location
      def __init__(self, n, d, e, o):
          self.Name = n
          self.Description = d
          self.Exits = e
          self.Objects = o
        
    # Called when a character visits this location
    # Print description
    # Lists available objects
    # Ask for input and return the name of a new location to go to
      def visit(self):
          print self.Description
          if len(self.Objects) > 0:
              print 'There is also ..'
              for i in range(len(self.Objects)):
                  print self.Objects[i]
                
          Decis = raw_input ('What now?')
          Decis = Decis.upper()
 
      #process their input
          moving = False
          if Decis == 'N':
                Decis = 'NORTH'
                moving = not moving
          elif Decis == 'S':
                Decis = 'SOUTH'
                moving = not moving
          elif Decis == 'W':
                Decis = 'WEST'
                moving = not moving
          elif Decis == 'IN':
                Decis = 'DOOR'
                moving = not moving
          elif Decis == 'OUT':
                Decis = 'DOOR'
                moving = not moving
          elif Decis == 'E':
                Decis = 'EAST'
                moving = not moving
          elif Decis == 'OUT':
                Decis = 'DOOR'
                moving = not moving
          if moving:
                return self.Exits[Decis]
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
    
            