class Character:
    'A player or NPC in the game'
#    name = ""
#    location = None
#    inventory = None
    
    def __init__(self, name, location, inventory):
        self.name = name
        self.location = location
        self.inventory = inventory

