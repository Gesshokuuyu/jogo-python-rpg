# game/core/story.py

from game.core.ui import (
    titulo, narrar, menu, escolha, aviso, separador,limparUI,
    COR_MENU, COR_AVISO
)
from game.locations.tavern import taverna
from game.locations.forest import floresta
from game.locations.cave import caverna
from game.locations.tower import torre


def inicio(player):
    """Loop principal de história — hub da vila de Lyris"""
    narrar("Você chega à vila de Lyris, uma pequena comunidade cercada por florestas sombrias.")
    narrar("Os moradores sussurram sobre uma torre escura no horizonte...")
    narrar("Dizem que Morvak, o Senhor das Sombras, ameaça destruir tudo.")
    narrar("Cabe a você, aventureiro, enfrentar essa ameaça.\n")

    while player.esta_vivo():
        titulo("VILA DE LYRIS")

        opcoes = ["Taverna (descansar, mercador, inventário)"]

        # Floresta sempre disponível
        opcoes.append("Floresta de Lyris")

        # Caverna desbloqueada após cap 2
        if player.capitulo >= 2:
            opcoes.append("Caverna das Sombras")
        else:
            opcoes.append(COR_AVISO + "Caverna das Sombras [BLOQUEADA]")

        # Torre desbloqueada após cap 3
        if player.capitulo >= 3:
            opcoes.append("Torre de Morvak (Boss Final)")
        else:
            opcoes.append(COR_AVISO + "Torre de Morvak [BLOQUEADA]")

        opcoes.append("Sair do jogo")

        menu(opcoes)

        total = len(opcoes)
        validas = [str(i) for i in range(1, total + 1)]
        op = escolha(validas=validas)

        limparUI()

        if op == "1":
            taverna(player)

        elif op == "2":
            floresta(player)

        elif op == "3":
            if player.capitulo >= 2:
                caverna(player)
            else:
                aviso("Você precisa provar seu valor na Floresta primeiro!")

        elif op == "4":
            if player.capitulo >= 3:
                resultado = torre(player)
                if resultado:
                    break
            else:
                aviso("Você precisa derrotar o Golem na Caverna primeiro!")

        elif op == "5":
            narrar("Até a próxima, aventureiro!")
            break

        if not player.esta_vivo():
            break
