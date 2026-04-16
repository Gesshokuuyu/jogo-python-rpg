# =========================
# PADRÕES
# =========================

CLASSES = ["guerreiro", "arqueiro", "mago"]

TIPOS_ARMADURA = ["head", "chest", "legs"]

# =========================
# ARMADURAS
# =========================

ARMADURAS = {
    # --- HEAD ---
    "ab-h-l1": {
        "nome": "Capuz Simples",
        "tipo": "armadura",
        "slot": "head",
        "nivel": 1,
        "defesa": 2,
        "preco": 15,
        "classe": ["arqueiro", "mago"]
    },
    "ab-h-l2": {
        "nome": "Elmo de Ferro",
        "tipo": "armadura",
        "slot": "head",
        "nivel": 2,
        "defesa": 5,
        "preco": 40,
        "classe": ["guerreiro"]
    },
    "ab-h-l3": {
        "nome": "Coroa do Arcano",
        "tipo": "armadura",
        "slot": "head",
        "nivel": 3,
        "defesa": 4,
        "magia": 8,
        "preco": 80,
        "classe": ["mago"]
    },
    "ab-h-l3b": {
        "nome": "Elmo do Dragão",
        "tipo": "armadura",
        "slot": "head",
        "nivel": 3,
        "defesa": 10,
        "preco": 100,
        "classe": ["guerreiro"]
    },

    # --- CHEST ---
    "ab-c-l1": {
        "nome": "Armadura de Couro",
        "tipo": "armadura",
        "slot": "chest",
        "nivel": 1,
        "defesa": 5,
        "preco": 20,
        "classe": ["arqueiro", "guerreiro"]
    },
    "ab-c-l2": {
        "nome": "Robe Arcano",
        "tipo": "armadura",
        "slot": "chest",
        "nivel": 2,
        "defesa": 4,
        "magia": 6,
        "preco": 50,
        "classe": ["mago"]
    },
    "ab-c-l2b": {
        "nome": "Cota de Malha",
        "tipo": "armadura",
        "slot": "chest",
        "nivel": 2,
        "defesa": 8,
        "preco": 55,
        "classe": ["guerreiro", "arqueiro"]
    },
    "ab-c-l3": {
        "nome": "Peitoral de Mithril",
        "tipo": "armadura",
        "slot": "chest",
        "nivel": 3,
        "defesa": 14,
        "preco": 120,
        "classe": CLASSES
    },

    # --- LEGS ---
    "ab-l-l1": {
        "nome": "Calça Simples",
        "tipo": "armadura",
        "slot": "legs",
        "nivel": 1,
        "defesa": 3,
        "preco": 10,
        "classe": CLASSES
    },
    "ab-l-l2": {
        "nome": "Grevas de Ferro",
        "tipo": "armadura",
        "slot": "legs",
        "nivel": 2,
        "defesa": 6,
        "preco": 35,
        "classe": ["guerreiro"]
    },
    "ab-l-l2b": {
        "nome": "Calça de Caçador",
        "tipo": "armadura",
        "slot": "legs",
        "nivel": 2,
        "defesa": 4,
        "destreza": 3,
        "preco": 35,
        "classe": ["arqueiro"]
    },
    "ab-l-l3": {
        "nome": "Grevas Encantadas",
        "tipo": "armadura",
        "slot": "legs",
        "nivel": 3,
        "defesa": 9,
        "preco": 90,
        "classe": CLASSES
    },
}


# =========================
# ARMAS
# =========================

ARMAS = {
    # --- GUERREIRO ---
    "ar-g-l1": {
        "nome": "Espada Básica",
        "tipo": "arma",
        "nivel": 1,
        "ataque": 8,
        "preco": 20,
        "classe": ["guerreiro"]
    },
    "ar-g-l2": {
        "nome": "Espada de Aço",
        "tipo": "arma",
        "nivel": 2,
        "ataque": 14,
        "preco": 60,
        "classe": ["guerreiro"]
    },
    "ar-g-l3": {
        "nome": "Lâmina Flamejante",
        "tipo": "arma",
        "nivel": 3,
        "ataque": 22,
        "preco": 150,
        "classe": ["guerreiro"]
    },

    # --- ARQUEIRO ---
    "ar-a-l1": {
        "nome": "Arco Curto",
        "tipo": "arma",
        "nivel": 1,
        "ataque": 6,
        "destreza": 3,
        "preco": 20,
        "classe": ["arqueiro"]
    },
    "ar-a-l2": {
        "nome": "Arco Longo",
        "tipo": "arma",
        "nivel": 2,
        "ataque": 11,
        "destreza": 5,
        "preco": 60,
        "classe": ["arqueiro"]
    },
    "ar-a-l3": {
        "nome": "Arco do Vento",
        "tipo": "arma",
        "nivel": 3,
        "ataque": 18,
        "destreza": 8,
        "preco": 150,
        "classe": ["arqueiro"]
    },

    # --- MAGO ---
    "ar-m-l1": {
        "nome": "Cajado Simples",
        "tipo": "arma",
        "nivel": 1,
        "ataque": 4,
        "magia": 6,
        "preco": 20,
        "classe": ["mago"]
    },
    "ar-m-l2": {
        "nome": "Cajado de Cristal",
        "tipo": "arma",
        "nivel": 2,
        "ataque": 7,
        "magia": 12,
        "preco": 60,
        "classe": ["mago"]
    },
    "ar-m-l3": {
        "nome": "Báculo das Sombras",
        "tipo": "arma",
        "nivel": 3,
        "ataque": 12,
        "magia": 20,
        "preco": 150,
        "classe": ["mago"]
    },
}


# =========================
# CONSUMÍVEIS
# =========================

CONSUMIVEIS = {
    "co-hp-l1": {
        "nome": "Poção de Vida",
        "tipo": "consumivel",
        "nivel": 1,
        "cura": 30,
        "preco": 10,
    },
    "co-hp-l2": {
        "nome": "Poção de Vida Grande",
        "tipo": "consumivel",
        "nivel": 2,
        "cura": 70,
        "preco": 25,
    },
    "co-mp-l1": {
        "nome": "Poção de Mana",
        "tipo": "consumivel",
        "nivel": 1,
        "mana": 20,
        "preco": 10,
    },
    "co-mp-l2": {
        "nome": "Elixir de Mana",
        "tipo": "consumivel",
        "nivel": 2,
        "mana": 50,
        "preco": 25,
    },
    "co-antidoto": {
        "nome": "Antídoto",
        "tipo": "consumivel",
        "nivel": 1,
        "cura": 10,
        "preco": 8,
    },
}


# =========================
# INIMIGOS
# =========================

INIMIGOS = {
    # --- FLORESTA ---
    "e-lobo": {
        "nome": "Lobo Selvagem",
        "hp": 35,
        "ataque": 7,
        "defesa": 2,
        "xp": 15,
        "ouro": 8,
        "loot": [
            {"item_id": "co-hp-l1", "chance": 50},
            {"item_id": "ab-l-l1", "chance": 10},
        ]
    },
    "e-goblin": {
        "nome": "Goblin",
        "hp": 40,
        "ataque": 8,
        "defesa": 3,
        "xp": 20,
        "ouro": 12,
        "loot": [
            {"item_id": "co-hp-l1", "chance": 40},
            {"item_id": "ab-h-l1", "chance": 15},
            {"item_id": "co-mp-l1", "chance": 20},
        ]
    },
    "e-sombria": {
        "nome": "Criatura Sombria",
        "hp": 50,
        "ataque": 10,
        "defesa": 4,
        "xp": 30,
        "ouro": 18,
        "loot": [
            {"item_id": "co-hp-l1", "chance": 60},
            {"item_id": "ab-c-l1", "chance": 15},
        ]
    },

    # --- CAVERNA ---
    "e-troll": {
        "nome": "Troll da Caverna",
        "hp": 80,
        "ataque": 14,
        "defesa": 6,
        "xp": 45,
        "ouro": 25,
        "loot": [
            {"item_id": "co-hp-l2", "chance": 40},
            {"item_id": "ab-c-l2b", "chance": 15},
            {"item_id": "ab-l-l2", "chance": 15},
        ]
    },
    "e-esqueleto": {
        "nome": "Esqueleto Guerreiro",
        "hp": 60,
        "ataque": 12,
        "defesa": 8,
        "xp": 35,
        "ouro": 20,
        "loot": [
            {"item_id": "co-hp-l1", "chance": 50},
            {"item_id": "ar-g-l2", "chance": 8},
        ]
    },
    "e-aranha": {
        "nome": "Aranha Gigante",
        "hp": 55,
        "ataque": 11,
        "defesa": 3,
        "xp": 30,
        "ouro": 15,
        "loot": [
            {"item_id": "co-antidoto", "chance": 60},
            {"item_id": "co-hp-l1", "chance": 40},
        ]
    },

    # --- MINI BOSS ---
    "e-golem": {
        "nome": "Golem de Pedra",
        "hp": 150,
        "ataque": 18,
        "defesa": 12,
        "xp": 80,
        "ouro": 60,
        "is_boss": True,
        "loot": [
            {"item_id": "co-hp-l2", "chance": 100},
            {"item_id": "ab-c-l2b", "chance": 50},
            {"item_id": "ar-g-l2", "chance": 30},
            {"item_id": "ar-a-l2", "chance": 30},
            {"item_id": "ar-m-l2", "chance": 30},
        ]
    },

    # --- TORRE ---
    "e-cavaleiro": {
        "nome": "Cavaleiro das Trevas",
        "hp": 90,
        "ataque": 16,
        "defesa": 10,
        "xp": 50,
        "ouro": 30,
        "loot": [
            {"item_id": "co-hp-l2", "chance": 50},
            {"item_id": "ab-h-l3b", "chance": 10},
        ]
    },
    "e-espectro": {
        "nome": "Espectro",
        "hp": 70,
        "ataque": 20,
        "defesa": 5,
        "xp": 55,
        "ouro": 35,
        "loot": [
            {"item_id": "co-mp-l2", "chance": 50},
            {"item_id": "ab-h-l3", "chance": 10},
        ]
    },

    # --- BOSS FINAL ---
    "e-morvak": {
        "nome": "Morvak, o Senhor das Sombras",
        "hp": 300,
        "ataque": 25,
        "defesa": 15,
        "xp": 200,
        "ouro": 500,
        "is_boss": True,
        "loot": []
    },
}


# =========================
# MERCADORES
# =========================

MERCADORES = {
    "m-taverna": {
        "nome": "Baldric, o Mercador",
        "saudacao": "Bem-vindo, aventureiro! Dê uma olhada nas minhas mercadorias.",
        "itens": [
            "co-hp-l1", "co-hp-l2", "co-mp-l1", "co-mp-l2", "co-antidoto",
            "ab-h-l1", "ab-c-l1", "ab-l-l1",
            "ar-g-l1", "ar-a-l1", "ar-m-l1",
        ]
    },
    "m-caverna": {
        "nome": "Dúrin, o Anão",
        "saudacao": "Hmpf... Tenho coisas boas. Se tiver ouro, claro.",
        "itens": [
            "co-hp-l2", "co-mp-l2", "co-antidoto",
            "ab-h-l2", "ab-c-l2", "ab-c-l2b", "ab-l-l2", "ab-l-l2b",
            "ar-g-l2", "ar-a-l2", "ar-m-l2",
        ]
    },
}
