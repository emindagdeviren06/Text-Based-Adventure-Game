import random
from room_class import *
from castleNPCs import *

"""
Documentation:

This file contains the room class
The forest_room subclass
and the generate forest function.

The room class contains basic skeleton for rooms as a class
it is defined by:
room = room(name of room ,description of room, and npcs in the room)
it has basic get functions so far

The forest_Room class is a subclass specific to the forest location.
"""

#define any room that is in the forest
#subclass of room
class forest_Room(room):
    def __init__(self,name,text,npc,location, exits , items = None, special_commands = None ):
        #initialise parent class attributes
        room.__init__(self,name,text,npc)
        #define location in 2d array location[0] refers to it's position along the vertical axis
        #wheras location[1] refers to it's position on the horizontal axis
        self.location = location
        #define the exits.
        self.exits = exits
        #assign items
        self.items = items
        #assign special commands
        if special_commands is None:
            self.special_commands = []
        else:
            self.special_commands = special_commands

        #add attack to special_commands if an NPC is in the room
        if len(npc) >= 1:
            self.special_commands.append("attack")


    #assign exits to each room once the 2d array has already been created
    def assign_Exits(self,map_Width,map_Height,forest):
        if self.location[1] != 0:
            #any room on the left side of the 2d array cannot go west
            self.exits["west"] = forest[self.location[0]][self.location[1]-1]

        if self.location[1] != map_Width-1:
            #any room on the Right side of the 2d array cannot go east
            self.exits["east"] = forest[self.location[0]][self.location[1]+1]

        if self.location[0] != 0:
            #any room on the top side of the 2d array cannot go north
            self.exits["north"] = forest[self.location[0]-1][self.location[1]]

        if self.location[0] != map_Height-1:
            #any room on the top side of the 2d array cannot go south
            self.exits["south"] = forest[self.location[0]+1][self.location[1]]

    #getExits function prints exits
    def get_Npc(self):
        return self.npc
    def print_Exits(self):
        for i in self.exits:
            print(f"You can Go {i.capitalize()}")

    def enter_Room(self):
        self.text = ""

    def print_Coordintes(self):
        print(self.location)

    #define a method to test if there is an item room items
    def contains_item(self,item_id):
        item_in_list = False
        for i in self.items:
            if i.get_id() == item_id:
                item_in_list = True
            else:
                continue
        return item_in_list


    #define a method to remove an item

    def remove_Item(self,item_id):
        for i in self.items:
            if i.get_id() == item_id:

                self.items.remove(i)
            else:
                continue

    #drop an item into the room
    def drop_Item_Object(self,item):
        self.items.append(item)#

    #another get method
    def get_Name(self):
        return self.name

    def get_Exits(self):
        return self.exits

    def get_Items(self):
        return self.items

    def get_Description(self):
        return self.text

    def get_Special_Commands(self):
        return self.special_commands

    #add NPC method
    def add_NPC(self,NPC):
        self.npc.append(NPC)



#generates random names for the woodland rooms
def generate_Room_Name():
    randomPart1 = ["Silent","moonlit", "Eerie", "Haunting", "Haunted", "Blood Stained", "Misty", "Barren", "Wooded",
                   "Creeping","Heavenly","Blighted","Foggy"]
    randomPart2 = ["Heath", "Quagmire", "Mire", "Jungle", "Hollow", "Marshes", "Foothill", "Swamp", "River",
                   "Wastes"
        , "Clearing","Taiga","flats","Temple","Quarry","Gorge","bayou","prairie","meadow",
                   "Valley","badlands","moor"]
    name = ""
    name += random.choice(randomPart1)
    name += " "
    name += random.choice(randomPart2)
    return name

#function used to generate a 2d array of Forest Rooms. of size N by N.
def generate_Forest(width_Of_Map,depth_of_Map):
    #list containing forest NPCs
    NPCs = [Wolf,Kirill,fairy,Raven,Goblin]

    rooms = []

    forest_room_names = []

    #creates a list of unique names for each room in the forest
    for i in range(width_Of_Map*depth_of_Map):
        newRoomName = generate_Room_Name()
        while newRoomName in forest_room_names:
            newRoomName = generate_Room_Name()
        forest_room_names.append(newRoomName)

    #for each room in the array create a forest room
    count = 0
    for i in range(depth_of_Map):
        row = []
        for j in range(width_Of_Map):

            #generate a room in the coordinate of the forest where there is a 1/4 chance of generating a random NPC
            #at that location
            npcSpawn = random.randint(1,3)
            if npcSpawn == 2:
                row.append(forest_Room(forest_room_names[count],"A room in the forest, it's probably quite scary",
                                       [random.choice(NPCs)],[i,j],{},items=[]))
            else:
                row.append(forest_Room(forest_room_names[count], "A room in the forest, it's probably quite scary",
                                       [], [i, j], {}, items=[]))

            count += 1
        rooms.append(row)


    #adding special rooms
    grekthors_layer = forest_Room(
        "Grekthor's Lair",
        "There is a stench of goblin in the air...\nIt smells of something between Vanilla and rotten oranges"
        " You feel you are reaching the end of your journey",
        [Grekthor],
        [width_Of_Map-1,depth_of_Map-1],
        {},
        items=[],
        special_commands = ["spare"]
    )

    rooms[width_Of_Map-1][depth_of_Map-1] = grekthors_layer

    #once created assign the exits of each room so all rooms can be accessed from each other
    for i in range(depth_of_Map):
        for j in range(width_Of_Map):
            rooms[i][j].assign_Exits(width_Of_Map, depth_of_Map,rooms)


    return rooms

#add NPC to forest function
def add_NPC_to_forest(forest,npc,coordianate):
    forest[coordianate[0]][coordianate[1]].add_NPC(npc)

#generate the forest

forest = generate_Forest(5,5)



