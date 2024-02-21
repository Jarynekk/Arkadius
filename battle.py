import random

from entities.hero_data import abilities
from entities.enemy_data import enemies
from phase import game_constants
import time


def calculate_hero_attack():
    return (abilities["Strength"]["points"],
            abilities["Strength"]["points"] + abilities["Dexterity"]["points"] + abilities["Skill"]["points"])


def calculate_enemy_attack(enemy_data):
    return (enemies["Strength"],
            enemies["Strength"] + enemies["Dexterity"] + enemies["Skill"])


def print_hero_stats(hero):
    print("Tvuj hrdina:")
    print("Utok: minimum - " + str(hero["attack"][0]) + ", maximum - " + str(hero["attack"][1]))
    print("Sance na krit: " + str(hero["critical_hit"]) + "%")
    print("Obrana: minimum - " + str(hero["defense"][0]) + ", maximum - " + str(hero["defense"][1]))
    print("Zivoty: ", str(hero["health"]))


def print_enemy_stats(enemy):
    print("Tvuj enemak:" + enemy["name"])
    print("Utok: minimum - " + str(enemy["attack"][0]) + ", maximum - " + str(enemy["attack"][1]))
    print("Sance na krit: " + str(enemy["critical_hit"]) + "%")
    print("Obrana: minimum - " + str(enemy["defense"][0]) + ", maximum - " + str(enemy["defense"][1]))
    print("Zivoty: ", str(enemy["health"]))


def is_critical_hit(chance):
    return random.randint(0, 100) < chance


def battle(fight_level):
    enemy_data = enemies[fight_level]

    hero = {
        "attack": calculate_hero_attack(),
        "critical_hit": min(100, (abilities["Skill"]["points"] * abilities["Luck"]["points"]) // 2),
        "defense": (abilities["Defense"]["points"], abilities["Defense"]["points"] + abilities["Dexterity"]["points"]),
        "health": abilities["HP"]["points"]
    }

    enemy = {
        "name": enemy_data["name"],
        "attack": calculate_hero_attack(),
        "critical_hit": min(100, (enemy_data["Skill"] * enemy_data["Luck"]) // 2),
        "defense": (enemy_data["Defense"], enemy_data["Defense"] + enemy_data["Dexterity"]),
        "health": enemy_data["HP"]
    }
    return simulate_battle(hero, enemy)


def simulate_battle(hero, enemy):
    print(game_constants.DIVIDER)
    print_hero_stats(hero)
    print()
    time.sleep(2)
    print_enemy_stats(enemy)
    time.sleep(3)

    print(game_constants.DIVIDER)
    print("\nZaciname souboj, zacinas!\n")

    hero_turn = True
    while True:
        if hero_turn:
            min_attack, max_attack = hero["attack"]
            attack = random.randint(min_attack, max_attack)
            if is_critical_hit(hero["critical_hit"]):
                attack *= 3
                print("Utocis kritickym zasahem")

            min_defense, max_defense = enemy["defense"]
            defense = random.randint(min_defense, max_defense)

            #final_attack = attack-defense
            final_attack = max((attack-defense), 0)

            if final_attack > 0:
                print("Zautocil si silou ", final_attack)
                enemy["health"] -= final_attack

                if enemy["health"] > 0:
                    print(enemy["name"] + " stale zije se zbyvajicim hp: " + str(enemy["health"]))
                else:
                    time.sleep(1)
                    print("Zvitezil si!!")
                    print(game_constants.DIVIDER)
                    return True, hero["health"]
            else:
                print("Netrefils...")

        else:
            min_attack, max_attack = enemy["attack"]
            attack = random.randint(min_attack, max_attack)
            if is_critical_hit(enemy["critical_hit"]):
                attack *= 3
                print("Souper utoci kritickym utokem..")

            min_defense, max_defense = hero["defense"]
            defense = random.randint(min_defense, max_defense)

            #final_attack = attack - defense
            final_attack = max((attack-defense), 0)

            if final_attack > 0:
                print(enemy["name"] + " utoci silou ", final_attack)
                hero["health"] -= final_attack

                if hero["health"] > 0:
                    print("Po utoku ti zbyva " + str(hero["health"]) + " zivotu")
                else:
                    time.sleep(1)
                    print("Byl si porazen..")
                    print(game_constants.DIVIDER)
                    return False, 0
            else:
                print("Souperuv utok te netrefil...")

        print()
        hero_turn = not hero_turn
        time.sleep(2)
