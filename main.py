FACTIONS = ["earther", "belter", "opa", "mcrn", "laconian", "pirate"]
SHIPS =  ["rocinante", "tycho", "razorback", "donnager", "gathering storm"]
GATES = ["ilus", "laconia", "freehold", "auberon"]

faction = ""
ship = ""

def initialize():
    faction = input("Choose your faction {FACTIONS}:\n".format(FACTIONS = FACTIONS)).lower()
    ship = input("Choose your ship {SHIPS}:\n".format(SHIPS = SHIPS)).lower()
    if faction.lower() == 'earther':
        print("We're the OG. Earth is the best, even though our world is falling apart.")
    elif faction == "belter":
        print("Owkwa beltalowda!")
    elif faction == "opa":
        print("Welcome, copeng. Let's get those inyalowda.")
    elif faction == "mcrn":
        print("Donkey balls!")
    elif faction == "laconian":
        print("Yay for being a powerful bad guy with strong but questionable values!")
    elif faction == "pirate":
        merchandise = input("What do you smuggle, priate?")
    if (ship not in SHIPS) | (faction not in FACTIONS):
        print("Your choices don't match the options... Try again.")
    if faction.lower():
        
def ceres()
    # go to Ceres?
        # go for a drink with Miller?
            # get shot by drunk Miller
        # go for a drink alone?
            # get drunk
        # win a golgo competition
            # if on Roci, Naomi likes you now
    # leave Ceres?
        # got drunk?
        # you put {ship} in manual and crash into an asteroid, idiot
        # if not pirate, you leave Ceres and get chased by pirates
        # if pirate, you get captured and tortured by Laconians

def ganymede()
# go to Ganymede?
    # get infected with the protomolecule

def final_frontier()
# "Still alive? Lucky. The universe isn't usually this nice."
# "You head to the ring gate. Time to explore the universe!"
# if drunk, enter random ring gate
# else, choose a ring gate
    # if infected, "The protomolecule gets the better of you. You dead."
    # if (opa | pirate | rocinante) & auberon, get a contract "You get a contract to smuggle {merchandise} to Freehold. Your career in the Underground has begun!"
    # else, "You infiltrate and capture a group of Underground members."
    # if Laconia, "You get tortured by Laconians. Say hi to the other mutants in the pit!""
    # if freehold
    # if ilus

initialize()
ceres()
ganymede()
final_frontier()

print("I hope you enjoyed your time in the Expanse universe! JOIN US for the readalong starting in July.")
print("Media Death Cult: https://www.youtube.com/c/MovieDeathCult/featured")
