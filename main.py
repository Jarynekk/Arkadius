import phase.phase_constants as phase_constants
import entities.hero_data as hero_data
from items.items import item_check, destroy_item_when_lost
from battle import battle
from phase import game_constants
from phase.abilities import set_abilities
from phase.check import phase_check, battle_check
from phase.game_constants import DIVIDER
from phase.intro import start_game, game_init
from phase.name import set_hero_name

current_phase = phase_constants.START

continue_game = True
while continue_game:
    if current_phase == phase_constants.START:
        current_phase = start_game()
    elif current_phase == phase_constants.INTRO:
        current_phase = game_init()
    elif current_phase == phase_constants.END:
        print(DIVIDER)
        print("Lucim bardzo")
        continue_game = False
    elif current_phase == phase_constants.NAME:
        print(DIVIDER)
        current_phase = set_hero_name()
    elif current_phase == phase_constants.INTRO_ABILITIES:
        print(DIVIDER)
        set_abilities(game_constants.INTRO_ABILITIES_COUNT)
        print(DIVIDER)
        current_phase = phase_check(phase_constants.FIGHT)
    elif current_phase == phase_constants.FIGHT:
        print(DIVIDER)
        is_boss_fight = hero_data.fight_level == game_constants.BOSS_FIGHT_LEVEL
        win, health_remaining = battle(hero_data.fight_level)
        if win:
            if is_boss_fight:
                current_phase = phase_constants.WON_GAME
                continue

            print("Po vitezne bitce ti zustalo " + str(health_remaining) + "/"
                  + str(hero_data.abilities["HP"]["points"]))
            print("Po pridani bodu a volby predmetu si budes moct zivoty doplnit")

            item_check(hero_data.fight_level)

            print(DIVIDER)
            print("Po tvoji " + str(hero_data.fight_level) + ". vyhre ti pridavam "
                  + str(hero_data.fight_level) + " bodu, ktere muzes vyuzit na vylepseni hrdiny")
            set_abilities(hero_data.fight_level)

            hero_data.fight_level += 1

            if hero_data.fight_level == game_constants.BOSS_FIGHT_LEVEL:
                print("Tvuj dalsi a zaroven posledni souper bude ten nejsilnejsi!")
            print(DIVIDER)
        else:
            destroy_item_when_lost()
            print("Potrebujes si oddychnout a prehodnotit svoje schopnosti")
            print(DIVIDER)

        max_health = hero_data.abilities["HP"]["points"]
        hero_data.abilities["HP"]["points"] = health_remaining
        current_phase = battle_check(hero_data.fight_level, max_health)

    elif current_phase == phase_constants.WON_GAME:
        print(DIVIDER)
        print("\nPrave si porazil bosse a dokoncil celou hru!!! congrats")
        break
