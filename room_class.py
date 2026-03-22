#basic class room
class room:
    #A class that acts as a template for all rooms in the forest
    def __init__(self,name,text,npc):
        #initialise all the attributes of the room
        self.name = name #name of room
        self.text = text #description that is printed upon entering the room
        self.npc = npc #NPCs (functionality to be added later)

    def getText(self):
        return self.text
    def getName(self):
        return self.name
    def get_Npc(self):
        return self.npc



