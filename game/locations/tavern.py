# game/locations/tavern.py

from game.core.ui import (
    titulo, dialogo, narrar, menu, escolha, info_cura,
    aviso, sucesso, separador, mostrar_status, limparUI
)
from game.core.inventory import menu_inventario
from game.core.merchant import abrir_loja


def taverna(player):
    """Hub principal — Taverna de Lyris"""
    limparUI()
    titulo("TAVERNA DE LYRIS")
    narrar("Você empurra a pesada porta de madeira e entra na taverna.")
    narrar("O calor da lareira e o cheiro de cerveja preenchem o ar.")
    dialogo("Barkeep", "Bem-vindo, aventureiro! O que deseja?")

    while True:
        titulo("TAVERNA")
        menu([
            "Descansar (recuperar HP/Mana)",
            "Mercador — Baldric",
            "Ver Status",
            "Inventário",
            "Conversar com o velho sábio",
            "Sair da taverna"
        ])
        op = escolha(validas=["1", "2", "3", "4", "5", "6"])

        if op == "1":
            player.descansar()
            narrar("Você se senta perto da lareira e descansa...")
            info_cura(f"HP e Mana totalmente restaurados! ({player.hp}/{player.hp_max} HP, {player.mana}/{player.mana_max} MP)")

        elif op == "2":
            abrir_loja(player, "m-taverna")

        elif op == "3":
            mostrar_status(player)

        elif op == "4":
            menu_inventario(player)

        elif op == "5":
            _conversar_sabio(player)

        elif op == "6":
            limparUI()
            narrar("Você sai da taverna e sente a brisa fresca da noite.")
            break


def _conversar_sabio(player):
    limparUI()
    """O velho sábio dá dicas baseadas no capítulo atual"""
    if player.capitulo == 1:
        dialogo("Eldric, o Sábio",
                "A Floresta de Lyris está infestada de criaturas. "
                "Prove seu valor enfrentando os monstros lá.")
        narrar("O velho olha nos seus olhos com seriedade.")
        dialogo("Eldric, o Sábio",
                "Quando estiver mais forte, a caverna ao norte revelará seus segredos...")

    elif player.capitulo == 2:
        dialogo("Eldric, o Sábio",
                "Você cresceu, jovem guerreiro. A Caverna das Sombras "
                "guarda um Golem de Pedra. Derrote-o e o caminho à Torre será seu.")
        narrar("Ele aponta para um mapa velho na parede.")
        dialogo("Eldric, o Sábio",
                "Dúrin, o Anão, está na caverna. Ele vende equipamentos melhores.")

    elif player.capitulo == 3:
        dialogo("Eldric, o Sábio",
                "A Torre de Morvak... Poucos que entraram retornaram.")
        narrar("O velho segura sua mão com força.")
        dialogo("Eldric, o Sábio",
                "Morvak é poderoso. Prepare-se bem antes de enfrentá-lo. "
                "Compre as melhores armas e poções que puder.")

    elif player.capitulo >= 4:
        dialogo("Eldric, o Sábio",
                "Você é uma lenda, aventureiro! As terras de Lyris estão em paz graças a você.")