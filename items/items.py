from ability_functions import print_items
from entities import hero_data
from items.item_data import items


def get_item_by_name(name):
    for item_in_level in items.values():
        for item in item_in_level.values():
            if item["name"] == name:
                return item
    return None


def destroy_item_when_lost():
    items_to_remove = []
    for item in hero_data.hero_items:
        if item["destroy_when_lost"]:
            items_to_remove.append(item)
    if len(items_to_remove) > 0:
        for to_remove in items_to_remove:
            remove_item(to_remove)
        print("Po prohrane bitve se ti vymazali nasledujici predmety: ")
        for item in items_to_remove:
            print(item["name"], end=",")
        print()


def remove_item(item):
    abilities_to_remove = item["ability"]
    for ability_key, ability_value in abilities_to_remove.items():
        hero_data.abilities[ability_key]["points"] -= ability_value
    hero_data.hero_items.remove(item)


def replace_item(chosen_item):
    if chosen_item["replaceable"]:
        tag = chosen_item["tag"]
        for hero_item in hero_data.hero_items:
            if hero_item["replaceable"] and hero_item["tag"] == tag:
                return hero_item
    return None


def add_item(item):
    abilities_to_add = item["ability"]
    for ability_key, ability_value in abilities_to_add.items():
        if ability_value > 0:
            hero_data.abilities[ability_key]["points"] += ability_value
        else:
            hero_data.abilities[ability_key]["points"] = (
                max(0, hero_data.abilities[ability_key]["points"] - ability_value))
    hero_data.hero_items.append(item)


def item_check(level):
    available_new_items = items[level]
    print("\nPo vyhre mas na vyber z " + str(len(available_new_items)) + " itemu")
    new_items_key = list(available_new_items.keys())

    should_continue = True
    while should_continue:
        for item_key, item_value in available_new_items.items():
            print(str(item_key) + " - " + item_value["name"] + " -> " + item_value["description"])

        choice = input("Ktery item budes chtit ? ")
        if not choice.isnumeric() or int(choice) not in new_items_key:
            print("Netrefils ani jednu moznou volbu.")
            continue

        chosen_item = available_new_items[int(choice)]
        item_to_replace = replace_item(chosen_item)

        if item_to_replace is not None:
            print("Vybral sis " + chosen_item["name"] + ", musel bys zahodit " + item_to_replace["name"])

            confirm = False
            while True:
                print("0 - Ok, potvrzuji")
                print("1 - Ne, vyberu neco jineho")
                replace_choice = input(" ")
                if replace_choice not in ["0","1"]:
                    print("Netrefil si ani jednu moznost")
                    continue

                if replace_choice == "0":
                    confirm = True
                    break
                if replace_choice == "1":
                    break

            if confirm:
                remove_item(item_to_replace)
                add_item(chosen_item)
                should_continue = False
            else:
                print("Opakuji vyber predmetu...")
                continue
        else:
            add_item(chosen_item)
            should_continue = False

    print("\nTvoje predmety se aktualizovali..")
    print_items()
