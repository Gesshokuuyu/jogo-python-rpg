# game/locations/cave.py

import random
from game.entities.enemy import Enemy
from game.core.combat import iniciar_combate
from game.core.merchant import abrir_loja
from game.core.ui import (
    titulo, narrar, menu, escolha, aviso, sucesso,
    subtitulo, separador, COR_MENU, COR_BOSS
)
from colorama import Style

INIMIGOS_CAVERNA = ["e-troll", "e-esqueleto", "e-aranha"]
VITORIAS_NECESSARIAS = 3


def caverna(player):
    """Caverna das Sombras — inimigos mais fortes + mercador + mini-boss"""
    titulo("CAVERNA DAS SOMBRAS")
    narrar("O ar fica pesado e úmido conforme você desce pela caverna.")
    narrar("O som de gotas ecoa nas paredes de pedra escura...")

    while True:
        separador()
        print(COR_MENU + f"  Vitórias na caverna: {player.vitorias_caverna}/{VITORIAS_NECESSARIAS}")

        if player.vitorias_caverna >= VITORIAS_NECESSARIAS:
            sucesso("Você explorou toda a caverna!")
            menu(["Enfrentar o Golem de Pedra (Mini-Boss)", "Voltar"])
            op = escolha(validas=["1", "2"])

            if op == "1":
                if _boss_golem(player):
                    return
                if not player.esta_vivo():
                    return
            else:
                narrar("Você recua para se preparar melhor...")
                break
        else:
            menu(["Explorar (procurar inimigos)", "Mercador — Dúrin, o Anão", "Voltar à vila"])
            op = escolha(validas=["1", "2", "3"])

            if op == "1":
                _encontro(player)
                if not player.esta_vivo():
                    return
            elif op == "2":
                abrir_loja(player, "m-caverna")
            elif op == "3":
                narrar("Você retorna para a superfície...")
                break


def _encontro(player):
    """Encontro aleatório na caverna"""
    enemy_id = random.choice(INIMIGOS_CAVERNA)
    enemy = Enemy(enemy_id)

    narrar(f"Uma sombra enorme se aproxima... É um {enemy.nome}!")

    resultado = iniciar_combate(player, enemy)

    if resultado is True:
        player.vitorias_caverna += 1
    elif resultado is False:
        return


def _boss_golem(player):
    """Mini-boss: Golem de Pedra"""
    print(COR_BOSS + Style.BRIGHT + "\n  A terra treme sob seus pés...")
    narrar("Um imenso Golem de Pedra desperta diante de você!")
    narrar("Seus olhos brilham com uma luz vermelha ameaçadora...")

    golem = Enemy("e-golem")
    resultado = iniciar_combate(player, golem)

    if resultado is True:
        sucesso("O Golem desmorona! O caminho para a Torre de Morvak está aberto!")
        player.capitulo = max(player.capitulo, 3)
        return True
    return False
