import pygame
from castleItems import *
from castleItems import *
from castleNPCs import *
from Generating_Forest_Function import *
from castleRooms import *
from name import name
from Dialogue import *
from goodending import *
from secretending import *
import time
import sys
from button import kill_button
import combat


import os
#get filepath
file_path = os.path.dirname(os.path.abspath(__file__)) + """\\"""

pygame.init()
pygame.mixer.init()

ambient_music_path = file_path+"Ambient.mp3"
try:
    pygame.mixer.music.load(ambient_music_path)
    pygame.mixer.music.set_volume(0.5)  # Set volume for the ambient OST
    pygame.mixer.music.play(-1)  # Loop the ambient OST
except pygame.error as e:
    print(f"Error loading ambient music: {e}")


def play_king_dialogue():
    # Initialize Pygame and the mixer
    try:
        pygame.mixer.music.stop()
        dialogue_path = file_path+"KingDialogue.mp3"
        pygame.mixer.music.load(dialogue_path)
        pygame.mixer.music.set_volume(1.0)  # Set volume for dialogue
        pygame.mixer.music.play()

        slow_text(kingDialogue1, delay=0.0755)
        slow_text(kingDialogue2, delay=0.0000005)
        slow_text(kingDialogue3, delay=0.0755)

        while pygame.mixer.music.get_busy():  # Wait for the dialogue to finish
            pygame.time.Clock().tick(3)
    except pygame.error as e:
        print(f"Error playing king dialogue: {e}")
    finally:
        pygame.mixer.music.load(ambient_music_path)  # Reload ambient music
        pygame.mixer.music.play(-1)


def play_another_audio(file_path, dialogue_text,special_King_Speech = None):
    pygame.mixer.music.stop()
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(0)

#Display text while the audio plays
        if special_King_Speech is None:
            slow_text(dialogue_text, delay=0.074)
        else:
            slow_text(dialogue_text, delay=0.074)
            slow_text(special_King_Speech[0],0.00000005)
            slow_text(special_King_Speech[1], delay = 0.074)

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(3)
    except pygame.error as e:
        print(f"Error loading {file_path}: {e}")
    finally:
        pygame.mixer.music.load(ambient_music_path)
        pygame.mixer.music.play(-1)


def play_dialogue(file_path):
    # Pause the current background music to play dialogue
    pygame.mixer.music.pause()
    try:
        # Load the dialogue audio file
        pygame.mixer.music.load(file_path)
        # Set volume to full for dialogue clarity
        pygame.mixer.music.set_volume(1.0)
        # Play the dialogue audio
        pygame.mixer.music.play()

        # Wait until the dialogue audio has finished playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Limit loop speed to reduce CPU usage
    finally:
        # Resume previous music after dialogue is done
        pygame.mixer.music.unpause()


# Simple input cleanup function
def clean(text):
    # Convert input text to lowercase for consistency
    text = text.lower()
    return text


# Function to print text with a delay for dramatic effect
def slow_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)  # Print each character individually
        sys.stdout.flush()  # Flush output to display immediately
        time.sleep(delay)  # Add a delay between characters
    print()  # Add newline after text is complete


# Function to move the player within the castle
def move_In_Castle(currentRoom, direction):
    # Set the new current room based on the specified direction
    currentRoom = rooms[currentRoom.get_Exits()[direction]]
    return currentRoom

def move_In_Forest(currentRoom, direction):
    currentRoom = currentRoom.get_Exits()[direction]
    return currentRoom

def print_Items(items):
    fstring = "You have "
    if len(items) == 0:
        fstring = ("")
        return fstring
    else:
        for i in items:
            fstring += i.get_id()
            fstring += ", "
        fstring = fstring[0:-2]
        fstring += "."
        return fstring


# take command
# takes an item_id as an input and drops it as an output. lol

def execute_take(item_id):
    # Declare global variables for accessing inventory and current room data
    global inventory
    global currentRoom

    # Check if the specified item is present in the current room
    if not currentRoom.contains_item(item_id):
        slow_text(f"You cannot take {item_id}")  # Notify if item is not present
    else:
        # Iterate through items in the current room to find the specified item
        for i in currentRoom.get_Items():
            if i.get_id() == item_id:
                # Add the item to inventory and remove it from the room
                inventory.append(i)
                currentRoom.remove_Item(item_id)


def execute_Drop(item_id):
    # Declare global variables for accessing inventory and current room data
    global inventory
    global currentRoom

    # Create a list of item IDs currently in inventory
    inventory_Ids = [i.get_id() for i in inventory]

    # Check if the item exists in inventory
    if item_id not in inventory_Ids:
        slow_text(f"You cannot drop {item_id}, it is not in your inventory!")
    else:
        # Iterate through inventory to find and drop the specified item
        for i in inventory:
            if i.get_id() == item_id:
                inventory.remove(i)  # Remove the item from inventory
                currentRoom.drop_Item_Object(i)  # Place item back in room
                slow_text(i.on_drop())  # Display item's drop message


def get_item_from_inventory_by_id(item_id):
    # Declare global variable for accessing inventory
    global inventory

    # Search for item by ID within inventory
    for i in inventory:
        if i.get_id() == item_id:
            return i  # Return item object if found

    return False  # Return False if item is not in inventory


# auto generated forest

# basic player functionality and variable
inventory = [fist, castle_map]
inCastle = True

welcomeMessage = slow_text(f"Welcome {name}, to Veil of Vengeance!")

currentRoom = room_village
print_speed = 0.05
good_ending = False
kingDialogueCount = 0
princessDialogueCount = 0
goblinDialogueCount = 0
slow_text("Type go {direction} to navigate the map.")
slow_text("Type talk to talk to the NPC.")


while True:
    # if the player has changed rooms since last go print out the rooms

    slow_text(f"You are in {currentRoom.getName()}")
    print("")
    slow_text(currentRoom.get_Description().strip(), print_speed)
    currentRoom.enter_Room()
    print("")

    # print out NPC names

    # NPC Dialogue section
    for i in currentRoom.get_Npc():
        # Display main stats for each NPC present in the current room
        i.getMainStats()

    # Check if the player has entered the princess's room for the first time
    if currentRoom == room_princess and princessDialogueCount == 0:
        # Play the princess's dialogue audio
        play_another_audio(file_path + "PrincessDialogue.mp3", princessDialogue1)
        princessDialogueCount += 1  # Increment count to avoid replaying

    elif currentRoom == room_hall and kingDialogueCount == 0 and good_ending == False:
        # Play the king's dialogue if in the hall for the first time
        play_king_dialogue()
        kingDialogueCount += 1  # Increment count for dialogue control

    # Print available exits in the current room for navigation
    if inCastle == True:
        """Due to unforeseen circumstances, the rooms in a forest 
        room actually point to the object they refer to rather than 
        a dictionary, requiring slightly different methods to print 
        everything correctly."""

        for direction in currentRoom.get_Exits():
            room_name = currentRoom.get_Exits()[direction]  # Get the name of the room in the specified direction
            slow_text(f"You can go {direction} to go to {room_name}", print_speed)  # Inform player of possible exit

            print("")  # Print newline for spacing

    elif inCastle == False:
        # If not in the castle, list exits from the forest or other area
        for direction in currentRoom.get_Exits():
            room_name = currentRoom.get_Exits()[direction].get_Name()
            slow_text(f"You can go {direction} to go to {room_name}", print_speed)

            print("")

    # Print out a list of items available to take in the current room
    for i in currentRoom.get_Items():
        slow_text(f"You can take {i.get_id()}", print_speed)

    # Display dialogue options with NPCs present in the room
    for i in currentRoom.get_Npc():
        slow_text(f"You can talk to {i.get_name()}", print_speed)

    # Print out the player's current inventory
    for i in inventory:
        slow_text(f"You have {i.id}")

    print("")

    # basic command list.
    possible_commands = ["go", "take", "drop", "use", "talk"]

    # special commands based on rooms
    possible_commands += currentRoom.get_Special_Commands()

    try:
        #special print commands based on room
        if currentRoom.get_Name() == "Grekthor's Lair":
            slow_text("It is finally time to meet with GREKTHOR THE SAGE", print_speed)
            slow_text("You think you could probably kill him if you stab him", print_speed)
            slow_text("But do you want to?????", print_speed)
            print(kill_button)
    except:
        pass

    #special commands based on rooms
    if "leave" in possible_commands:
        slow_text("Type leave to leave the castle now")

    if "attack" in possible_commands:
        slow_text("Type Attack to kill " + currentRoom.get_Npc()[0].get_name())

    if "spare" in possible_commands:
        slow_text("Type Spare to spare not Kill GREKTHOR (He does look kinda evil tho)")

    while True:
        #accept command from player
        command = str(input("Enter what you want to do:"))
        command = clean(command)
        commandlist = command.split()

        if commandlist == []:
            commandlist = ["not"]

        # execute command if the command is ok
        if commandlist[0] in possible_commands:
            # testing it commands
            if command.startswith("go"):
                # for moving within the castle
                if inCastle == True:
                    try:
                        # attempts to move through the castle
                        currentRoom = move_In_Castle(currentRoom, commandlist[1])
                        break
                    except:
                        # tells the player they can't type
                        slow_text(
                            f"You attempt to move {commandlist[1]} but you crash into a wall, because it does not lead "
                            f"anywhere!")
                        slow_text("Type go {direction} to navigate the map.")

                # for moving within the forrest
                elif inCastle == False:
                    try:
                        # attempts to move through the castle
                        currentRoom = move_In_Forest(currentRoom, commandlist[1])
                        break
                    except:
                        # tells the player they can't type
                        slow_text(
                            f"You attempt to move {commandlist[1]} but you crash into a wall, because it does not lead anywhere!")

            # take command
            elif command.startswith("take"):
                execute_take(commandlist[1])
                for i in inventory:
                    slow_text(f"You have {i.id}", print_speed)
                print("")
            # drop command. enter an item_id
            elif command.startswith("drop"):
                execute_Drop(commandlist[1])

            # implementing the leave between the forest and the thing
            elif command.startswith("leave"):
                if get_item_from_inventory_by_id("forestmap") == False:
                    slow_text(
                        "You are trying to leave to go to the forest but surely\n you realise that u need a map of the forest to have any hope of making it out alive?"
                    )


                else:
                    # sets the current room to be inside the forest

                    currentRoom = forest[0][0]
                    slow_text("Welcome to the Misty Forest, where it is dark and possibly filled with evil", print_speed)
                    # update incastle variable

                    inCastle = False
                    break

            # implemented the use function
            elif command.startswith("use"):
                if get_item_from_inventory_by_id(commandlist[1]) == False:
                    slow_text(f"You try to use {commandlist[1]} but unfortunately you don't have it")

                #special castle map function
                elif commandlist[1] == "castle-map":
                    print(final_map)
                    #specific commands for the directions
                    for direction in currentRoom.get_Exits():
                        room_name = currentRoom.get_Exits()[direction]
                        slow_text(f"You can go {direction} to go to {room_name}", print_speed)
                    for i in currentRoom.get_Items():
                        slow_text(f"You can take {i.get_id()}", print_speed)

                    #oh no who's on greaze
                    #stormZ is underrated these daYs
                    #print the NPC You can talk to
                    for i in currentRoom.get_Npc():
                        slow_text(f"You can talk to {i.get_name()}", print_speed)

                else:
                    #print useing a basic item on not much
                    if commandlist[1] == "forestmap" or commandlist[1] == "castle-map":
                        print(get_item_from_inventory_by_id(commandlist[1]).on_use())
                    else:
                        slow_text(get_item_from_inventory_by_id(commandlist[1]).on_use())

            # implement talk function
            elif command.startswith("talk"):
                #get the on talk attribute from the npc and printing it
                if len(currentRoom.get_Npc()) == 0:
                    #if there isn't an NPC
                    slow_text("You try to talk but there's nobody there to listen", print_speed)
                else:
                    #if there's an NPC
                    slow_text(currentRoom.get_Npc()[0].on_talk())
            
            #attack special function functionaliT
            elif command.startswith("attack"):
                #Grekthor's layer personality
                if currentRoom.get_Name() == "Grekthor's Lair":
                    #print the dialogue from the secret ending upon attacking grekthor
                    play_another_audio(file_path+"SecretEndingDialogue.mp3",
                                           wisegoblinDialogue1)
                    goblinDialogueCount += 1
                    print(secret_ending)
                    exit()

                elif currentRoom.get_Name() == "King's Room" and good_ending == True:
                    #kill the king ending printing
                    kingDeathSpeechExtra = kingDeath1 + KingDeath2 + KingDeath3
                    #play audio of the end of the thing
                    play_another_audio(file_path+"KingDeathDialogue.mp3", kingDeath1,
                                       ["",KingDeath3])
                    print(good_ending_text)
                    exit()

                else:
                    try:
                       #attack the NPC
                        combat.Action(100,100,currentRoom.get_Npc()[0])
                        slow_text(currentRoom.get_Npc()[0].on_death_speech)

                        currentRoom.get_Npc()[0] = None
                    except:
                        slow_text("You try to attack but there's nothing there to attack", print_speed)

            elif command.startswith("spare"):
                # basic functionality of sparing Grekthor
                play_another_audio(
                    file_path+"GrekthorSpare.mp3",
                    wisegoblinDialogue2)
                currentRoom = room_hall
                inCastle = True
                good_ending = True
                break

        else:
            print(f"Invalid command! type:{possible_commands} at the beginning ")#if it's over.
