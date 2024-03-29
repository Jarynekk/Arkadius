from entities import hero_data
from os import listdir
from os.path import isfile, join
from items.items import get_item_by_name
from phase import game_constants


def save_game(next_phase, fight_level):
    print("Pod jakym nazvem chces hru ulozit? jen pismenka plski")
    while True:
        save_name = input("Nazev - ")
        if save_name.isalpha():  # kontroluje jestli jsou na vstupu jen pismenka
            file_path = "saved/" + save_name + ".txt"
            file_handler = open(file_path, "w", encoding="utf-8")  # utf-8 kvuli diakritice
            file_handler.write(hero_data.hero_name)
            file_handler.write("\n")
            for k, v in hero_data.abilities.items():
                file_handler.write(str(k) + " - " + str(v["points"]))
                file_handler.write("\n")
            file_handler.write(str(fight_level))
            file_handler.write("\n")
            file_handler.write(next_phase)
            file_handler.write("\n")
            file_handler.write(str(hero_data.available_points))
            file_handler.write("\n")

            for item in hero_data.hero_items:
                file_handler.write(item["name"])
                file_handler.write("\n")
            file_handler.close()
            print("Hra byla uspesne ulozena")
            break
        else:
            print("Nazev neobsahuje jen pismenka")
            continue


def load_game():
    print(game_constants.DIVIDER)
    saves = []
    for file in listdir("saved"):
        if isfile(join("saved", file)):
            saves.append(file)
    if len(saves) > 0:
        print("0 - zpet")
        for i, save in enumerate(saves):
            print(str(i + 1) + " - " + save.replace(".txt", ""))

        while True:
            choice = input("Kterou hru chces nacist?")
            if choice == "0":
                print()
                return False, ""

            if not choice.isdigit() or int(choice) not in list(range(1, len(saves) + 1)):
                print("Netrefil si ani jednu moznost")
                continue
            else:
                game_to_load = saves[int(choice) - 1]
                return load(game_to_load)
    else:
        print("Nemas zadne ulozene hry kamosu")
        return False, ""


def load(file_name):
    print("Nacitam hru ulozenou pod nazvem " + file_name.replace(".txt", ""))
    with open("saved/" + file_name, encoding="utf-8") as f:
        name_loaded = False
        abilities_loaded = False
        abilities_loaded_count = 0
        available_points_loaded = False
        fight_level_loaded = False
        next_phase = ""
        next_phase_loaded = False
        hero_items_loaded = False

        for line in f:
            if not name_loaded:
                hero_data.hero_name = line.rstrip()
                name_loaded = True
            elif not abilities_loaded:
                ability_key, points = line.rstrip().split(" - ")
                hero_data.abilities[ability_key]["points"] = int(points)
                abilities_loaded_count += 1
                if abilities_loaded_count == len(hero_data.abilities):
                    abilities_loaded = True
            elif not fight_level_loaded:
                hero_data.fight_level = int(line.rstrip())
                fight_level_loaded = True
            elif not next_phase_loaded:
                next_phase = line.rstrip()
                next_phase_loaded = True
            elif not available_points_loaded:
                hero_data.available_points = int(line.rstrip())
                available_points_loaded = True
            elif not hero_items_loaded:
                item_name = line.rstrip()
                hero_data.hero_items.append(get_item_by_name(item_name))

        print()
        return True, next_phase
