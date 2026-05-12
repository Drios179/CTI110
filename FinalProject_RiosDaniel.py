#Daniel Rios
#12May2026
#Final Project
#Create a game with one main character/object using functions

import random
import time

#creating character with items
def create_character():
    name = input("Enter your character's name: ")
    #what character has to grow plants
    inventory = {"watering_can": "💧 Watering Can"}
    return {"name": name, "inventory": inventory}

#stages for the plant that could potentially grow
def create_plant():
    return {
        "stage": 0,
        "max_stage": 10,
        "stages": [
            "🌱 Seedling (Stage 1)",
            "🌱 Seedling (Stage 2)",
            "🌱 Seedling (Stage 3)",
            "🌱 Seedling (Stage 4)",
            "🌿 Sprout (Stage 5)",
            "🌿 Sprout (Stage 6)",
            "🌾 Small Plant (Stage 7)",
            "🌾 Small Plant (Stage 8)",
            "🌾 Small Plant (Stage 9)",
            "🌳 Fully Grown (Stage 10)"]
    }

#def function for random weather events that decrease growth
def weather_event(plant):
    #random weather events and decreases in growth
    events = [
        ("☀️ Heatwave", 2),
        ("🌧️ Heavy Rain", 1),
        ("💨 Strong Winds", 3),
        ("❄️ Cold Snap", 2),
        ("⛈️ Thunderstorm", 1),
        ("🌤️ Mild Weather", 0)]

    event, penalty = random.choice(events)

#shows weather event is happening
    print(f"⚠️ WEATHER EVENT: {event}!")

    #decrease plant growth/health

    if penalty > 0:
        print(f"The plant loses {penalty} growth stage(s).")
        plant["stage"] = max(0, plant["stage"] - penalty)
    else:
        print("No growth lost.")

    print(f"Current plant stage: {plant['stages'][plant['stage']]}")
    time.sleep(1)

#def function for making the regular grow the plant by +1
def regular_grow(character, plant, grow_stage):
    """Grow +1 stage per watering."""
    #shows name when you water the plant
    input(f"{character['name']}, press ENTER to water the plant... ")
    #plant growth each time it is watered
    plant["stage"] = min(plant["stage"] + 1, plant["max_stage"] - 1)
    #shows name watering plant
    print(f"{character['name']} waters the plant...")
    #prompts the plant is growing
    print(f"The plant is now: {plant['stages'][plant['stage']]}")
    time.sleep(1)

#def function that makes super grow, grow the plant 3x
def super_grow(character, plant, grow_stage):
    """Super grow grows the plant 3x."""
    #shows name when you water the plant
    input(f"{character['name']}, press ENTER to water the plant... ")
    #plant growth each time it is watered
    plant["stage"] = min(plant["stage"] + 3, plant["max_stage"] - 1)
    #shows grow type
    print("⚡ SUPER GROW ACTIVATED!")
    #prompts the plant became 3x larger
    print(f"The plant becomes 3x: {plant['stages'][plant['stage']]}")
    time.sleep(1)

#Menu of grow modes you can choose from
def choose_mode():
    print("========== GROW MODE MENU ==========")
    print("1. Regular Grow 🌿")
    print("2. Super Grow ⚡")
    print("====================================")

    choice = input("Choose a grow mode (1 or 2): ")
    #choice of grow mode or default to regualr grow mode
    if choice == "1":
        return regular_grow
    elif choice == "2":
        return super_grow
    else:
        print("Invalid choice, defaulting to Regular Grow.")
        return regular_grow

#creating main function for the game
def main():
    character = create_character()


    while True:
        # Player chooses grow mode each game
        grow_mode = choose_mode()
        #creation of the plant
        plant = create_plant()

        # Randomize how many times the plant grows this game
        grow_stage = random.randint(3, 10)
        print(f"🌿 This game requires {grow_stage} watering actions!")

        # Runs selected grow mode with randomized grow stages
        for _ in range(grow_stage):
            grow_mode(character, plant, grow_stage)

            # weather that decreases health of plant after watering
            weather_event(plant)

            # stop early if plant is fully grown
            if plant["stage"] >= plant["max_stage"] - 1:
                break

        #Growth of plant and when plant is fully grown
        print("🌳 Your plant is fully grown!")
        print("🏆 Game complete!")

        # Asks player if they want to play again
        play_again = input("Play again? (y/n): ").lower()

        if play_again != "y":
            print("Thanks for playing!")
            break


#end of main function
main()
