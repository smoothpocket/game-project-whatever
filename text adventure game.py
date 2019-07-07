from __future__ import print_function
import random
from textwrap import dedent


items = []

class Attack():
    def __init__(self, name, uses, multiplier):
        self.name = name
        self.uses = uses
        self.multiplier = multiplier

# Each character has profile data, where 0 <= `luck` <= 100
class Character():
    def __init__(self, name, description, hp, base_attack, attack, base_defense, luck, gold):
        self.name = name
        self.description = description
        self.hp = hp
        self.base_attack = base_attack
        self.attack = attack
        self.base_defense = base_defense
        self.luck = luck
        self.gold = gold

francis = Character("Francis", "the hero", 100, 10, [Attack("Punch", 5, 2), Attack("Kick", 10, 4)], 5, 50, 20)
crackhead = Character("Crackhead", "he needs his fix", 20, 5, [Attack("Injection", 2, 4), Attack("Scratch", 100, 1.5)], 5, 50, 5)

# The gps_grid shows where Francis currently is. The breadcrumb_grid shows where Francis has been
gps_grid,  breadcrumb_grid = ["-" * 5] * 5, ["-" * 5] * 5
gps_grid[4][3], breadcrumb_grid[4][3] = 'X', '+'

def print_map():
    print(dedent("""
        _______________________________________
        |Museum------T--------------Field     |
        |______|___|_1_|___________|__________|
        |      |   | 1 |Engineering|          |
        |______|___|_1_|____1______|__________|
        |      |   | L-|----+-------Sneed Hall|
        |______|___|___|____1______|__________|
        |      |Rec---------J      |          |
        |______|___|___|____1______|__________|
        |      |   |   |           |          |
        |______|___|___|__Entrance_|__________|
    """))

def print_gps():
    for i in range(5):
        for j in range(5):
            print(gps_grid[i][j], " ", end="")
        print()

def print_stats():
    print("Name: ", francis.name)
    print('Description: ', francis.description)
    print('HP: ', francis.hp)
    print("BaseATK: ", francis.base_attack)

    print('attack1Name: ', francis.attack[0].name)
    print('attack1Uses: ', francis.attack[0].uses)
    print('attack1Multiplier: ', francis.attack[0].multiplier)

    print('attack2Name: ', francis.attack[1].name)
    print('attack2Uses: ', francis.attack[1].uses)
    print('attack2Multiplier: ', francis.attack[1].multiplier)

    print('baseDEF: ', francis.base_defense)
    print('luck: ', francis.luck)
    print('gold: ', francis.gold)

def pick_item(item, item_list):
    '''Once an item is obtained, this function can be called to select it from a menu.'''
    item_list.append(item)
    print(item, "has been added to your inventory!")

def restart_after_death(answer):
    '''After the character dies, this function is called to
    ask the user if he wants to restart or quit the game.'''
    if answer=="y":
        print('Start at the beginning')
    else:
        print("Quit the game")

def combat(attacker, defender, index):
    if attacker.attack[index].uses >= 1:
        attacker.attack[index].uses -= 1
        print(attacker.name, " attacked ", defender.name, " with their ", attacker.attack[index].name, " move!")

        damage_dealt = (attacker.base_attack * attacker.attack[index].multiplier) - defender.base_defense
        defender.hp -= damage_dealt
        print(defender.name, " took ", damage_dealt, "points of damage from ", attacker.name, ", dropping ", defender.name, " to ", defender.hp, " hit points.")
        print("Attacker now has ", attacker.attack[index].uses, " charges left of their ", attacker.attack[index].name, " move.")

        if defender.hp <= 0:
            if doomsday(attacker, defender):
                os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("Francis does not have any charge left for that move!")

    global francis
    francis = attacker
    global crackhead
    crackhead = defender

# doomsday() is a function that handles the procedure when a char's HP drops to zero or below zero. Luck multiplier is
# used to see if he survives with 1hp
def doomsday(attacker, defender):
    print("The defender is badly wounded and at the doors of death. In his last efforts, he hopes his luck will give him a second breath...")
    # random.randint(0,100) makes a random number including 0 to including 100. attacker/defender[11] is the luck multiplier
    death_num_a = ((random.randint(0, 100)) * attacker.luck) / 1  # "/1" to round to nearest whole number
    death_num_b = ((random.randint(0, 100)) * defender.luck) / 1
    if death_num_a > death_num_b:
        print("Battered and bruised, the defender is unable to recover before the attacker throws his killing blow.")
        print(defender.name + " has died.")
        if defender.name == "Francis":
            print("\n".join(
                (["GAME OVER"] * 2) +
                (["Returning to title screen and wiping board..."]) * 2) +
                (["\n" * 30])
            )
            return True
    else:
        print("Despite all odds, a miracle of luck recovers the fallen defender, reviving him with 1HP")
        print(defender.name + " has been revived with 1HP and escapes.")
        return False

def face_wall(victim):
    print(dedent("""
        Francis, not consulting his map or common sense before deciding where he wanted
        to go, turned and walked directly into the wall of a nearby building. This sheer
        act of stupidity causes a nosebleed that reduces Francis' health significantly.
    """))

    victim.hp -= 10
    return victim.hp

while True:
    print(dedent("""
        The Missing Miss of Chapati Academy
        -----------------------------------
        
        A text-based adventure game by Nick Lloyd and Demetrius Cunningham
        
        [Q] Start Game
        [Z] Quit Game
    """))

    if input("Input: ") == "Q":
        print("\n" * 40)
        print(dedent("""
            Francis Magilicutty, private eye, receives a case of a missing girl said to be
            spotted near an abandoned college, Chapati Academy. Arriving on campus, the calm
            fall climate was nothing but eerie. After paying the Uber driver with no tip, he
            arrives on the campus 'Just Talk' area (with his map and gps) and cleans up his
            mess.
            
            * This is a text-based adventure game using a grid of 'squares'. *
            * If you're even lost, type 'help' for a list of commands.       *
        """))

        while True:
            user_input = input("\nEnter a command: ")

            if user_input == "help":
                print(dedent("""
                    COMMAND:                       EFFECT
                    'move north/south/east/west'...moves character to the square above/below/left/right of the square they're on
                    'map'..........................pulls up the map that shows buildings, paths, and intersections
                    'mKey'.........................helps explain how to read map
                    'gps'..........................pulls up the square you are at in the college, shown as an 'X'
                    '[insert name] stats'..........displays known stats of person selected. unknown stats will show up as '???'
                    'combat commands'..............shows available commands while in combat
                    'exit'.........................exits the program (WARNING: Your progress will not be saved!)
                    'my stats'.....................overviews Francis' updated stats
                """))

            elif user_input == "my stats":
                print_stats()

            elif user_input == "exit":
                print("Are you sure you want to quit? Progress will not be saved!")
                if input("Press [y] if you're sure, or any other letter to continue: ") == "y":
                    print("GAME OVER")
                    exit()

            elif user_input == "map":
                print_map()

            elif user_input == "gps":
                print_gps()

            elif user_input == "move north":
                if gps_grid[2][3]=="X":
                    engi_switch = False
                    while not engi_switch:
                        engi_switch = True
                        x = 0
                        print(dedent("""
                            You are at the Engineering Building. Surprisingly, the nerd smell still remains.
                            
                            [1] Chemical Engineering Room
                        """))
                        if input('Where do you want to go now?: ') == '1':
                            while x < 10:
                                choice = input("Looking like an ordinary chem, you see some chemical that might come in handy. Do you want it(y/n): ")
                                if choice == 'y':
                                    pick_item("chemical", items)
                                    print(dedent("""
                                        As soon as you were about to leave, a wild crackhead appeared. He asks you 'Do you the fix?',
                                        You reply with 'No', being the good student you are. He pulls out a needle, ready to fight.
                                    """))

                                    while crackhead.hp > 0:
                                        if crackhead.hp < 5:
                                            crackhead.base_attack = 16
                                            print("The crackhead attack multiplier is now 16.")
                                        elif crackhead.hp < 10:
                                            crackhead.base_attack = 12
                                            print("The crackhead attack multiplier is now 12.")
                                        elif crackhead.hp < 15:
                                            crackhead.base_attack = 8
                                            print("The crackhead attack multiplier is now 8.")
                                        move = input("Will you throw a [punch], or a [kick]? ")
                                        if move == "punch":
                                            combat(francis, crackhead, 0)
                                        if move == "kick":
                                            combat(francis, crackhead, 1)
                                        print("Crackhead swings at you for 10 damage!")
                                        francis.hp -= 10
                                        if francis.hp <= 0:
                                            doomsday(crackhead, francis)


                                else:
                                    print("I guess you won't need that will you.")
                                x = 20
                        else:
                            print("The only option is 1 so far.")
                            engi_switch = False
                    gps_grid[2][3] = "-"
                    gps_grid[1][3] = "X"
                    #all the engineering building stuff (he enters)
                elif gps_grid[1][2]=="X":
                    gps_grid[1][2] = "-"
                    gps_grid[0][2] = "X"
                    #code for the fork in the road
                elif gps_grid[2][2] == "X":
                    gps_grid[2][2] = "-"
                    gps_grid[1][2] = "X"
                    #code at that path
                elif gps_grid[3][3] == "X":
                    gps_grid[3][3] = "-"
                    gps_grid[2][3] = "X"
                    #code at that path
                elif gps_grid[4][3] == "X":
                    print(dedent("""
                        Francis paces forwards, approaching a slight split in the path.
                        A light scent of BO drifts into his nostrils from the path to the left
                    """))

                    gps_grid[4][3] = "-"
                    gps_grid[3][3] = "X"
                else:
                    francis[2] = face_wall(francis)
