from ability_functions import print_abilities_points, hero_update, hero_data, print_items
import phase.phase_constants as phase_constants
from entities import enemy_data
from phase import game_constants
from save_load import save_game
import time


def hero_check():
    print()
    print(hero_data.hero_name + ", tvoje momentalni schopnosti:")
    print_abilities_points()
    if len(hero_data.hero_items) > 0:
        print("Mas nasledujici predmety(body jsou zapocitane): ")
        print_items()
    else:
        print("Zatim nemas zadne predmety.")

    print("Mas " + str(hero_data.available_points) + " bodu na pridani schopnosti")

    while True:
        print("0 - zpet")
        print("1 - upravit schopnosti")

        choice = input("Co chces robit? ")
        if choice not in ["0", "1"]:
            print("musis vybrat alespon jednu moznost")
            continue
        if choice == "0":
            break
        elif choice == "1":
            hero_update()


def phase_check(next_phase):
    if next_phase == phase_constants.FIGHT:
        text = "fight - level " + str(hero_data.fight_level)
        if hero_data.fight_level == game_constants.BOSS_FIGHT_LEVEL:
            text = "Posledni " + text
    else:
        text = next_phase

    while True:
        print("0 - Pokracovat na ", text)
        print("1 - Upravit hrdinu")
        print("2 - Ulozit hru")
        print("3 - Ukoncit hru")
        choice = input("Jaky je tvuj dalsi krok?")
        if choice not in ["0", "1", "2", "3"]:
            print("netrefil ses")
            continue

        if choice == "0":
            return next_phase
        elif choice == "1":
            hero_check()
        elif choice == "2":
            save_game(next_phase, hero_data.fight_level)
        elif choice == "3":
            if end_game_choice():
                return phase_constants.END
            else:
                print()
                continue


def battle_check(fight_level, max_health):
    enemy_name = enemy_data.enemies[fight_level]["name"]
    if fight_level == game_constants.BOSS_FIGHT_LEVEL:
        fight_enemy_text = "Posledni souboj. " + enemy_name
    else:
        fight_enemy_text = enemy_name

    while True:
        print("0 - Oddychnout si - " + rest_text(max_health))
        print("1 - Bojovat proti - " + fight_enemy_text)
        print("2 - Upravit hrdinu")
        print("3 - Ulozit hru")
        print("4 - Ukoncit hru")
        choice = input("Aký je tvoj ďalsí krok?: ")
        if choice not in ["0", "1", "2", "3", "4"]:
            print("netrefil ses")
            continue
        if choice == "0":
            if hero_data.abilities["HP"]["points"] < max_health:
                print("Dobra volba, cas na pauzu")
                time.sleep(2)
                hero_data.abilities["HP"]["points"] = min(hero_data.abilities["HP"]["points"] + 20, max_health)
                print("Po oddychnuti ses vylecil o 20 zivotu a mas "
                      + str(hero_data.abilities["HP"]["points"]) + "/" + str(max_health))
                print()
            else:
                print("Mas plne zivoty:]")
                print()
        elif choice == "1":
            return phase_constants.FIGHT
        elif choice == "2":
            hero_check()
        elif choice == "3":
            save_game(phase_constants.FIGHT, fight_level)
        elif choice == "4":
            if end_game_choice():
                return phase_constants.END
            else:
                print()
                continue


def rest_text(max_health):
    hero_current_hp = hero_data.abilities["HP"]["points"]
    if hero_current_hp < max_health:
        text = "Obnovit 20 zivotu, do plnych ti chybi " + str(max_health - hero_current_hp) + " bodu"
    else:
        text = "Mas sice plne zivoty ale nekdy je treba si oddychnout"
    return text


def end_game_choice():
    while True:
        choice = input("Ses si jisty ze chces ukoncit hru?\n 1 = Ano, ukoncit \n 2 = zpet")
        if choice not in ["1", "2"]:
            print("musis vybrat alespon jednu moznost")
            continue
        if choice == "1":
            return True
        if choice == "0":
            return False
