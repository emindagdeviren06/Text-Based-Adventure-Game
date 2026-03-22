from castleNPCs import *
from Generating_Forest_Function import *
from name import name



def Combat(room: forest_Room, enemy: npc):

    """
    slow_text("You encountered a " + enemy.name + ": " + enemy.dialogue)
    global name
    slow_text("Get ready to fight " + name + ". Press any key to continue.")"""


    health = 100000
    while health > 0 & enemy.health > 0:

        health, enemy.health = Action(health, enemy.health, enemy)

        slow_text("Player health: " + str(health) + ", " + enemy.name + " health: " + str(enemy.health))

        Action(health,enemy.health,enemy)

        slow_text("Press enter to continue:")
        delay = input()


def Action(p_health, enemy_health, enemy: npc):
    global name

    #define random lists

    move_verbs: list[str] = ["rolled", "jumped", "dodged", "darted", "dived"]
    attack_verbs: list[str] = ["stabbed", "kicked", "punched", "elbowed", "pushed"]
    sentence_starters: list[str] = ["mustered up all his", "thought about all his", "became consumed with"]
    emotions: list[str] = ["anger", "sadness", "courage", "pain", "panic", "rage"]
    adjectives: list[str] = ["swiftly", "quickly", "cautiously", "courageously", "embarrasingly"]
    directions: list[str] = ["to the side", "backwards", "away"]
    body_parts: list[str] = ["head", "stomach", "knee", "side", "chest"]

    attacker = ""
    defender = ""
    ran = Generate_Random(1, 2)
    if ran == 1:
        attacker = name
        defender = "the " + enemy.name
    else:
        attacker = "the " + enemy.name
        defender = name
    sentence = attacker + " " + sentence_starters[Generate_Random(0, len(sentence_starters) - 1)] + " " + emotions[
        Generate_Random(0, len(emotions) - 1)] + " and " + move_verbs[
                   Generate_Random(0, len(move_verbs) - 1)] + " towards " + defender + " and " + adjectives[
                   Generate_Random(0, len(adjectives) - 1)] + " " + attack_verbs[
                   Generate_Random(0, len(attack_verbs) - 1)] + " his enemy."
    time.sleep(1)
    slow_text(sentence)

    return p_health, enemy_health
"""
    ran = Generate_Random(0, 100)
#move_verbs[Generate_Random(0, len(move_verbs) - 1)]
    if ran > 70:
        sentence += " However, " + defender + " had managed to have " + move_verbs[
            Generate_Random(0, len(move_verbs) - 1)] +  " away"
        if ran > 85:
            sentence += " and then " + attack_verbs[Generate_Random(0, len(attack_verbs) - 1)] + attacker + " in the " + \
                        body_parts[Generate_Random(0, len(body_parts) - 1)]
            if attacker == name:
                p_health = p_health - enemy.damage
            else:
                enemy_health = enemy_health - 20
    else:
        if attacker == name:
            enemy_health = enemy_health - 20
        else:
            p_health = p_health - enemy.damage

    slow_text(sentence)"""


def Generate_Random(min, max):
    ran = random.randint(min, max)
    return ran

