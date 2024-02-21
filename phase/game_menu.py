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



