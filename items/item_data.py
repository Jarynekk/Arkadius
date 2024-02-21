items = {
    1: {
        1: {
            "name": "Nápoj zdravi (LVL 1)",
            "description": "Pridá 15 zdravi. Kdyz pri souboji umres, tak napoj vyprcha.",
            "ability": {
                "HP": 15
            },
            "tag": "drink",
            "replaceable": False,
            "destroy_when_lost": True
        },
        2: {
            "name": "Látkové brneni (LVL 1)",
            "description": "Prida 2 obrany, zustava dokud ho sam nevymenis.",
            "ability": {
                "Defense": 2
            },
            "tag": "armor",
            "replaceable": True,
            "destroy_when_lost": False
        },
        3: {
            "name": "Boticky (LVL 1)",
            "description": "Prida 1 obratnost, zustava dokud ho sam nevymenis.",
            "ability": {
                "Dexterity": 1
            },
            "tag": "boots",
            "replaceable": True,
            "destroy_when_lost": False
        },
    },
    2: {
        1: {
            "name": "Napoj stesti (LVL 2)",
            "description": "Prida 5 stesti. Kdyz pri souboji umres, tak napoj vyprcha.",
            "ability": {
                "Luck": 5
            },
            "tag": "drink",
            "replaceable": False,
            "destroy_when_lost": True
        },
        2: {
            "name": "Krátky meč (LVL 2)",
            "description": "Pridá 3 utocne sily, zustava dokud ho sam nevymenis.",
            "ability": {
                "Strength": 3
            },
            "tag": "weapon",
            "replaceable": True,
            "destroy_when_lost": False
        },
        3: {
            "name": "Tréning gladiátora (LVL 2)",
            "description": "Prida 2 body skillu. Schopnosti ti nevyprchaji.",
            "ability": {
                "Skill": 2
            },
            "tag": "training",
            "replaceable": False,
            "destroy_when_lost": False
        },
    },
    3: {
        1: {
            "name": "Energetak (LVL 3)",
            "description": "Prida 2 body utocne sily, 2 body obrane a 2 body skillu. Kdyz pri souboji umres, "
                           "tak napoj vyprcha.",
            "ability": {
                "Strength": 2,
                "Defense": 2,
                "Skill": 2,
            },
            "tag": "drink",
            "replaceable": False,
            "destroy_when_lost": True
        },
        2: {
            "name": "Dlouhý meč (LVL 3)",
            "description": "Prida 5 utocne sily, zustava dokud ho sam nevymenis.",
            "ability": {
                "Strength": 5
            },
            "tag": "weapon",
            "replaceable": True,
            "destroy_when_lost": False
        },
        3: {
            "name": "Kožené boticky (LVL 3)",
            "description": "Prida 2 Obratnosti a 2 body obrany, zustava dokud je sam nevymenis.",
            "ability": {
                "Dexterity": 2,
                "Defense": 2,
            },
            "tag": "boots",
            "replaceable": True,
            "destroy_when_lost": False
        },
        4: {
            "name": "Ocelove brnenie (LVL 3)",
            "description": "Pridá 5 obrany, zustava dokud je sam nevymenis.",
            "ability": {
                "Defense": 5
            },
            "tag": "armor",
            "replaceable": True,
            "destroy_when_lost": False
        },
    },
    4: {
        1: {
            "name": "Pivinko (LVL 4)",
            "description": "Pridá 30 Života a 10 stesti. Kdyz pri souboji umres, tak napoj vyprcha.",
            "ability": {
                "HP": 30,
                "Luck": 10,
            },
            "tag": "drink",
            "replaceable": False,
            "destroy_when_lost": True
        },
        2: {
            "name": "Dvojhlavá sekera (LVL 4)",
            "description": "Pridá 10 utocne sily, zustava dokud je sam nevymenis.",
            "ability": {
                "Strength": 10
            },
            "tag": "weapon",
            "replaceable": True,
            "destroy_when_lost": False
        },
        3: {
            "name": "Tréning Spartana (LVL 4)",
            "description": "Pridá 4 body skillu, 2 body utocne sily a 2 body obrane. Schopnosti ti nevyprchaji.",
            "ability": {
                "Skill": 3,
                "Strength": 3,
                "Defense": 3
            },
            "tag": "training",
            "replaceable": False,
            "destroy_when_lost": False
        },
        4: {
            "name": "Rímsky štít (LVL 4)",
            "description": "Pridá 16 obrany, ale odebere 2 body obratnosti. Zostáva ti do konca hry",
            "ability": {
                "Defense": 16,
                "Dexterity": -2
            },
            "tag": "armor",
            "replaceable": False,
            "destroy_when_lost": False
        },
    }
}
