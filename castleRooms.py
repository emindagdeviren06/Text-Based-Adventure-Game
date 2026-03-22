from room_class import room
from castleItems import *
from castleNPCs import *



class castleRoom(room):
    # A subclass defining the room in a castle.
    #Attributes of the Castle Room are
    # Name
    # Text description (this text will appear when the player enters the room)
    #npcs (a list of NPCs that are in the room at that time)
    # items (a list of items contained within the room)
    def __init__(self, name, text, npc, exits,items,special_commands = ()):
        room.__init__(self,name,text,npc)
        self.exits = exits
        self.items = items
        if special_commands == ():
            self.special_commands = []
        else:
            self.special_commands = special_commands




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

    def drop_Item_Object(self,item):
        #method to drop items from the inventor
        self.items.append(item)

    def enter_Room(self):
        #deletes the description of the room when u enter the room
        self.text = ""

    #define the get methods
    def get_Exits(self):
        return self.exits

    def get_Items(self):
        return self.items

    def get_Description(self):
        return self.text

    def get_Name(self):
        return self.name

    def getName(self):
        return self.name

    def get_Special_Commands(self):
        return self.special_commands


#Creating an Object for each room in the castle

room_village = castleRoom(f"{name}'s House",
f"""{name}'s house is located within the village of the Alberics. 
It is made of bricks and the roof is completely shut by the wooden trees,
the house might not be deluxe, but it does give eery vibes of a main character.""",
[],
{"forwardthroughthepath": "greatHall"},

[])

room_hall = castleRoom("Great Hall",
"""You step into the Great Hall, where the air is thick 
with the scent of roasted meats and the sound of laughter echoes off the stone walls. 
Flickering torches cast dancing shadows on the rich tapestries that recount tales of heroism.
Long tables are set for a feast, and a grand fireplace crackles warmly, 
inviting you to join the festivities and perhaps uncover secrets hidden among the revelers.
You can go to the rooms on your left, or the rooms on your right. The exit is behind you.""",
[HeadMaid],
{"back": "exit", "right": "toilet", "left": "chapel", "forwardleft": "storeRoom", "forwardright": "princeroom",
"tooforwardleft": "kitchen", "tooforwardright": "princessRoom", "topright":"kingRoom"},
[])

room_chapel = castleRoom("The Chapel",
"""As you enter the Chapel, a serene hush envelops you, 
 broken only by the soft flicker of candlelight illuminating the stone altar.
 Stained glass windows filter the sunlight into a kaleidoscope of colors,
 casting vibrant patterns on the cold floor. 
 The air is fragrant with incense, 
 creating a sense of peace and reflection,
 inviting you to pause and contemplate in this sacred sanctuary.""",
[Priest],
{"left": "dungeon", "right":"greatHall"},
[item_cross],
special_commands=[]
)
room_kitchen = castleRoom(
"The Kitchen",
"""The Kitchen bustles with activity, 
filled with the rich aroma of simmering stews and baked bread. 
Flames dance in the hearth, while chefs chop and stir, 
creating a warm and inviting atmosphere that promises hearty meals.""",

[bob_the_waiter],
{"left": "courtyard", "right":"greatHall"},
[]
)

room_dungeon = castleRoom(
"The Dungeon",
"""The Dungeon looms dark and foreboding, 
with cold stone walls echoing the faint sound of dripping water.
Flickering torchlight reveals rusty chains and shadowy corners,
creating an atmosphere of dread and mystery.
The air is heavy with the scent of dampness and decay, 
reminding you of the secrets and stories held within its grim confines.""",
[Guard],
{"right": "chapel", "left": "courtyard"},
[item_webs],
["leave"]
)


room_princess = castleRoom(
"Princess's Room",

"""The Princess's Room exudes elegance and charm, 
adorned with soft silks and delicate tapestries that reflect her refined taste.
A lavish canopy bed invites rest, while a writing desk sits near a window,
offering a view of the castle gardens. 
The gentle glow of candles casts a warm light, 
creating a serene atmosphere filled with the scent of blooming flowers.""",
[Princess],

{"forward": "greatHall"},

[item_forestmap]
)

room_prince = castleRoom(
"Prince's Room",

"""The Prince's Room is a blend of sophistication and adventure, 
featuring rich fabrics and ornate furnishings that reflect his royal status. 
A sturdy wooden desk holds maps and scrolls, hinting at his aspirations for exploration and leadership.
The room is well-lit by a grand window, 
offering views of the sprawling castle grounds, while the walls are adorned with trophies and relics from his conquests.""",

[],
{"forward": "greatHall"},

[item_note]
)

room_king = castleRoom(
"King's Room",

"""The King's Room has an air of mystery, 
with its dark wooden furnishings and shadows that linger in the corners. 
Rich tapestries depicting ancient battles hang on the walls,
whispering secrets of the past. 
An intricately carved four-poster bed looms ominously in the center, 
while the flickering candlelight casts strange patterns, 
making the room feel alive with hidden stories.
A heavy, velvet curtain drapes over the window,
blocking out the daylight and adding to the sense of seclusion and intrigue.""",

[Magnar],

{"forward": "greatHall"},

[],
special_commands=["attack"])

room_toilet = castleRoom(
"The Toilet",


"""The Toilet is a small, unadorned room with stone walls and a basic wooden seat.
A flickering candle provides the only light, casting shadows that make the space feel a bit eerie.
Despite its simplicity, the room offers a sense of privacy, a quiet escape from the bustling castle.""",

[],
{"forward": "greatHall"},

[item_toiletpaper]
)

room_courtyard = castleRoom(
"The Courtyard",

"""The Courtyard is an open space bathed in sunlight, 
surrounded by the castle's tall stone walls. 
Colorful flowers bloom in neat gardens, 
while a few trees provide shade for visitors.
The sound of birds chirping fills the air, 
creating a peaceful atmosphere, 
and cobblestone paths lead to various areas of the castle,
inviting exploration and relaxation..""",

[],

{"forwardleft": "kitchen", "forward": "storeRoom", "forwardright":"dungeon",
"left": "guardtower", "aroundleft": "watchtower", "right": "royaltower", "aroundright": "librarytower"},

[item_rose]
)

room_storeroom = castleRoom(
"The Store Room",

"""The Store Room is a tidy space with wooden shelves neatly lined with jars, sacks, and supplies.
The air is filled with the fresh scent of herbs and dried goods, 
creating an inviting atmosphere. 
Sunlight filters through a small window,
illuminating the organized shelves, making it easy to find what you need in this well-kept storage area.""",

[Guard],

{"right": "greatHall", "left": "courtyard"},

[]
)

room_tower1 = castleRoom(
"Watch Tower",


"""The Watchtower stands tall and slender,
offering a commanding view of the surrounding landscape.
Narrow slits for windows provide ample lookout points,
allowing guards to keep watch for any approaching threats.
The tower's stone walls are weathered yet sturdy,
a testament to its role as a vigilant sentinel for the castle.""",

[Guard],

{"back": "courtyard"},

[]
)

room_tower2 = castleRoom(
"Library Tower",

"""The Library Tower features a spiral staircase that ascends to a cozy sanctuary filled with ancient tomes and scrolls. 
Soft light filters through tall windows, 
illuminating the rows of books lining the shelves. 
This tranquil space invites quiet reflection and study, 
making it a cherished retreat for scholars and curious minds alike.""",

[Guard],

{"back": "courtyard"},
[]
)


room_tower3 = castleRoom(
"Guard Tower",

"""The Guard Tower is adorned with battlements and thick stone walls, 
creating an imposing presence. Sentries patrol its heights,
ensuring the safety of the castle and its inhabitants.
The air is filled with the sound of armor clanking and the occasional call of duty,
as watchful eyes scan the grounds below for any signs of danger.""",

[Guard],

{"back": "courtyard"},

[]
)

room_tower4 = castleRoom(
"Royal Tower",

"""The Royal Tower boasts a rounded top and elegant design,
housing the royal chambers in serene luxury.
Soft fabrics drape from the windows,
and rich furnishings create an atmosphere of comfort. 
With stunning views of the gardens and castle grounds, 
this tower offers a peaceful retreat for the royal family, 
combining beauty and tranquility in one space..""",

[],

{"back": "courtyard"},

[]
)

room_exit = castleRoom(
"Path",

"""The exit path winds through the castle gardens,
bordered by vibrant flowers and smooth cobblestones.
It provides a clear route out of the castle,
offering a serene atmosphere as you walk.""",
[],

{"forward":"greatHall"},

[]
)


rooms = {
    "greatHall": room_hall,
    "chapel": room_chapel,
    "kitchen": room_kitchen,
    "dungeon": room_dungeon,
    "princessRoom": room_princess,
    "princeRoom": room_prince,
    "kingRoom": room_king,
    "toilet": room_toilet,
    "courtyard": room_courtyard,
    "storeRoom": room_storeroom,
    "watchtower": room_tower1,
    "librarytower": room_tower2,
    "guardtower": room_tower3,
    "royaltower": room_tower4,
    "exit": room_exit
}
