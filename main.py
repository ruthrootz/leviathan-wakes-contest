FACTIONS = ["earther", "belter", "opa", "mcrn", "laconian", "pirate"]
SHIPS =  ["rocinante", "tycho", "razorback", "donnager", "gathering storm"]
GATES = ["ilus", "laconia", "freehold", "auberon"]

faction = input("Choose your faction {FACTIONS}:\n".format(FACTIONS = FACTIONS)).lower()
ship = input("Choose your ship {SHIPS}:\n".format(SHIPS = SHIPS)).lower()

if faction.lower() == 'earther':
    print(
        "We're the OG. That's why we're always right, even though our world is falling apart."
    )
elif faction == "belter":
    print("Owkwa beltalowda!")
elif faction == "opa":
    print("Welcome, copeng. Let's get those inyalowda.")
elif faction == "mcrn":
    print("Donkey balls!")
elif faction == "laconian":
    print(
        "Yay for being a powerful bad guy with strong but questionable values!"
    )
elif faction == "pirate":
    print("You'll still get dragged into this mess, pirate, even if you don't want to fight for a cause.")
if (ship not in SHIPS) | (faction not in FACTIONS):
    print("Your choices don't match the options... Try again.")

# if pirate, choose what you smuggle, get captured
# go to Ceres?
# get shot by drunk Miller
# win a golgo competition, Naomi likes you now (if on Roci)
# get drunk
# leave Ceres?
# get drunk? & leave Ceres?
# you put [ship name] in manual and crash into an asteroid, idiot
# if not pirate, you leave Ceres and get chased by pirates
# if pirate, you get caputred and tortured by Laconians
# go to Ganymede?
# get infected with the Protomolecule

# "Still alive? Lucky. The universe isn't usually this nice."
# "You head to the ring gate. Time to explore the universe!"
# if drunk, enter random ring gate
# else, choose a ring gate
# if (opa | pirate | rocinante) & auberon, get a contract "You get a contract to smuggle supplies to Freehold. Your career in the Underground has begun!"
# else, "You infultrate and capture a group of Underground members."
# if Laconia, "You get tortured by Laconians. Say hi to the other mutants in the pit!""
# if freehold
# if ilus
