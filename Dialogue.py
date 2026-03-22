from name import name
from goblin import get_ascii_image
from Ending1 import *
import time
import sys

#The dialogue between the princess and the hero(us)
ascii_art = get_ascii_image()
ending_art = get_ascii_image()

def slow_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


princessDialogue1 = f'''

Princess Elowen: “Don't you think these flowers are just beautiful?”

{name}: “Yeah they seem nice i guess”

Princess Elowen: “Nice”?  Just nice? You must not have good taste in flowers then. Who are you anyways?”

{name}: “ i'm a nobody”

Princess Elowen: “Nobody's a nobody, who are you really?” 

{name}: Reluctantly, you say “I’m on a mission of sorts, i’m avenging the murder of my younger sister done by the hands of the goblins.”

Princess Elowen: “oh…i’m sorry to hear that, it must have been painful to carry the weight of your dead sister all on your own”

{name}: “...it was"

Princess Elowen: “You know what, i’d like to help you. Have a look at this.”
The princess hands you a map

Princess Elowen:  “This is a map of the forest that was made years ago when it was first discovered, the rumours say you can get to the forest by going
through the chapel into the dungeon, and through the hidden tunnels of the dungeon into the Misty forest. now this isn’t a spot on map as we aren’t exactly sure where Grekthor the Sage, 
the commander of the goblins is, but it’ll help you get going.

{name}: “This will be of use, I am speechless, this will definitely be of use to me, Thank you…wait i never asked but, what is your name?”

Princess Elowen: “My name is Elowen, Princess Elowen daughter of the king Magnar III”

{name}: “Princess…”

Princess Elowen: “Yeah yeah too stunned to speak or something? Get going you have a sister to avenge”

{name}: “ I will. Thank you, Princess. I will see you soon.”
'''


kingDialogue1 = f'''King: “Welcome to my humble castle, I am Magnar the Third, where under my rule even the poor do not starve,
for i am not only the King of this mighty castle, but a king of truth and justice. May i ask, what is your name?”

{name}:My name is {name}

King: “A fine name for a warrior, now no one usually goes roaming around the Great Hall for no reason. What are you here for exactly?”

{name}: “My sister has been slaughtered.”

King: “I'm sorry to hear that...”

{name}: “When I was a boy, it was just my sister and I. My mother and father died in battle, so she was all I had. 
From hiding ourselves from those damned raiders, to sometimes going hungry so she can go to sleep with a full belly,
I would have done anything to protect her. She was a joyful kid, often filling our house with laughter and warmth. 
Everything came crashing down when one night, I heard a scream coming from her room. 
It was everywhere, her blood was splattered on the walls as though her murderer was painting something.
The window. He came from the window and left before i could see who it was…” said with a stern face. 
“I’m here searching for answers, for any information as to who killed my sister”

King: With a sorrowful look and a nod “Poor girl, it must have been work of those goblins.”

{name}: “Goblins?”'''

kingDialogue2 = ascii_art

kingDialogue3 = f'''King: “Yes, about a decade ago many of them went on a rampage in a nearby town,
they killed every human they could get their hands on and retreated into the forest,
with their king Grekthor the Sage. It’s fascinating how a single command from a person in power can change the course of many lives.
Sometimes, the throne demands sacrifices, and one must be prepared to make them.
We’ve fought tirelessly against them sending my own knights there, but they never came back.
If you are interested in revenge, unfortunately i cannot help you with reinforcements, we have lost many as it is.
But you are welcome to venture out on your own to seek your own path. 

{name}: “...I understand. I appreciate the help, my Lord” 

King: “Of course, anything i can do to help. 
One more thing, i would like to gift you this dagger,
it is one of a kind and is meant to be for my successor, but i fear you may need it more.”

{name}: “I will be sure to wield it with wisdom, and to put it down after its use, for peace is what i wish to attain.”

*King goes back to his room*
'''

wisegoblinDialogue1 = f'''{name}: “ I am here for your head Grekthor!. 

{name} reaches Grekthor the Sage.

{name}: “It must be you, are you Grekthor the Sage??” 

Grekthor the Sage: ”Yes it is I. You have murdered countless of my kinds folk, men, and women. What is your reason for this unrelenting bloodshed?”

{name}: “ YOU KILLED MY SISTER. That night you came into my house through the window and killed her. I’m supposed to ask YOU what was the reason for her death.”

Grekthor the Sage: ”...The window? You do realize that the smallest goblin out there is the size of a bear! What madness are you on about.

{name}: “But…but that night five years ago-”

Grekthor the Sage: ”Five years ago? Hold on…are you talking about the the Magnar Massacre? When Magnar III supposedly murdered everyone in a nearby village in order to keep something a secret?

{name}: “What are you talking about? I’ve never heard of this massacre…”

Grekthor the Sage: ”Yeah no wonder, it was all hush hush by the kingdom, and was swept under the rug. Luckily, i have my spies here and there who’ve witnessed it firsthand.”

{name}: “Well why should i believe you? You could just be saying all this in order to protect your sorry ass!!”

Grekthor the Sage: ”You have already killed many of my kinsfolk, i have nothing more to lose. But if you kill the king, the man who ordered the execution of your people, I will overlook what you have done to seek peace.”

{name}: “ I don’t trust you! You goblins and your lies, the king has told me it was you, so it must be you. Do you have any last words.”

Grekthor the Sage: with a mix of sadness and resolve “ Before you strike, know this: vengeance blinds the heart. Your sister's spirit and yourself seeks peace, not a cycle of blood. Seek the truth, or you will carry this sorrow forever”

{name} kills Grekthor the Sage.

{name}: “ Finally, you have been avenged. Yet my heart is empty, i have found peace knowing that your death has been avenged.” 

*You slowly realise that you have not actually avenged your sister, because it was the King who murdered her*
'''


kingDeath1 = f'''You make your way into the castle, and enter the King's room

The King: “You’re back already! How did it go?”

{name}: “ YOU LIED TO ME”

The King: “Woah woah woah, I would do no such thing”

{name}: “You killed my sister that day…five years ago”

The King: “Have you gone mad? What kind of accusation is that? I would never do such a thing!”

{name}: “ And what of the Magnar Massacre”

The King: “...Who told you” 

{name}: “Not only did you kill my sister…You manipulated me into killing the goblins!!” 

The King: “NO. That was you. Allll you. You were the one who went out there and murdered them. Their blood is on your hands.”

{name}: “You lying, sly conniving bastard!” 

The King draws his sword, the blade shimmering with dark magic.

The King: "You are a fool to challenge me. You will fare no better than those before you."

The battle ensues. Steel clashes as you and the king duel fiercely. Despite his power, you fight with the strength of the oppressed. Finally, you disarm him, and he falls to his knees.

The King: "Spare me, and I will grant you riches and power!"

{name}: "This is for all the lives you destroyed."

With a swift motion, you plunge your sword into the king's chest. He gasps and collapses, dead.
'''
KingDeath2 = ending_art

KingDeath3 = f'''
Silence falls. You stand victorious, the tyrant king defeated. 

And so, the tyrant king fell, ending his reign of terror. The hero, once an ordinary citizen, became a legend. The kingdom, once in darkness, basked in the light of a new dawn.
'''

wisegoblinDialogue2 = f'''Hero reaches Grekthor the Sage.

{name}: “It must be you, are you Grekthor the Sage??” 

Grekthor the Sage: ”Yes it is I. You have murdered countless of my kinndds folk, men, and women. What is your reason for this unrelenting bloodshed?”

{name}: “ YOU KILLED MY SISTER. That night you came into my house through the window and killed her. I’m supposed to ask YOU what was the reason for her death.”

Grekthor the Sage: ”...The window? You do realize that the smallest goblin out there is the size of a bear! What madness are you on about.

{name}: “But…but that night five years ago-”

Grekthor the Sage: ”Five years ago? Hold on…are you talking about the the Magnar Massacre? When Magnar III supposedly murdered everyone in a nearby village in order to keep something a secret?

{name}: “What are you talking about? I’ve never heard of this massacre…”

Grekthor the Sage: ”Yeah no wonder, it was all hush hush by the kingdom, and was swept under the rug. Luckily, i have my spies here and there who’ve witnessed it firsthand.”

{name}: “Well why should i believe you? You could just be saying all this in order to protect your sorry ass!!”

Grekthor the Sage: ”You have already killed many of my kinsfolk, i have nothing more to lose. But if you kill the king, the man who ordered the execution of your people, I will overlook what you have done to seek peace.”

{name}: Okay, I trust you...

{name}: “ But why would the king lie to me. Why would he tell me it was you who had killed my sister.”

Grekthor the Sage: “ It would only make sense to put the blame on us, he has hated our kind for for as long as i can remember. He found an opportunity in the death of your sister and took advantage of that, to turn you against us. That cunning Magnar.”

{name}: “That can’t be…I killed your people…how could i have done that”

Grekthor the Sage: “ Listen, you have done what is done. It’s over. You have been manipulated by the king. You must accept that reality now, and your next step is to figure out what you should do next” 

{name}: “ …The King killed my sister…it is him who i need to kill.”

Grekthor the Sage: “Do what you must”

You turn silent, with a stiff face. You exit the forest with the intent to kill the King.

*You make way towards the castle and enter the Great Hall*
'''

