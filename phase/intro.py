import phase.phase_constants
from save_load import load_game
from entities import hero_data
from phase.check import phase_check


def game_init():
    print("Arkadius game \n jsi rdy? \n 0 - Ne \n 1 - Samozrejme ")
    should_continue = True
    while should_continue:
        user_input = int(input("Jaka je tvoje volba? \n"))
        if user_input != 0 and user_input != 1:
            print("Musis si vybrat aspon jednu")
            continue
        if user_input == 0:
            print("Nevadi zkus prijit priste")
            return phase.phase_constants.END
        print("Skvelee, mas odvahu!")
        return phase.phase_constants.NAME


def start_game():
    while True:
        print("0 - Zacit novou hru")
        print("1 - Nacist ulozenou hru")

        choice = input("Tak? ")
        if choice not in ["0", "1"]:
            print("vyber aslepon jednu moznost")
            continue
        if choice == "0":
            return phase.phase_constants.INTRO
        elif choice == "1":
            result, load_phase = load_game()
            print("Hra se nacetla, vitej zpet " + hero_data.hero_name)
            if result:
                return phase_check(load_game)

