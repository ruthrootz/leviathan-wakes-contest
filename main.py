FACTIONS = ["earther", "belter", "opa", "mcrn", "laconian", "pirate"]
SHIPS =  ["rocinante", "tycho", "razorback", "donnager", "gathering storm"]
GATES = ["ilus", "laconia", "freehold", "auberon"]

faction = ""
ship = ""
merchandise = ""
gate = ""
keep_going = True

def initialize():
    faction = input("Choose your faction {FACTIONS}:\n".format(FACTIONS = FACTIONS)).lower()
    ship = input("Choose your ship, captain {SHIPS}:\n".format(SHIPS = SHIPS)).lower()
    if faction.lower() == 'earther':
        print("We're the OG. Earth is the best, even though our world is falling apart.\n")
    elif faction == "belter":
        print("Owkwa beltalowda!\n")
    elif faction == "opa":
        print("Welcome, copeng. Let's get those inyalowda.\n")
    elif faction == "mcrn":
        print("Donkey balls!\n")
    elif faction == "laconian":
        print("Yay for being a powerful bad guy with strong but questionable values!\n")
    elif faction == "pirate":
        merchandise = input("What do you smuggle, priate?\n")
    if (ship not in SHIPS) | (faction not in FACTIONS):
        print("Your choices don't match the options... Try again.\n")
        return False
    else:
        return True
 
def ceres():
    if input("Do you want to go to Ceres? y/n\n")[0].lower() == "n":
        return True
    if input("You meet Detective Miller. Want to go out for a drink with him? y/n\n")[0].lower() == "y":
        print("You guys get drunk and then get into an argument. Miller shoots you. You die. The end.\n")
        return False
    elif input("You meet some golgo players. Want to join them for some games? y/n\n")[0].lower() == "y":
        if ship == "rocinante":
            print("Your team wins the competition. Naomi is starting to think you're alright.\nTime to get back to your ship.\n")
        else:
            print("You win the competition and make a few extra bucks!\nTime to get back to your ship.\n")
        return True
    else:
        print("You go for a drink alone and get nice and plastered. Good for you.\nTime to get back to your ship.\n")
        print("You accidentally put {ship} in manual and crash into an asteroid. You die. Idiot. The end.\n".format(ship = ship))
        return False

def ganymede():
    if input("Do you want to go to Ganymede? y/n")[0].lower() == "y":
        print("Oops! You just got infected with the protomolecule. You're already in the process of dying a horrible death. So it goes.")
        return False
    else:
        return True

def final_frontier():
    print("Still alive? Lucky. The universe isn't usually this nice.\n")
    print("You head to the ring gate. Time to explore the universe!\n")
    gate = input("Choose a gate {GATES}:\n".format(GATES = GATES)).lower()
    if (faction == "opa" | faction == "pirate" | ship == "rocinante") & gate == "auberon":
        print("You get a contract to smuggle {merchandise} to Freehold. Your career in the Underground has begun!\n".format(merchandise = merchandise))
    elif gate == "auberon":
        print("You infiltrate and capture a group of Underground members. Congrats!\n")
    elif gate == "laconia":
        print("You get tortured by Laconians. Say hi to the other mutants in the pit!\n")
    elif gate == "freehold":
        print("You get tortured by Laconians. Say hi to the other mutants in the pit!\n")
    elif gate == "ilus":
        print("You get tortured by Laconians. Say hi to the other mutants in the pit!\n")

keep_going = initialize()
if keep_going:
    keep_going = ceres()
if keep_going:
    keep_going = ganymede()
if keep_going:
    keep_going = final_frontier()

print("I hope you enjoyed your time in the Expanse universe! JOIN US for the readalong starting in July.")
print("Media Death Cult: https://www.youtube.com/c/MovieDeathCult/featured")
