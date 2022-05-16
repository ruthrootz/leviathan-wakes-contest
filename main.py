faction = input("Choose your faction [Earther, Belter, OPA, MCRN, Laconian, pirate (no affiliation)]:\n")
ship = input("Choose your ship [Rocinante, Tycho, Razorback, Donnager, Gathering Storm]:\n")

if faction.lower() == 'earther':
    print("We're the OG. That's why we're always right, even though our world is falling apart.")
elif faction.lower() == "belter":
    print("Owkwa beltalowda!")
elif faction.lower() == "opa":
    print("Welcome, copeng. Let's get those inyalowda.")
elif faction.lower() == "mcrn":
    print("Donkey balls!")
elif faction.lower() == "laconian":
    print("Yay for being a powerful bad guy with strong but questionable values!")
elif faction.lower() == "pirate  (no affiliation)":
    print("You'll still get dragged into this mess.")
elif ship not in ["Rocinante", "Tycho", "Razorback", "Donnager", "Gathering Storm"]:
    print("Your choices don't match the options... Try again.")

# if pirate, choose what you smuggle, get captured
# go to Ceres?
    # get shot by drunk Miller
    # win a xxx competition, Naomi likes you now (if on Roci)
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
    # else, choose a ring gate [Ilus, Laconia, Freehold, Auberon]
        # if (OPA | pirate | rocinante) & auberon, get a contract "You get a contract to smuggle supplies to Freehold. Your career in the Underground has begun!"
        # else, "You infultrate and capture a group of Underground members."
        # if Laconia, get tortured by Laconians, say hi to the other mutants in the pit
        # if freehold
        # if ilus
