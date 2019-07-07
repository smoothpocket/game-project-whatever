import random

# Character lists. Each character has a list of profile data as:
# [Name, description/hint, HP, baseATK, attack1Name, attack1Uses, attack1Multiplier, attack2Name, attack2Uses, attack2Multiplier, baseDEF, luck (1-100), gold]
#D.C
francis=["Francis", "the hero", 100, 10, "Punch", 5, 2, "Kick", 10, 4, 5, 50, 20]
items=[]
crackhead=['crackhead', 'he needs his fix', 20, 5, "Injection", 2, 4, 'Scratch', 100, 1.5, 5, 50, 5]

#The grid that only shows where the character is (5x5), char is denoted by an "X"
gps_grid=[['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','X','-']]
#breadcrumb_grid shows what spaces francis has travelled
breadcrumb_grid =[['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','+','-']]

def print_map():
    print("_______________________________________")
    print("|Museum------T--------------Field     |")
    print("|______|___|_1_|___________|__________|")
    print("|      |   | 1 |Engineering|          |")
    print("|______|___|_1_|____1______|__________|")
    print("|      |   | L-|----+-------Sneed Hall|")
    print("|______|___|___|____1______|__________|")
    print("|      |Rec---------J      |          |")
    print("|______|___|___|____1______|__________|")
    print("|      |   |   |           |          |")
    print("|______|___|___|__Entrance_|__________|")


def print_gps(list):
    # Shows location
    x = 0
    while x < 5:
        print(list[x][0], " ", list[x][1], " ", list[x][2], " ", list[x][3], " ", list[x][4], " ")
        x += 1

#D.C.
def print_stats():
    print("Name: ", francis[0])
    print('Description: ', francis[1])
    print('HP: ', francis[2])
    print("BaseATK: ", francis[3])
    print('attack1Name: ', francis[4])
    print('attack1Uses: ', francis[5])
    print('attack1Multiplier: ', francis[6])
    print('attack2Name: ', francis[7])
    print('attack2Uses: ', francis[8])
    print('attack2Multiplier: ', francis[9])
    print('baseDEF: ', francis[10])
    print('luck: ', francis[11])
    print('gold: ', francis[12])


#D.C.
def pick_item(item, item_list):
    '''Once an item is obtained, this function can be called to select it from a menu.'''
    item_list.append(item)
    print(item, "has been added to your inventory!")

#D.C.
def restart_after_death(answer):
    '''After the character dies, this function is called to
    ask the user if he wants to restart or quit the game.'''
    if answer=="y":
        print('Start at the beginning')
    else:
        print("Quit the game")



#D.C.
def pick_item(item, itemList):
    '''Once an item is obtained, this function can be called to select it from a menu.'''
    itemList.append(item)
    print(item, "has been added to your inventory!")

# attacker and defender objects are lists with their stats, preassigned from character status
# separating into two combats for attack1 and attack2
def combat1(attacker, defender):
    # check if attacker has at least 1 charge for the attack
        if (attacker[5] > 0):
        # lowers defender's hp based on attacker's base attack and particular attack multiplier minus the defender's def
            print(attacker[0], " attacked ", defender[0], " with their ", attacker[4], " move!")
            defender[2] = defender[2] - ((attacker[3] * attacker[6]) - defender[10])
            attacker[5] = attacker[5] - 1
            print(defender[0], " took ", (attacker[3] * attacker[6] - defender[10]), "points of damage from ", attacker[0], ", dropping ", defender[0], " to ", defender[2], " hit points.")
            print("Attacker now has ", attacker[5], " charges left of their ", attacker[4], " move.")

            if defender [2] <1:
                if doomsday(attacker, defender) == True:
                    os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            print("Francis does not have any charge left for that move!")
        francis[0:] = attacker[0:]
        crackhead[0:] = defender[0:]

def combat2(attacker, defender):
        if (attacker[8] > 0):
            print(attacker[0], " attacked ", defender[0], " with their ", attacker[4], " move!")
            defender[2] = defender[2] - ((attacker[3] * attacker[9]) - defender[10])
            attacker[5] = attacker[5] - 1
            print(defender[0], " took ", (attacker[3] * attacker[9] - defender[10]), "points of damage from ", attacker[0], ", dropping ", defender[0], " to ", defender[2], " hit points.")
            print("Attacker now has ", attacker[5], " charges left of thier ", attacker[4], " move.")
            if defender[2] < 1:
                if doomsday(attacker, defender) == True:
                    os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            print("Francis does not have any charge left for that move!")
        francis[0:] = attacker[0:]
        crackhead[0:] = defender[0:]

# doomsday() is a function that handles the procedure when a char's HP drops to zero or below zero. Luck multiplier is
# used to see if he survives with 1hp
def doomsday(attacker, defender):
    print("The defender is badly wounded and at the doors of death. In his last efforts, he hopes his luck will give him a second breath...")
    # random.randint(0,100) makes a random number including 0 to including 100. attacker/defender[11] is the luck multiplier
    death_num_a = ((random.randint(0, 100)) * attacker[11]) / 1  # "/1" to round to nearest whole number
    death_num_b = ((random.randint(0, 100)) * defender[11]) / 1
    if death_num_a > death_num_b:
        print("Battered and bruised, the defender is unable to recover before the attacker throws his killing blow.")
        print(defender[0] + " has died.")
        if defender[0] == "Francis":
            print("GAME OVER")
            print("GAME OVER")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print("Returning to title screen and wiping board...")
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            return True
    elif death_num_b > death_num_a:
        print("Despite all odds, a miracle of luck recovers the fallen defender, reviving him with 1HP")
        print(defender[0] + " has been revived with 1HP and escapes.")
        return False

def face_wall(victim):
    print("Francis, not consulting his map or common sense before deciding where he wanted to go,")
    print("turned and walked directly into the wall of a nearby building.")
    print("This sheer act of stupidity causes a nosebleed that reduces Francis' health significantly")
    victim[2] = victim[2]-10
    return victim[2]

while True:
    print("The Missing Miss of Chapati Academy")
    print("___________________________________")
    print("A text-based adventure game by Nick Lloyd and Demetrius Cunningham")
    print("[Q]Start Game         [Z]Quit Game")
    power_on = ''
    power_on = input("Input:")

    if power_on == "Q":
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
        print("Francis Magilicutty, private eye, receives a case of a missing girl said to be spotted near an ")
        print("abandoned college, Chapati Academy. Arriving on campus, the calm, Fall climate was nothing but ")
        print("eerie. After paying the Uber driver,with no tip, he arrives on the campus 'Just Talk' area (with his map and gps) and cleans up")
        print("his mess.")
        print()
        print("*This is a text-based adventure game using a grid of 'squares'. If you're ever lost, type 'help' for a list of commands*")

        in_combat = False
        francis_dead = False
        has_moved_a_square_this_turn = False
        clicker = False
        while francis_dead == False:
            clicker = False
            print()
            user_input = input("Enter a command: ")

            if user_input == "help":
                print(" COMMAND:                       EFFECT:")
                print("'move north/south/east/west'...moves character to the square above/below/left/right of the square they're on")
                print("'map'..........................pulls up the map that shows buildings, paths, and intersections")
                print("'mKey'.........................helps explain how to read map")
                print("'gps'..........................pulls up the square you are at in the college, shown as an 'X'")
                print("'[insert name] stats'..........displays known stats of person selected. unknown stats will show up as '???'")
                print("'combat commands'...............shows available commands while in combat")
                print("'exit'.........................exits the program (WARNING: Your progress will not be saved!)")
                print("'my stats'.......................overviews Francis' updated stats")

            elif user_input == "my stats":
                print_stats()
                clicker = True
            elif user_input == "exit":
                print("Are you sure you want to quit? Progress will not be saved!")
                clicker = True
                response = input("Press [y] if you're sure, or any other letter to continue: ")
                if response == "y":
                    print("GAME OVER")
                    exit()
            elif user_input == "map":
                print_map()
                clicker = True
            elif user_input == "gps":
                print_gps(gpsGrid)
                clicker = True

            if in_combat == False:


                #move checks
                if user_input == "move north":
                    if gps_grid[2][3]=="X":
                        engi_switch = False
                        while engi_switch == False:
                            engi_switch = True
                            x = 0
                            print('You are at the Engineering Building. Surprisingly, the nerd smell still remains.')
                            print('[1]Chemical Engineering Room')
                            an = input('Where do you want to go now?: ')
                            if an == '1':
                                while x < 10:
                                    choice = input(
                                        "Looking like an ordinary chem, you see some chemical that might come in handy. Do you want it(y/n): ")
                                    if choice == 'y':
                                        pick_item("chemical", items)
                                        print("As soon as you were about leave, a wild crackhead appeared. He asks you 'Do you the fix?'.")
                                        print("You reply with 'No', being the good student you are. He pulls out a needle, ready to fight")
                                        while crackhead[2] > 0:
                                            if crackhead[2] < 5:
                                                crackhead[6] = 16
                                                print("The crackhead attackmultiplier is now 16.")
                                            elif crackhead[2] < 10:
                                                crackhead[6] = 12
                                                print("The crackhead attackmultiplier is now 12.")
                                            elif crackhead[2] < 15:
                                                crackhead[6] = 8
                                                print("The crackhead attackmultiplier is now 8.")
                                            move = input("Will you throw a [punch], or a [kick]? ")
                                            if move == "kick":
                                                combat2(francis, crackhead)
                                            if move == "punch":
                                                combat1(francis, crackhead)
                                            print("Crackhead swings at you for 10 damage!")
                                            francis[2] = francis[2]-10
                                            if francis[2] < 1:
                                                doomsday(crackhead, francis)


                                    else:
                                        print("I guess you won't need that will you.")
                                    x = 20
                            else:
                                print("The only option is 1 retard.")
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
                        print("Francis paces forwards, approaching a slight split in the path.")
                        print("A light scent of BO drifts into his nostrils from the path to the left")
                        gps_grid[4][3] = "-"
                        gps_grid[3][3] = "X"
                    else:
                        francis[2] = face_wall(francis)
