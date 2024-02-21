from entities import hero_data
import phase.phase_constants as phase_constants


def set_hero_name():
    name_picked = False
    hero_name = ""
    while not name_picked:
        name = input("Zadej jak se bude tvuj hrdina jmenovat: ")
        print("Isto se tvuj hrdina bude jmenovat " + name + " ?")
        name_choice = input("Pokud ano zadej 1 pokud ne zadej 0 ")

        if name_choice not in ["0", "1"]:
            print("Mas zadat 0 nebo 1, musim se zeptat znovu..")
            continue
        elif name_choice == "1":
            print("skvele, mas nastavene jmeno")
            hero_data.hero_name = name
            name_picked = True
            return phase_constants.INTRO_ABILITIES
        elif name_choice == "0":
            continue
    print("Vitaam " + hero_name)
