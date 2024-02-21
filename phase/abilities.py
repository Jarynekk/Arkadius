import entities.hero_data
from ability_functions import print_abilities_description, print_abilities_points, print_abilities
from entities import hero_data
from entities.hero_data import abilities


def set_abilities(ability_points):
    hero_data.available_points += ability_points

    print(hero_data.hero_name + ", tvoje ability momentalne vypadaji takhle: ")
    print_abilities_points()

    ability_picked_count = 0
    abilities_picked = False

    while not abilities_picked:
        print_abilities(with_help_option=True)

        ability_input = input(
            "Mas " + str(ability_points - ability_picked_count)
            + " moznosti na zlepseni. Kterou schopnost chces vylepsit? ")
        if ability_input == "0":
            print_abilities_description()
            continue
        if ability_input.isnumeric() and int(ability_input) in list(range(1, len(abilities) + 1)):
            chosen_ability_name = list(abilities.keys())[int(ability_input) - 1]
            chosen_ability = abilities[chosen_ability_name]
            print("Vybral si schopnost " + chosen_ability_name + ", pridavam ti bod")

            if chosen_ability_name == "HP":
                chosen_ability_name = "HP"
                chosen_ability["points"] += 5
            else:
                chosen_ability["points"] += 1
            hero_data.available_points -= 1
            print_abilities_points()
        else:
            print("Netrefil si ani jednu moznost troubo, musis znovu..")
            continue

        ability_picked_count += 1
        if ability_picked_count == ability_points:
            abilities_picked = True
