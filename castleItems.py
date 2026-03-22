from Castlemap import final_map
from Forestmap3 import forest_map_print
class item:
    # class defining attributes of a basic item
    def __init__(self, id, name, weight, description, on_drop_text="",on_use_text="", on_take_text = ""):
        self.id = id
        self.name = name
        self.weight = weight
        self.description = description
        # defining the ON_drop text for an item
        if on_drop_text == "":
            self.on_drop_text = f"You drop the {self.name} and it falls to the floor with a slight whistling sound"
        else:
            self.on_drop_text = on_drop_text

        if on_use_text == "":
            self.on_use_text = f"You use the {self.name}"
        else:
            self.on_use_text = on_use_text


        if on_take_text == "":
            self.on_take_text= f"You take the {self.name}"
        else:
            self.on_take_text = on_take_text


    # defining get methods
    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_weight(self):
        return self.weight

    def on_drop(self):
        return self.on_drop_text

    def on_use(self):
        return self.on_use_text

    def on_take(self):
        return self.on_take_text


fist = item("fist", "Fist", 0, "It's your fist bro, go beat someone up",
            on_take_text="You take the fist and surgically reattach the arm to your arm.\n It's at a slight angle but "
                         "mostly functional.")

castle_map = item("castle-map",
                  "Map of the Castle",
                  0,
                  "A map that shows the map of the whole castle.",
                  on_use_text=final_map)

cross = item("cross", "The cross", 0.6, """The cross in the chapel is made of gold, dark wood, and diamond.
    It might not be of use against goblins, but it stands as a solemn focal point for reflection and prayer.""",
             "You attempt to drop your fist.\n Wow you actually did it. You now have only one arm."
             )

item_cross = item(
    "cross",

    "The cross",

    0.6,
    """The cross in the chapel is made of gold, dark wood, and diamond.
    It might not be of use against goblins, but it stands as a solemn focal point for reflection and prayer."""
)

item_webs = item(
    "webs",

    "Webs",

    0.2,

    """It does not have any use, 
    but may give you luck in the future """
)

item_forestmap = item(
    "forestmap",

    "Map of the Forest",

    0.0,

    """ You unlocked the forest map! You can now access the forest area, 
    where you will be able to fight goblins. You will need a weapon,
    if you do not already have one!""",
    "But you really really need that. To like go to the forest. Personally I wouldn't recommend it.",
    on_use_text=forest_map_print
)

item_note = item(
    "note",

    "Prince's note",

    0.8,

    """

    The note says:
To the Head Maid,
Please remember to arrange for my horse to be ready at dawn. 
I have important matters to attend to, and I cannot be delayed.

- Your Majesty.""",
    "The note gently falls to the ground"
)

item_dagger = item(
    "dagger",

    "The Royal Dagger",

    0.0,

    """The royal dagger is used to kill goblins, 
    though its true use lies in the hands of its owner""",
    "You drop the dagger on your toe. You now only have 9 toes."
    # maybe add easter egg where the number of toes decreases each time u drop a dagger.
)

item_toiletpaper = item(
    "toiletpaper",

    "A toilet paper",

    0.6,

    """The toilet paper is not of use for combat, 
    although you can still pick it up and use it for ver important purposes."""
)

item_rose = item("rose",

                 "Beautiful Rose",

                 0.2,

                 """The rose will certainly improve your smell,
                 might even help you with the princess""")
