# game/locations/forest.py

import random
from game.entities.enemy import Enemy
from game.core.combat import iniciar_combate
from game.core.ui import (
    titulo, narrar, menu, escolha, aviso, sucesso,limparUI,
    subtitulo, separador, COR_MENU
)

INIMIGOS_FLORESTA = ["e-lobo", "e-goblin", "e-sombria"]
VITORIAS_NECESSARIAS = 3


def floresta(player):
    """Floresta de Lyris — encontros aleatórios até desbloquear caverna"""
    titulo("FLORESTA DE LYRIS")
    narrar("Você adentra a floresta densa. A luz do sol mal penetra as copas das árvores.")
    narrar("Sons estranhos ecoam entre os troncos retorcidos...")

    while True:
        separador()
        print(COR_MENU + f"  Vitórias na floresta: {player.vitorias_floresta}/{VITORIAS_NECESSARIAS}")

        if player.vitorias_floresta >= VITORIAS_NECESSARIAS:
            limparUI()
            sucesso("Você limpou a floresta! O caminho para a Caverna das Sombras está aberto!")
            player.capitulo = max(player.capitulo, 2)
            break

        menu(["Explorar (procurar inimigos)", "Voltar à vila"])
        op = escolha(validas=["1", "2"])

        limparUI()

        if op == "1":
            _encontro(player)
            if not player.esta_vivo():
                return
        elif op == "2":
            narrar("Você retorna à segurança da vila...")
            break


def _encontro(player):
    """Gera um encontro aleatório na floresta"""
    enemy_id = random.choice(INIMIGOS_FLORESTA)
    enemy = Enemy(enemy_id)

    narrar(f"Algo se move entre as árvores... É um(a) {enemy.nome}!")

    resultado = iniciar_combate(player, enemy)

    if resultado is True:
        player.vitorias_floresta += 1
    elif resultado is False:
        return  # morreu
    # None = fugiu
