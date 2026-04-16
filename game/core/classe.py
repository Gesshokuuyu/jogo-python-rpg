# game/core/classe.py

from game.data.helpers.dataHelper import get_item_by_id
from game.core.ui import titulo, menu, escolha, sucesso, info_item, COR_ITEM, COR_MENU, COR_XP


CLASSES_CONFIG = {
    "1": {
        "nome": "Guerreiro",
        "descricao": "Mestre em combate corpo a corpo. Alta vida e defesa.",
        "hp": 120,
        "mana": 20,
        "ataque": 12,
        "defesa": 8,
        "magia": 0,
        "destreza": 2,
        "arma_id": "ar-g-l1",
        "armadura_id": "ab-c-l1",
        "habilidade_nome": "Golpe Brutal",
        "habilidade_dano": 25,
        "habilidade_custo": 15,
    },
    "2": {
        "nome": "Arqueiro",
        "descricao": "Ágil e preciso. Ataques rápidos com alta destreza.",
        "hp": 90,
        "mana": 30,
        "ataque": 9,
        "defesa": 5,
        "magia": 0,
        "destreza": 8,
        "arma_id": "ar-a-l1",
        "armadura_id": "ab-l-l1",
        "habilidade_nome": "Chuva de Flechas",
        "habilidade_dano": 20,
        "habilidade_custo": 20,
    },
    "3": {
        "nome": "Mago",
        "descricao": "Domina as artes arcanas. Devastador com magia.",
        "hp": 75,
        "mana": 60,
        "ataque": 5,
        "defesa": 3,
        "magia": 12,
        "destreza": 2,
        "arma_id": "ar-m-l1",
        "armadura_id": "ab-h-l1",
        "habilidade_nome": "Bola de Fogo",
        "habilidade_dano": 30,
        "habilidade_custo": 25,
    },
}


def escolher_classe(player):
    """Menu de escolha de classe. Aplica stats ao player."""
    titulo("ESCOLHA SUA CLASSE")

    for key, cfg in CLASSES_CONFIG.items():
        arma = get_item_by_id(cfg["arma_id"])
        print(COR_MENU + f"  [{key}] " + COR_XP + f"{cfg['nome']}")
        print(COR_MENU + f"      {cfg['descricao']}")
        print(COR_MENU + f"      HP: {cfg['hp']} | Mana: {cfg['mana']} | ATK: {cfg['ataque']} | DEF: {cfg['defesa']}")
        if arma:
            print(COR_ITEM + f"      Arma inicial: {arma['nome']}")
        print()

    op = escolha("Escolha (1/2/3): ", validas=["1", "2", "3"])
    cfg = CLASSES_CONFIG[op]

    player.classe = cfg["nome"]
    player.hp = cfg["hp"]
    player.hp_max = cfg["hp"]
    player.mana = cfg["mana"]
    player.mana_max = cfg["mana"]
    player.ataque = cfg["ataque"]
    player.defesa = cfg["defesa"]
    player.magia = cfg["magia"]
    player.destreza = cfg["destreza"]
    player.habilidade_nome = cfg["habilidade_nome"]
    player.habilidade_dano = cfg["habilidade_dano"]
    player.habilidade_custo = cfg["habilidade_custo"]

    # Equipar arma inicial
    arma = get_item_by_id(cfg["arma_id"])
    if arma:
        player.equipamento["arma"] = arma
        info_item(f"Arma equipada: {arma['nome']}")

    # Equipar armadura inicial
    armadura = get_item_by_id(cfg["armadura_id"])
    if armadura:
        slot = armadura.get("slot", "chest")
        player.equipamento[slot] = armadura
        info_item(f"Armadura equipada: {armadura['nome']}")

    # Dar poção inicial
    pocao = get_item_by_id("co-hp-l1")
    if pocao:
        player.inventario.append(pocao)
        player.inventario.append(dict(pocao))  # 2 poções
        info_item("Recebeu 2x Poção de Vida!")

    sucesso(f"\nVocê é agora um {player.classe}!")