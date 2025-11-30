import random
import time

print("Welcome to the Shadow Door Puzzle!")
print("There are three doors. One has a shadow behind it… choose carefully.\n")

all_doors = ["Red", "Blue", "Green"]

while True:
    shadow_at = random.choice(all_doors)
    safe = [d for d in all_doors if d != shadow_at]
    clue_kind = random.choice(["first_letter", "contains_letter", "backwards"])

    if clue_kind == "first_letter":
        clue_text = "The shadow avoids any door starting with the letter '{}'.".format(shadow_at[0])
    elif clue_kind == "contains_letter":
        some_letter = random.choice(random.choice(safe))
        clue_text = "A safe door has the letter '{}' somewhere in it.".format(some_letter)
    else:
        clue_text = "If you reverse the name of the shadow’s door, it looks like '{}'.".format(shadow_at[::-1])

    print("Clue:", clue_text)

    player_pick = input("Pick a door (Red / Blue / Green): ").strip().capitalize()

    print("Hmm...")
    time.sleep(1)

    if player_pick == shadow_at:
        print("Oh no… the shadow was behind the {} door. Game over.".format(shadow_at))
        break
    elif player_pick in all_doors:
        print("Good call! The shadow was actually behind {}.".format(shadow_at))
        print("Next round...\n")
    else:
        print("That’s not even a valid door… the shadow catches you for hesitating.")
        break
