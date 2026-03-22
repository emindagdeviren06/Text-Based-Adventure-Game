import time
import sys
from name import name

def slow_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


class npc:
    def __init__(self, name: str, description: str, health: int, damage: int, dialogue, on_talk_speech=None,
                 on_death_speech=None):
        # Initialize the NPC with essential attributes and default dialogue options if not provided
        self.name = name
        self.description = description
        self.health = health
        self.health_max = health
        self.damage = damage
        self.dialogue = dialogue
        self.dialoguePart = 0
        if on_talk_speech is None:
            self.on_talk_speech = [f"You try to talk to {name} but they don't feel like talking"]
        else:
            self.on_talk_speech = on_talk_speech

        if on_death_speech is None:
            self.on_death_speech = f"You use your aura and rage to kill {self.name}.\n It didn't drop anything"
        else:
            self.on_death_speech = on_death_speech

    def get_name(self):
        # Return the name of the NPC
        return self.name

    def get_description(self):
        # Return the description of the NPC
        return self.description

    def get_health(self):
        # Return the current health of the NPC
        return "Current health: " + str(self.health)

    def get_maximumHealth(self):
        # Return the maximum health of the NPC
        return "Maximum health: " + str(self.health_max)

    def get_damage(self):
        # Return the damage dealt by the NPC
        return "Damage: " + str(self.damage) + "hp"

    def get_dialogue(self):
        # Return the dialogue associated with the NPC
        return self.dialogue

    def getStats(self):
        # Print all main statistics of the NPC
        slow_text(self.get_name())
        slow_text(self.get_description())
        slow_text(self.get_health())
        slow_text(self.get_maximumHealth())
        slow_text(self.get_damage())

    def getMainStats(self):
        # Display the NPC's main stats and dialogue in a formatted manner
        slow_text(self.get_name() + ",")
        slow_text('"' + self.get_description() + '" says')
        slow_text(self.get_dialogue())

    def on_talk(self):
        # Manage and return the dialogue when the player talks to the NPC, cycling through dialogue parts
        speech = self.on_talk_speech[self.dialoguePart]
        # Loop through dialogue
        self.dialoguePart += 1
        if self.dialoguePart == len(self.on_talk_speech):
            self.dialoguePart = 0

        return speech

class mainNPC(npc):
    def __init__(self, name: str, description: str, health: int, damage: int, dialogue, on_talk_speech = None):
        npc.__init__(self, name, description, health, damage, dialogue,on_talk_speech)

    def getMainStats(self):
        slow_text(self.get_name() + ",")
        # time.sleep(1.2)
        slow_text('"' + self.get_description() + '" says')
        # time.sleep(1.2)
        slow_text(self.get_dialogue())
        # time.sleep(1.7)

#define various NPCs that appear throughout the world.

Goblin = npc("Goblin:", "Weak-looking green goblin with big ears and sharp teeth", health=100, damage=3, dialogue=
"You... y-you better go... or else... I-I'll have to hurt you... I don't want to, but... but I will!",on_talk_speech=["nghhh","imma kill ya","oogoggerybagwag","I hate humans"],
             on_death_speech="You killed the Goblin\nHOw harsh the world has become that a goblin cannot\nwalk home on it's own anymore")

Raven = npc("Raven", "sharp claws", health=100, damage=7,
            dialogue="The raven lands nearby, fixing you with a cold, silent stare. Raven let's out a sharp 'Caw-Caw' ",
            on_talk_speech=["It's a raven? it caws"], on_death_speech="Cawwwwww.. a sad death caw is heard from the raven\nYou are now less lucky")

Wolf = npc("Wolf", "really vicious looking creature, staring at you menacingly", health=100, damage=5,
           dialogue="The wolf growls lowly...\n it seems to be sizing you up",on_talk_speech=["Rawwr"],on_death_speech="You killed the wolf.")

smelvin = npc("Smelvin the Goblin","small ugly goblin who is unreasonably interested in your knees",100,100000,"Hello human, lemme have a quick look a quick look at those knees", on_talk_speech=["hhhehehehheheheheh","*Smelvin is wobbling in anticipation*",
            "smelvin is literally throthing at the mouth"], on_death_speech="Ugh stupid human let me touch your knee...\nIn the knick of time you kill Smelvin...\nYou breathe a sigh of relief.")

fairy = npc("Fairy","a small flying human,\n it appears to be listening to NY state of mine",
            100,100,"In the streets I can greet ya,\n\n about blunts I teach ya Inhale deep like the words of my breath", on_talk_speech=["I never sleep, 'cause sleep is the cousin of death","Beyond the walls of intelligence, life is defined","I think of crime when I'm in a New York state of mind",
                                     "New York state of mind","Ummm","I forgot the rest of the lyrics I can't lie"],
            on_death_speech="And they say rappers are violent\nYou kill the Rapping Fairy\nIt didn't drop anything")
Kirill = npc("Kirill", "You stumble across a computer science doctor in the forest ?!?!?!",
             100,100,"Hello, welcome to my class" ,on_talk_speech=["please don't interrupt this lesson.","This doesn't seem right to you"],
             on_death_speech="I will fail you\nYou kill the Kirill\nIt didn't drop anything")

gnome = npc("Gnome", "It's a gnome... u think. he's sitting on a gnome chair?",100,100,
            "....",on_talk_speech=["...","...","go away","...","...","ugly"],on_death_speech="I was literally midning my own business. Why would you do this."
                                                                                             "You kill the Gnome\nIt didn't drop anything")

Guard = npc("Guard", "Protector of the mighty castle, saviour of the lords", health=100, damage=4, dialogue="Be careful, it is pretty dangerous!")

HeadMaid = mainNPC("The Headmaid", "The Assistant of the Castle", 90, 100, "I am the carer of this mighty castle!\n",

                   on_talk_speech = [f'''Hello {name}, welcome to Veil of vengeance! To pick up an item, simply type take <item name>,
to drop an item type drop <item name> and to use an item type use <item name>''',"Dost thou need any help?"])


Grekthor = mainNPC("Grekthor The Goblin", "Wisdom of the ancient alps", 100, 100,
                   "From whence hast thou come, O mortal creature?")

Magnar = mainNPC("Magnar The Third", "Ruler of the eternal kingdom", 1000, 1000, "Welcome traveller, to my castle!",
                 on_talk_speech = ["Track Grekthor the Sage and make sure to avenge your sister!", "Remember, you can never trust those filthy goblins"])

Princess = mainNPC("Princess Elowen", "Princess of the mighty kingdom", 90, 100, "Hey, do you like horses?\n",
                   on_talk_speech = ['''Go and avenge your sister, come on you don't have time!''', 'What are you waiting for?'])
Prince = mainNPC("Prince Maximus", "Next heir of the monarch", 90, 100, "I do not have time for you",
                 on_talk_speech = ["Get out of my room peasant!", "Guards!"])

Priest = mainNPC("The Grand Priest", "The ally of faith", 90, 100, "Hast thou come to learn, my child?",
                 on_talk_speech = ["""Do not give in on your desires my child""", """Those whom you 
think are your ally can turn out to be thy foe,
trust in God more than you trust in those in power"""])

#bob the waiter :(

bob_the_waiter = mainNPC("Bob the Waiter", "A proper geezer to give u beer", 10, 10, "Ahhhhh j'n'pais francais",
                         on_talk_speech = ["Mon cieur, my food is the best", "oui oui oui I have a rat to help me cooke ehh my meals.","His name is rattus rattus"])




