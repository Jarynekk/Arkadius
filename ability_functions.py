from entities import hero_data
from entities.hero_data import abilities, hero_items
from phase import game_constants


def print_abilities(with_help_option=False):
    if with_help_option:
        print("0 - Vysvetlivky - načo su dobré jednotlivé schopnosti?")

    for i, ability in enumerate(abilities.keys()):
        ability_option = str(i + 1) + ' - ' + ability
        if ability == "Život":
            ability_option += " " + "- jeden bod pridá 5 života"
        print(ability_option)


def print_abilities_points():
    print("Tvoje schopnosti: ")
    for x, y in abilities.items():
        print(x + " - " + str(y["points"]), end=", ")
    print("\n")


def print_abilities_description():
    print(game_constants.DIVIDER)
    for k, v in abilities.items():
        print(k + " - " + str(v["description"]))
    print(game_constants.DIVIDER)


def print_items():
    for item in hero_items:
        print(item["name"] + "->" + item["description"])
    print()


def hero_update():
    while True:
        print("0 - Zpet")
        print("1 - Pridat body (mas " + str(hero_data.available_points) + " bodov na pridanie)")
        print("2 - Odstranit body zo schopnosti")

        choice = input("Co chces robit? ")
        if choice not in ["0", "1", "2"]:
            print("musis vybrat alespon jednu moznost")
            continue
        if choice == "0":
            break
        elif choice == "1":
            if hero_data.available_points > 0:
                hero_add_points()
            else:
                print("Nemas dostupne zadne body na pridani")
                continue
        elif choice == "2":
            hero_remove_points()


def hero_add_points():
    while True:
        if hero_data.available_points < 1:
            print("Nemas dostupne zadne body na pridani")
            break

        print("Mas " + str(hero_data.available_points) + " bodu na pridani schopnosti")
        print("0 - zpet, uz nechci pridavat body")
        print_abilities_points()
        ability_input = input("Ktere schopnosti chces pridat bod? ")

        if ability_input == "0":
            break

        if ability_input.isnumeric() and int(ability_input) in list(range(1, len(abilities) + 1)):
            chosen_ability_name = list(abilities.keys())[int(ability_input) - 1]
            chosen_ability = abilities[chosen_ability_name]

            print("Vybral si schopnost " + chosen_ability_name + ", pridavam ti bod")

            if chosen_ability_name == "HP":
                chosen_ability["points"] += 5
            else:
                chosen_ability["points"] += 1
            print_abilities_points()
            hero_data.available_points -= 1
        else:
            print("Netrefil si ani jednu moznost troubo, musis znovu..")
            continue


def hero_remove_points():
    while True:
        print("0 - zpet, uz nechci odebirat body")
        print_abilities_points()
        ability_input = input("Ktere schopnosti chces odebrat bod? ")

        if ability_input == "0":
            break

        if ability_input.isnumeric() and int(ability_input) in list(range(1, len(abilities) + 1)):
            chosen_ability_name = list(abilities.keys())[int(ability_input) - 1]
            chosen_ability = abilities[chosen_ability_name]
            if chosen_ability["points"] < 1:
                print("Tehle schopnosti jiz nemuzes odebrat bod")
                break

            print("Vybral si schopnost " + chosen_ability_name + ", pridavam ti bod")
            hero_data.available_points += 1

            if chosen_ability_name == "HP":
                chosen_ability["points"] -= 5
            else:
                chosen_ability["points"] -= 1
            print_abilities_points()
        else:
            print("Netrefil si ani jednu moznost troubo, musis znovu..")
            continue
